# QUESTION 5: UNIVERSITY COURSE ENROLLMENT AND GRADE TRACKING SYSTEM

# Supplied data
students = [
    {
        "name": "Amos",
        "courses": {
            "Math": [75, 80, 78],
            "English": [85, 88, 90]
        }
    },
    {
        "name": "Betty",
        "courses": {
            "Math": [60, 58, 62],
            "English": [92, 94, 89]
        }
    },
    {
        "name": "Charles",
        "courses": {
            "Math": [85, 88, 90],
            "Science": [80, 82, 85]
        }
    },
    {
        "name": "Diana",
        "courses": {
            "Math": [45, 48, 50],
            "English": [70, 72, 68]
        }
    }
]

# Additional test dataset with edge cases
students_test = [
    {
        "name": "Amos",
        "courses": {
            "Math": [75, 80, 78],
            "English": [85, 88, 90]
        }
    },
    {
        "name": "Betty",
        "courses": {
            "Math": [60, 58, 62],
            "English": [92, 94, 89]
        }
    },
    {
        "name": "Charles",
        "courses": {
            "Math": [85, 88, 90],
            "Science": [80, 82, 85]
        }
    },
    {
        "name": "Diana",
        "courses": {
            "Math": [45, 48, 50],
            "English": [70, 72, 68]
        }
    },
    {
        "name": "Edward",
        "courses": {
            "Math": [90, 92, 88],
            "English": [85, 87, 89],
            "Science": [95, 93, 94]
        }
    },
    {
        "name": "Fiona",
        "courses": {
            "Math": [55, 58, 52],
            "English": [65, 68, 70]
        }
    },
    {
        "name": "George",
        "courses": {
            "Math": [40, 42, 38],
            "English": [50, 48, 45],
            "Science": [30, 35, 32]
        }
    },
    {
        "name": "Helen",
        "courses": {
            "Math": [95, 98, 97],
            "Science": [88, 90, 92]
        }
    },
    {
        "name": "Ivan",
        "courses": {
            "Math": [70, 72, 68],
            "English": [80, 82, 78],
            "Science": [75, 77, 73]
        }
    },
    {
        "name": "Jane",
        "courses": {
            "Math": [50, 52, 48],
            "English": [60, 62, 58]
        }
    },
    {
        "name": "Kevin",
        "courses": {
            "Math": [35, 40, 38],
            "English": [45, 48, 42]
        }
    },
    {
        "name": "Linda",
        "courses": {
            "Math": [85, 88, 90],
            "English": [75, 78, 80],
            "Science": [90, 92, 88]
        }
    }
]

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def assign_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

def determine_status(student_name, course_grades):
    has_f = False
    has_c = False
    
    for course, grade in course_grades.items():
        if grade == "F":
            has_f = True
        elif grade == "C":
            has_c = True
    
    if has_f:
        return "Critical"
    elif has_c:
        return "At-Risk"
    else:
        return "Good Standing"

def calculate_course_statistics(all_students_data):
    course_sums = {}
    course_counts = {}
    course_students = {}
    
    for student in all_students_data:
        name = student["name"]
        courses = student["courses"]
        
        for course_name, marks in courses.items():
            avg = calculate_average(marks)
            grade = assign_grade(avg)
            
            if course_name not in course_sums:
                course_sums[course_name] = avg
                course_counts[course_name] = 1
                course_students[course_name] = [name]
            else:
                course_sums[course_name] += avg
                course_counts[course_name] += 1
                course_students[course_name].append(name)
    
    course_averages = {}
    for course_name in course_sums:
        course_averages[course_name] = course_sums[course_name] / course_counts[course_name]
    
    pass_counts = {}
    for course_name in course_students:
        pass_count = 0
        for student_name in course_students[course_name]:
            for student in all_students_data:
                if student["name"] == student_name:
                    if course_name in student["courses"]:
                        marks = student["courses"][course_name]
                        avg = calculate_average(marks)
                        grade = assign_grade(avg)
                        if grade != "F":
                            pass_count += 1
        pass_counts[course_name] = pass_count
    
    lowest_course = min(course_averages.items(), key=lambda x: x[1])
    
    return course_averages, course_counts, pass_counts, lowest_course

