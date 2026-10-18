"""
RECORD CHECK  -  my version
===========================

Name  : Noorshaan Uteene
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    diff = value - limit
    perc = (value / limit * 100) if limit != 0 else 0
    status = "OVER LIMIT" if value > limit else "OK"
    return diff, perc, status

def print_report(record):
    diff, perc, status = check_record(record["value"], record["limit"])
    print(f"{record['label']}: {int(record['value'])}/{int(record['limit'])} ({perc:.1f}%) -> {status}")

def load_records(path):
    recs = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            recs.append({"label": label, "value": float(value), "limit": float(limit)})
    return recs

#that all i could do i still need some times to understand
#i got some help to do this template
