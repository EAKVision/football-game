import re

TARGET_KEYWORDS = [
    "Systems Software Engineer", "Linux Engineer", "C Programming",
    "POSIX APIs", "Low-Latency", "p95 tail latency",
    "Backend Infrastructure", "Distributed Systems",
    "World Record Holder", "Valgrind", "GDB"
]

PROFILE_TEXT = """
Software Developer & Systems Engineer | C, POSIX, Python & Linux Architecture | Sub-12ms Low-Latency Telemetry | World Record Holder 🥇
Systems Engineer (C & Unix) by day. World Record Holder & Hybrid Athlete by design.
Core Focus: Low-level systems engineering & zero-dependency C programming (42 methodology).
Unix/Linux architecture, POSIX APIs & deterministic memory management (malloc/free, Valgrind & GDB profiling).
High-throughput asynchronous pipelines & custom UDP worker nodes maintaining p95 tail latency under 12ms.
Core Stack: C · POSIX · Linux/Ubuntu · Python (asyncio, FastAPI) · SQLite · UDP/WebSockets · Bash · Git · Valgrind/GDB
github.com/EAKVision. Currently open to Systems Software Engineer, Linux Engineer, Backend Infrastructure, and Distributed Systems roles.
"""

def audit_seo():
    print("=" * 60)
    print("      ELITE AKV LINKEDIN & GOOGLE SEO RANK AUDITOR")
    print("=" * 60)
    text_lower = PROFILE_TEXT.lower()
    score = 0
    missing = []
    for kw in TARGET_KEYWORDS:
        matches = len(re.findall(re.escape(kw.lower()), text_lower))
        if matches > 0:
            print(f"  [MATCH] {kw} ({matches}x)")
            score += 10
        else:
            print(f"  [MISSING] {kw}")
            missing.append(kw)
    seo_score = min(100, score)
    print("-" * 60)
    print(f"Global Search Indexing Score: {seo_score}/100")
    if missing:
        print(f"Recommended additions: {missing}")
    print("=" * 60)

if __name__ == "__main__":
    audit_seo()