def generate_academic_report(students_data):
    print("=" * 70)
    print("           UNIVERSITY ACADEMIC PERFORMANCE REPORT")
    print("=" * 70)
    
    student_overall_averages = {}
    student_statuses = {}
    student_course_grades = {}
    
    print("\n--- PART A: INDIVIDUAL STUDENT PERFORMANCE ---")
    
    for student in students_data:
        name = student["name"]
        courses = student["courses"]
        course_averages = {}
        course_grades = {}
        total_marks = 0
        mark_count = 0
        
        print(f"\nStudent: {name}")
        print("-" * 50)
        
        for course_name, marks in courses.items():
            avg = calculate_average(marks)
            grade = assign_grade(avg)
            course_averages[course_name] = avg
            course_grades[course_name] = grade
            total_marks += avg
            mark_count += 1
            print(f"  {course_name}: Average = {avg:.1f}, Grade = {grade}")
        
        overall_avg = total_marks / mark_count
        student_overall_averages[name] = overall_avg
        student_course_grades[name] = course_grades
        
        status = determine_status(name, course_grades)
        student_statuses[name] = status
        print(f"  Overall Average: {overall_avg:.1f}")
        print(f"  Academic Status: {status}")
        
        improvement_courses = []
        for course_name, grade in course_grades.items():
            if grade == "C" or grade == "F":
                improvement_courses.append(course_name)
        
        if improvement_courses:
            print(f"  Courses requiring improvement: {', '.join(improvement_courses)}")
        else:
            print("  Courses requiring improvement: None")
        
        if status == "Critical" or status == "At-Risk":
            print("  Recommendation: TUTORING REQUIRED")
    
    course_averages, course_counts, pass_counts, lowest_course = calculate_course_statistics(students_data)
    
    print("\n--- PART B: COURSE STATISTICS ---")
    print("-" * 50)
    
    for course_name in sorted(course_averages.keys()):
        avg = course_averages[course_name]
        count = course_counts[course_name]
        passes = pass_counts[course_name]
        print(f"{course_name}:")
        print(f"  Overall Average: {avg:.1f}")
        print(f"  Number of Students Enrolled: {count}")
        print(f"  Number of Students Passing: {passes}")
        print(f"  Passing Rate: {(passes/count)*100:.1f}%")
    
    print(f"\nCourse with Lowest Overall Average: {lowest_course[0]} ({lowest_course[1]:.1f})")
    print(f"Course Requiring Greatest Academic Attention: {lowest_course[0]}")
    
    print("\n--- PART C: INTERVENTION PRIORITY LIST ---")
    print("-" * 50)
    
    critical_students = []
    at_risk_students = []
    good_standing_students = []
    
    for name, status in student_statuses.items():
        if status == "Critical":
            critical_students.append(name)
        elif status == "At-Risk":
            at_risk_students.append(name)
        else:
            good_standing_students.append(name)
    
    priority_list = []
    
    for name in critical_students:
        priority_list.append((name, "Critical", student_overall_averages[name]))
    
    for name in at_risk_students:
        priority_list.append((name, "At-Risk", student_overall_averages[name]))
    
    for name in good_standing_students:
        priority_list.append((name, "Good Standing", student_overall_averages[name]))
    
    priority_list.sort(key=lambda x: x[2], reverse=True)
    
    print("\nPriority Ranking (Highest Priority to Lowest):")
    for i, (name, status, avg) in enumerate(priority_list, 1):
        print(f"{i}. {name} - Status: {status}, Overall Average: {avg:.1f}")
    
    print("\n" + "=" * 70)
    print("                    END OF REPORT")
    print("=" * 70)

print("\n" + "=" * 70)
print("          RUNNING WITH SUPPLIED DATASET")
print("=" * 70)
generate_academic_report(students)

print("\n\n" + "=" * 70)
print("          RUNNING WITH ADDITIONAL TEST DATASET")
print("=" * 70)
generate_academic_report(students_test)