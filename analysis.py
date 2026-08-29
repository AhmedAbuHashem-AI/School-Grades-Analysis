import pandas as pd
import matplotlib.pyplot as plt

# Read the file
df = pd.read_csv("school_grades.csv.txt")

# --------------------------------
# Average grade
# --------------------------------
average_grade = df["grade"].mean()
print("Average Grade:")
print(average_grade)

# --------------------------------
# Top student
# --------------------------------
top_student = df.loc[df["grade"].idxmax()]
print("\nTop Student:")
print(top_student)

# --------------------------------
# Lowest student
# --------------------------------
lowest_student = df.loc[df["grade"].idxmin()]
print("\nLowest Student:")
print(lowest_student)

# --------------------------------
# Total number of students
# --------------------------------
total_students = len(df)
print("\nTotal Students:")
print(total_students)

# --------------------------------
# Passed and failed students
# --------------------------------
passed_students = df[df["grade"] > 50]
failed_students = df[df["grade"] <= 50]
passed_count = len(passed_students)
failed_count = len(failed_students)
print("\nPassed Students:")
print(passed_count)
print("\nFailed Students:")
print(failed_count)

# --------------------------------
# Excellent students (>85)
# --------------------------------
excellent_students = df[df["grade"] > 85]
print("\nExcellent Students:")
print(excellent_students)

# --------------------------------
# Average grade by gender
# --------------------------------
gender_average = df.groupby("gender")["grade"].mean()
print("\nAverage Grade by Gender:")
print(gender_average)

# --------------------------------
# Best male student
# --------------------------------
male_students = df[df["gender"] == "Male"]
best_male = male_students.loc[male_students["grade"].idxmax()]
print("\nBest Male Student:")
print(best_male)

# --------------------------------
# Best female student
# --------------------------------
female_students = df[df["gender"] == "Female"]
best_female = female_students.loc[female_students["grade"].idxmax()]
print("\nBest Female Student:")
print(best_female)

# --------------------------------
# Gender count
# --------------------------------
gender_count = df["gender"].value_counts()
print("\nGender Count:")
print(gender_count)

# --------------------------------
# Bar Chart for grades
# --------------------------------
plt.figure()
plt.bar(df["name"], df["grade"])
plt.title("Students Grades")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.show()

# --------------------------------
# Pie Chart for Passed vs Failed
# --------------------------------
plt.figure()
labels = ["Passed", "Failed"]
sizes = [passed_count, failed_count]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Passed vs Failed")
plt.show()

# --------------------------------
# Scatter Plot (Age vs Grade)
# --------------------------------
plt.figure()
plt.scatter(df["age"], df["grade"])
plt.title("Age vs Grade")
plt.xlabel("Age")
plt.ylabel("Grade")
plt.show()

# --------------------------------
# Create CSV report
# --------------------------------
report = pd.DataFrame({
    "Metric": [
        "Average Grade",
        "Top Student",
        "Lowest Student",
        "Total Students",
        "Passed Students",
        "Failed Students",
        "Best Male",
        "Best Female"
    ],
    "Value": [
        average_grade,
        top_student["name"],
        lowest_student["name"],
        total_students,
        passed_count,
        failed_count,
        best_male["name"],
        best_female["name"]
    ]
})
report.to_csv("school_report.csv", index=False)
print("\nReport saved successfully.")