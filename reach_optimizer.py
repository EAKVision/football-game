import asyncio
import sqlite3
import time
import os
import socket

DB_PATH = os.path.expanduser("~/EAKV-Reels/data/reach_queue.db")

def sd_notify(state: str):
    addr = os.environ.get("NOTIFY_SOCKET")
    if not addr:
        return
    if addr.startswith("@"):
        addr = "\0" + addr[1:]
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        sock.sendto(state.encode(), addr)
    finally:
        sock.close()

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS outbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payload TEXT NOT NULL,
            target TEXT NOT NULL,
            status TEXT DEFAULT 'PENDING',
            attempts INTEGER DEFAULT 0,
            next_retry REAL DEFAULT 0
        )
    """)
    conn.commit()
    return conn

async def dispatch_event(target: str, payload: str) -> bool:
    await asyncio.sleep(0.2)
    print(f"[DISPATCHED -> {target}] {payload}", flush=True)
    return True

async def worker_loop(conn: sqlite3.Connection):
    sd_notify("READY=1")
    while True:
        sd_notify("WATCHDOG=1")
        now = time.time()
        cursor = conn.execute(
            "SELECT id, target, payload, attempts FROM outbox "
            "WHERE status = 'PENDING' AND next_retry <= ? LIMIT 5",
            (now,)
        )
        rows = cursor.fetchall()

        for row_id, target, payload, attempts in rows:
            success = await dispatch_event(target, payload)
            if success:
                conn.execute("UPDATE outbox SET status = 'SENT' WHERE id = ?", (row_id,))
            else:
                backoff = min(3600, (2 ** attempts) * 5)
                conn.execute(
                    "UPDATE outbox SET attempts = ?, next_retry = ? WHERE id = ?",
                    (attempts + 1, now + backoff, row_id)
                )
            conn.commit()

        await asyncio.sleep(2)

if __name__ == "__main__":
    db = init_db()
    asyncio.run(worker_loop(db))
