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

#Threshold

print("=" * 30)

source_ip=(input("Enter source_ip: "))
failed_logins=int(input("Enter failed logins: "))
total_attempts=int(input("Emter total_attempts: "))

#Typical

#now i will calculate difference(sucesssfull logins)
successfull_logins = total_attempts - failed_logins

#now i will calculate percent failed
percent_failed = failed_logins / total_attempts * 100

#Excellent

success_rate = 100 - percent_failed

# Final report 
label = "Miniproject"
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)



print(f"source_IP :{source_ip}")
print(f"Failed :{failed_logins:10.2f}")
print(f"Total :{total_attempts:10.2f}")
print(f"Success :{successfull_logins:+10.2f}")
print(f"Percent :{percent_failed:10.2f}%")
print(f"success rate: {success_rate:10.2f}%")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
