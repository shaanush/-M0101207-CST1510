"""
RECORD CHECK  -  my version
===========================

Name  : Noorshaan Uteene
Lane  : Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """the function status_of hold percent which contain number then goes through if statemnet and return text"""
    if percent >= 100:
        return"OVER LIMIT"
    elif percent >= 90:
        return"WARNING"
    else:
        return"OK"

def check(value, limit):
    """this function check hold 2 parameters value and limit they are use to calculate difference and percentage and return them on 1 line"""
    difference = value - limit
    percentage = (value / limit) * 100
    """ calculate the difference and percentage"""
    return(difference, percentage)

def print_report(label, value,limit,difference,percent,status):
    """this function is use to print the report"""
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


count = 0
while True:
    label = input("source_IP: ")
    if label == "quit":
        break
    value = float(input("Failed logins: "))
    limit = float(input("Total attempts: "))
    difference, percent = check(value,limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        count += 1
    print_report(label,value,limit,difference,percent,status)
    print(f"{'Record over limit:':<15} {count}")






#label = input("Source_IP: ")
#value = float(input("Failed logins: "))
#limit = float(input("Total attempts: "))
#difference, percent = check(value,limit)
#status = status_of(percent)
#print_report(label, value,limit,difference,percent,status)



# your report lines go here
    #print("=" * 34)


# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

#label = input("Enter a Source_IP: ")   # replace with an input() call
#value = float(input("Enter Failed logins: "))   # replace with an input() call, converted
#limit = float(input("Enter Total attempts: "))   # replace with an input() call, converted



# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.


#difference = difference = value - limit    # replace with your code
#percent = (value / limit) * 100   # replace with your code
#status = status_of(percent)      # replace with your code


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


#print()
#print("=" * 34)
#print(f"  RECORD CHECK  -  {label}")
#print("=" * 34)

#print(f"Source_IP: {label}")   
#print(f"Failed logins: {value} ")
#print(f"Total attempts: {limit}")
#print(f"status: {status}")
#print(f"Difference: {difference:15.2f}")
#print(f"Percent: {percent:18.2f}%")




# your report lines go here
#print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
