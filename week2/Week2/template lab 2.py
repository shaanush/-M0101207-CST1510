"""
RECORD CHECK  -  my version
===========================

Name  : Noorshaan Uteene
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Enter label: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

print(label)
print(value)
print(limit)

difference = value - limit
percent    = value/limit * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent <= 90:
        status ="WARNINIG"
else:
    status = "OK"



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

count = 0
over_limit_count = 0 

while True:
     label = input("Enter label: ")
     if label == "done":
      break
     value = float(input("Enter value: "))
     limit = float(input("Enter limit: "))
     percent = value / limit * 100

     if percent >= 100:
         status = "OVER LIMIT"
         over_limit_count += 1
     else:
         status = "OK"
     count= count + 1


print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
