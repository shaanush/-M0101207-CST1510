"""
RECORD CHECK  -  my version
===========================

Name  :  Noorshaan Uteene
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""





#IMPORTANT MESSAGE
"""Dear sir my code isnt working due its not opening the "records.txt" file so am unable to run it,Thank you"""








# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """here it checks a value against its limit"""
    difference = value - limit
    percentage = (value / limit) * 100 if limit != 0 else 0 #here if limit is 0 we cant devide by zero because it gives an error so we set percenatge to 0
                                                            #otherwise we calculate (value / limit) * 100 to see how much of the limit was used
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference,percentage,status    


def print_report(label, value,limit,difference,percent,status):
    """ here it prints the report for 1 record"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"{'Source_IP:':<15} {label}")
    print(f"{'Failed logins:':<15} {value:.1f}")
    print(f"{'Total attempts:':<15} {limit:<15.1f}")
    print(f"{'status :':<15} {status}")
    print(f"{'Difference :':<15} {difference:<15.2f}")
    print(f"{'Percent:':<15} {percent:<15.2f}%")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """ here it will load records from file into a list"""
    records = []
    with open(path , "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            record = {
                "label":parts[0],
                "value":float(parts[1]),
                "limit":float(parts[2]),
            }
            records.append(record)
        return records


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

records = load_records("records.txt")
over_count = 0

for record in records:
    difference,percent,status = check_record(
    record["value"],
    record["limit"])
    
    print_report
    (record["label"],
    record["value"],
    record["limit"],
difference,percent,status)
    
    if status == "OVER LIMIT":
        over_count = over_count + 1
print(f"Total OVER LIMIT:{over_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
