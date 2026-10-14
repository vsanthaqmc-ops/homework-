marks = [85, 92, 78, 90, 64, 88, 95, 72]

num_students = len(marks)
first_mark = marks[0]
top_three = marks[:3]

s
total_marks = sum(marks)
average_mark = total_marks / num_students
smallest_mark = min(marks)
largest_mark = max(marks)


print("--- Student Marks Summary ---")
print(f"Total number of students: {num_students}")
print(f"First student's mark: {first_mark}")
print(f"First three marks (slicing): {top_three}")
print(f"Total marks: {total_marks}")
print(f"Average mark: {average_mark:.}")
print(f"Smallest mark: {smallest_mark}")
print(f"Largest mark: {largest_mark}")