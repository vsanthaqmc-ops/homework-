student_records = {
    "Alice": "Mathematics",
    "Bob": "Physics",
    "Charlie": "Chemistry",
    "Duplicate_Key": "Biology"  
}


student_name = "Alice"
subject = student_records.get(student_name, "Subject Not Found")
print(f"1. Safe Access -> {student_name}'s subject: {subject}")


student_records["David"] = "History"          
student_records["Bob"] = "Astrophysics"       
print(f"2. Updated Records: {student_records}")


student_records.pop("Duplicate_Key", None)    
print(f"3. Cleaned Records: {student_records}")


dict_length = len(student_records)
print(f"4. Total Records: {dict_length}")
print("5. Final Iteration:")
for student, sub in student_records.items():
    print(f"   - Student: {student} | Subject: {sub}")
    
     