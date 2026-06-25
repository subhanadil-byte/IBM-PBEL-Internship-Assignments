# IBM PBEL Python Assignment - 2
# Submitted by: Subhan Adil

import pandas as pd

# Data Initialization
dataset = {
    'Staff_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Employee_Name': ['Aman', 'Priya', 'Rahul', 'Sneha', 'Vikas', 'Neha', 'Rohit', 'Pooja', 'Karan', 'Anjali'],
    'Dept_Group': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'Base_Pay': [52000, 46000, 61000, 74000, 49000, 57000, 66000, 59000, 48000, 73000],
    'Yrs_Exp': [2, 1, 5, 7, 2, 4, 6, 3, 1, 8],
    'Hire_Date': ['2022-01-15', '2023-02-10', '2020-06-20', '2018-03-12', '2022-08-01', '2021-07-18', '2019-11-25', '2021-04-10', '2023-01-05', '2017-09-15']
}
df = pd.DataFrame(dataset)

# Q1
print(df.head())

# Q2
print(df.tail(3))

# Q3
print(df.shape)

# Q4
print(df.columns)

# Q5
print(df.dtypes)

# Q6
df.info()

# Q7
print(df.describe())

# Q8
print(df["Employee_Name"])

# Q9
print(df[["Employee_Name", "Base_Pay"]])

# Q10
print(len(df))

# Q11
print(df[df["Base_Pay"] > 55000])

# Q12
print(df[df["Dept_Group"] == "IT"])

# Q13
print(df[df["Yrs_Exp"] > 3])

# Q14
print(df.sort_values("Base_Pay"))

# Q15
print(df.sort_values("Base_Pay", ascending=False))

# Q16
print(df["Base_Pay"].mean())

# Q17
print(df["Base_Pay"].max())

# Q18
print(df["Base_Pay"].min())

# Q19
print(df["Dept_Group"].value_counts())

# Q20
print(df["Base_Pay"].sum())

# Q21
print(df.groupby("Dept_Group")["Base_Pay"].mean())

# Q22
print(df.groupby("Dept_Group")["Base_Pay"].max())

# Q23
print(df[df["Base_Pay"] == df["Base_Pay"].max()])

# Q24
print(df[df["Base_Pay"] == df["Base_Pay"].min()])

# Q25
df["Perk_Bonus"] = df["Base_Pay"] * 0.10
print(df)

# Q26
df["Deduct_Tax"] = df["Base_Pay"] * 0.05
print(df)

# Q27
df["Final_Pay"] = df["Base_Pay"] + df["Perk_Bonus"] - df["Deduct_Tax"]
print(df)

# Q28
df["Hire_Date"] = pd.to_datetime(df["Hire_Date"])
print(df)

# Q29
df["Year_Hired"] = df["Hire_Date"].dt.year
print(df)

# Q30
df["Month_Hired"] = df["Hire_Date"].dt.month
print(df)

# Q31
print(pd.pivot_table(df, values="Base_Pay", index="Dept_Group", aggfunc="mean"))

# Q32
df["Pay_Rank"] = df["Base_Pay"].rank(ascending=False)
print(df[["Employee_Name", "Base_Pay", "Pay_Rank"]])

# Q33
print(df.nlargest(3, "Base_Pay"))

# Q34
print(df.nsmallest(3, "Base_Pay"))

# Q35
print(df[df.duplicated()])

# Q36
print(df.isnull().sum())

# Q37
df.rename(columns={"Base_Pay": "Monthly_Salary"}, inplace=True)
print(df.columns)

# Q38
df["Dept_Group"] = df["Dept_Group"].replace("HR", "Human Resource")
print(df)

# Q39
df.to_csv("staff_records.csv", index=False)

# Q40
df.to_excel("staff_records.xlsx", index=False)
