"""
RECORD CHECK  -  my version
===========================

Name  : Noorshaan Uteee
Lane  : Cyber   
Date  : 9 oct 2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    if percent >= 100:
        return "over limit"
    elif percent >= 90:
        return "warning"
    else:
        return "ok"

def check(value, limit):
    difference=value - limit
    percent= (value/limit*100)if limit!=0 else 0
    return difference,percent

def print_report(label,value,limit,difference,percent,status):
    print|()
    print("=" * 34)
    print(f"record check - {label}")
    print("=" * 34)
    print(f"source ip: {label}")
    print(f" Failed : {value:10.2f}")
    print(f" Limit : {limit:10.2f}")
    print(f" Diff : {difference:10.2f}")
    print(f" Percent : {percent:9.2f} %")
    print(f" Status : {status:>10}")
    print("=" * 34)


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = 0.0   # replace with your code
percent = 0.0       # replace with your code
status = ""          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
