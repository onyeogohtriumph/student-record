"""Generate a fictional student dataset and save it as students.csv."""
import csv
import random

random.seed(42)  # makes the output reproducible

NUM_STUDENTS = 200
DEPARTMENTS = [
    "Computer Science", "Electrical Engineering", "Mechanical Engineering",
    "Accounting", "Economics", "Mass Communication", "Biochemistry", "Law",
]
LEVELS = [100, 200, 300, 400, 500]

MALE_NAMES = ["Chinedu", "Tunde", "Emeka", "Ibrahim", "Segun", "Obinna", "Femi",
              "Musa", "Daniel", "Chukwuma", "Kelechi", "Yusuf", "David", "Ayodele"]
FEMALE_NAMES = ["Ngozi", "Aisha", "Funke", "Chiamaka", "Blessing", "Zainab", "Temitope",
                "Amaka", "Fatima", "Folake", "Ifeoma", "Grace", "Bukola", "Halima"]
SURNAMES = ["Okafor", "Adeyemi", "Bello", "Nwosu", "Balogun", "Eze", "Abubakar",
            "Ogunleye", "Okonkwo", "Lawal", "Chukwu", "Afolabi", "Danjuma", "Ibe"]


def make_student(index):
    gender = random.choice(["Male", "Female"])
    first = random.choice(MALE_NAMES if gender == "Male" else FEMALE_NAMES)
    name = f"{first} {random.choice(SURNAMES)}"

    attendance = round(min(100, max(40, random.gauss(78, 13))), 1)
    # Exam score loosely follows attendance, plus random noise
    score = attendance * 0.6 + random.gauss(22, 8)
    score = round(min(100, max(15, score)), 1)
    return {
        "Student_ID": f"STU{index:04d}",
        "Full_Name": name,
        "Gender": gender,
        "Department": random.choice(DEPARTMENTS),
        "Level": random.choice(LEVELS),
        "Attendance_Percentage": attendance,
        "Average_Exam_Score": score,
    }


def main():
    students = [make_student(i) for i in range(1, NUM_STUDENTS + 1)]
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    print(f"Created students.csv with {len(students)} records.")


if __name__ == "__main__":
    main()
