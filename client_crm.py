#!/usr/bin/env python3
import sqlite3

CRM_DB = "akv_crm.db"

def init_crm():
    conn = sqlite3.connect(CRM_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prospect_name TEXT,
            niche_source TEXT,
            status TEXT,
            deal_value TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_lead(name, source, status, value):
    init_crm()
    conn = sqlite3.connect(CRM_DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (prospect_name, niche_source, status, deal_value) VALUES (?, ?, ?, ?)",
                   (name, source, status, value))
    conn.commit()
    conn.close()
    print(f"🎯 [CRM] Lead successfully logged: {name} ({source}) -> Status: {status}")

if __name__ == "__main__":
    add_lead("Enterprise AI Director", "Gun.io / Inbound Outreach", "Active Pipeline", "$120/hr")
