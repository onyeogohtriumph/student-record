# Fictional Student Dataset

A synthetic dataset of 200 students generated with Python (standard library only).
All names and values are made up.

## Columns
| Column | Description |
|---|---|
| Student_ID | Unique ID (STU0001 to STU0200) |
| Full_Name | Fictional student name |
| Gender | Male or Female |
| Department | One of 8 departments |
| Level | 100, 200, 300, 400 or 500 |
| Attendance_Percentage | 40 to 100 |
| Average_Exam_Score | 15 to 100, loosely correlated with attendance |

## Run
```
python generate_dataset.py
```
This creates `students.csv`.
