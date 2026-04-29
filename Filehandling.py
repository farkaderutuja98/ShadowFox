import csv

# Step 1: Read CSV file
students = []

with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Convert marks to integers
        maths = int(row["Maths"])
        science = int(row["Science"])
        english = int(row["English"])

        # Step 3: Calculate total
        total = maths + science + english

        # Step 4: Calculate average
        average = total / 3

        # Add new fields
        row["Total_Marks"] = total
        row["Average"] = round(average, 2)

        students.append(row)

# Step 5: Write to new CSV file
with open("updated_student_marks.csv", "w", newline="") as file:
    fieldnames = ["Name", "Maths", "Science", "English", "Total_Marks", "Average"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("New file created: updated_student_marks.csv")