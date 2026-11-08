"""
RECORD CHECK  -  my version
===========================

Name  : Noorshaan Uteen Sahil
Lane  : Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cyber.csv")# replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df.to_string(index=False))

print("\nNot OK rows:")
print(df[df["status"] != "OK"].to_string(index=False))

print("\nCount per status:")
counts = df.groupby("status").size()
print(counts)

df.to_csv("output.csv", index=False)

counts.plot(kind="bar")
plt.title("Count per status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_chart.png")
print("\nSaved output.csv and status_chart.png")

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
