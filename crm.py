#!/usr/bin/env python3
import csv
import os
from datetime import datetime

CRM_FILE = "recruiter_crm.csv"
HEADERS = ["Name", "Company", "Date_Contacted", "Status", "Notes"]

def init_crm():
    if not os.path.exists(CRM_FILE):
        with open(CRM_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            today = datetime.now().strftime("%Y-%m-%d")
            writer.writerow(["Olga Molgacheva", "Akvelon", today, "Sent Initial DM", "Sent Telemetry Engine pitch"])

def view_crm():
    init_crm()
    print("\n\033[1;36m=== RECRUITER OUTREACH PIPELINE ===\033[0m")
    with open(CRM_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contact_date = datetime.strptime(row["Date_Contacted"], "%Y-%m-%d")
            days_ago = (datetime.now() - contact_date).days
            # LinkedIn recruiters manage 30-50 roles; follow up after 5 business days
            alert = " \033[1;31m[FOLLOW UP DUE!]\033[0m" if days_ago >= 5 and "Replied" not in row["Status"] else ""
            print(f"- {row['Name']} ({row['Company']}) | Sent: {row['Date_Contacted']} ({days_ago}d ago) | Status: {row['Status']}{alert}")
    print()

def add_recruiter():
    init_crm()
    name = input("Recruiter Name: ").strip()
    company = input("Company: ").strip()
    notes = input("Pitch / Role Notes: ").strip()
    today = datetime.now().strftime("%Y-%m-%d")
    with open(CRM_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, company, today, "Sent Initial DM", notes])
    print(f"\033[1;32m[✓] Logged {name} at {company}.\033[0m\n")

if __name__ == "__main__":
    init_crm()
    while True:
        print("1. View Pipeline & Follow-Up Alerts")
        print("2. Log New Recruiter Outreach")
        print("3. Exit")
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            view_crm()
        elif choice == "2":
            add_recruiter()
        else:
            break
