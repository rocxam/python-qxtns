# QUESTION 1: SCHOOL CAFETERIA MEAL PLANNING SYSTEM

# Full dataset with 100 transactions including edge cases
meal_data = [
    # MONDAY TRANSACTIONS
    ("S001", "Amos", "Monday", "Lunch", "Beans and Matooke", 1500),
    ("S002", "Betty", "Monday", "Lunch", "Chapati and Beans", 1800),
    ("S003", "Charles", "Monday", "Lunch", "Soda", 1000),
    ("S004", "Diana", "Monday", "Lunch", "Juice", 1500),
    ("S005", "Emmanuel", "Monday", "Lunch", "Pilau", 3500),
    ("S006", "Faith", "Monday", "Lunch", "Chips and Sausage", 3000),
    ("S007", "George", "Monday", "Lunch", "Rolex", 2500),
    ("S008", "Hannah", "Monday", "Lunch", "Fish and Chips", 4000),
    ("S009", "Isaac", "Monday", "Lunch", "Pasta", 2200),
    ("S010", "Jessica", "Monday", "Lunch", "Burger", 2000),
    ("S011", "Kevin", "Monday", "Lunch", "Pizza", 2500),
    ("S012", "Lilian", "Monday", "Lunch", "Chicken and Rice", 3500),
    ("S013", "Moses", "Monday", "Lunch", "Beans and Matooke", 1500),
    ("S014", "Naomi", "Monday", "Lunch", "Chapati and Beans", 1800),
    ("S015", "Oscar", "Monday", "Lunch", "Soda", 1000),

    # TUESDAY TRANSACTIONS
    ("S016", "Priscilla", "Tuesday", "Lunch", "Juice", 1500),
    ("S017", "Quinn", "Tuesday", "Lunch", "Pilau", 3500),
    ("S018", "Rebecca", "Tuesday", "Lunch", "Chips and Sausage", 3000),
    ("S019", "Samuel", "Tuesday", "Lunch", "Rolex", 2500),
    ("S020", "Tracy", "Tuesday", "Lunch", "Fish and Chips", 4000),
    ("S021", "Umar", "Tuesday", "Lunch", "Pizza", 2500),
    ("S022", "Victoria", "Tuesday", "Lunch", "Chicken and Rice", 3500),
    ("S023", "William", "Tuesday", "Lunch", "Pasta", 2200),
    ("S024", "Xavier", "Tuesday", "Lunch", "Fish and Chips", 4000),
    ("S025", "Yvonne", "Tuesday", "Lunch", "Chips and Sausage", 3000),
    ("S026", "Zachary", "Tuesday", "Lunch", "Chapati and Beans", 1800),
    ("S001", "Amos", "Tuesday", "Lunch", "Burger", 2000),
    ("S002", "Betty", "Tuesday", "Lunch", "Pasta", 2200),

    # WEDNESDAY TRANSACTIONS
    ("S003", "Charles", "Wednesday", "Lunch", "Rolex", 2500),
    ("S004", "Diana", "Wednesday", "Lunch", "Beans and Matooke", 1500),
    ("S005", "Emmanuel", "Wednesday", "Lunch", "Chicken and Rice", 3500),
    ("S006", "Faith", "Wednesday", "Lunch", "Pizza", 2500),
    ("S007", "George", "Wednesday", "Lunch", "Fish and Chips", 4000),
    ("S008", "Hannah", "Wednesday", "Lunch", "Burger", 2000),
    ("S009", "Isaac", "Wednesday", "Lunch", "Juice", 1500),
    ("S010", "Jessica", "Wednesday", "Lunch", "Pilau", 3500),
    ("S027", "Alice", "Wednesday", "Lunch", "Soda", 1000),
    ("S028", "Brian", "Wednesday", "Lunch", "Chips and Sausage", 3000),

    # THURSDAY TRANSACTIONS
    ("S011", "Kevin", "Thursday", "Lunch", "Pasta", 2200),
    ("S012", "Lilian", "Thursday", "Lunch", "Rolex", 2500),
    ("S013", "Moses", "Thursday", "Lunch", "Fish and Chips", 4000),
    ("S014", "Naomi", "Thursday", "Lunch", "Pizza", 2500),
    ("S015", "Oscar", "Thursday", "Lunch", "Burger", 2000),
    ("S016", "Priscilla", "Thursday", "Lunch", "Beans and Matooke", 1500),
    ("S017", "Quinn", "Thursday", "Lunch", "Chapati and Beans", 1800),
    ("S018", "Rebecca", "Thursday", "Lunch", "Soda", 1000),
    ("S029", "Carol", "Thursday", "Lunch", "Pilau", 3500),
    ("S030", "Daniel", "Thursday", "Lunch", "Chicken and Rice", 3500),

    # FRIDAY TRANSACTIONS
    ("S019", "Samuel", "Friday", "Lunch", "Chips and Sausage", 3000),
    ("S020", "Tracy", "Friday", "Lunch", "Pizza", 2500),
    ("S021", "Umar", "Friday", "Lunch", "Juice", 1500),
    ("S022", "Victoria", "Friday", "Lunch", "Fish and Chips", 4000),
    ("S023", "William", "Friday", "Lunch", "Rolex", 2500),
    ("S024", "Xavier", "Friday", "Lunch", "Chicken and Rice", 3500),
    ("S025", "Yvonne", "Friday", "Lunch", "Pasta", 2200),
    ("S026", "Zachary", "Friday", "Lunch", "Burger", 2000),

    # STUDENT FRANK - MULTIPLE MEALS IN ONE DAY (Breakfast, Lunch, Supper)
    ("S031", "Frank", "Monday", "Breakfast", "Tea and Bread", 1000),
    ("S031", "Frank", "Monday", "Lunch", "Beans and Matooke", 1500),
    ("S031", "Frank", "Monday", "Supper", "Chapati and Beans", 1800),
    ("S031", "Frank", "Tuesday", "Breakfast", "Tea and Bread", 1000),
    ("S031", "Frank", "Tuesday", "Lunch", "Pilau", 3500),

    # STUDENT HELEN - MULTIPLE MEALS IN ONE DAY
    ("S032", "Helen", "Monday", "Breakfast", "Juice and Cake", 1500),
    ("S032", "Helen", "Monday", "Lunch", "Pizza", 2500),
    ("S032", "Helen", "Monday", "Supper", "Burger", 2000),
    ("S032", "Helen", "Tuesday", "Lunch", "Fish and Chips", 4000),
    ("S032", "Helen", "Wednesday", "Lunch", "Chicken and Rice", 3500),

    # STUDENT IRENE - MULTIPLE MEALS ACROSS THE WEEK
    ("S033", "Irene", "Monday", "Breakfast", "Tea and Bread", 1000),
    ("S033", "Irene", "Monday", "Lunch", "Rolex", 2500),
    ("S033", "Irene", "Tuesday", "Breakfast", "Tea and Bread", 1000),
    ("S033", "Irene", "Tuesday", "Lunch", "Chips and Sausage", 3000),
    ("S033", "Irene", "Wednesday", "Lunch", "Pasta", 2200),
    ("S033", "Irene", "Thursday", "Lunch", "Soda", 1000),

    # STUDENT JAMES - BUYS EVERY DAY (5 transactions)
    ("S034", "James", "Monday", "Lunch", "Pizza", 2500),
    ("S034", "James", "Tuesday", "Lunch", "Burger", 2000),
    ("S034", "James", "Wednesday", "Lunch", "Pasta", 2200),
    ("S034", "James", "Thursday", "Lunch", "Chicken and Rice", 3500),
    ("S034", "James", "Friday", "Lunch", "Fish and Chips", 4000),

    # STUDENT LINDA - BUYS EVERY DAY (5 transactions)
    ("S035", "Linda", "Monday", "Lunch", "Rolex", 2500),
    ("S035", "Linda", "Tuesday", "Lunch", "Chips and Sausage", 3000),
    ("S035", "Linda", "Wednesday", "Lunch", "Chapati and Beans", 1800),
    ("S035", "Linda", "Thursday", "Lunch", "Beans and Matooke", 1500),
    ("S035", "Linda", "Friday", "Lunch", "Pilau", 3500),

    # EDGE CASE 1: HIGH SPENDER - ROBERT (7 transactions in one week)
    ("S036", "Robert", "Monday", "Lunch", "Fish and Chips", 4000),
    ("S036", "Robert", "Monday", "Supper", "Fish and Chips", 4000),
    ("S036", "Robert", "Tuesday", "Lunch", "Pizza", 2500),
    ("S036", "Robert", "Wednesday", "Lunch", "Burger", 2000),
    ("S036", "Robert", "Thursday", "Lunch", "Chicken and Rice", 3500),
    ("S036", "Robert", "Friday", "Lunch", "Pilau", 3500),
    ("S036", "Robert", "Friday", "Supper", "Rolex", 2500),

    # EDGE CASE 2: LOW SPENDER - SUSAN (only 2 cheap meals)
    ("S037", "Susan", "Monday", "Lunch", "Soda", 1000),
    ("S037", "Susan", "Wednesday", "Lunch", "Soda", 1000)
]

# Initialize three empty dictionaries to store our calculated results
# student_weekly_spending: Stores each student's total spending for the week
student_weekly_spending = {}

# meal_revenue: Stores each meal type's total revenue for the week
meal_revenue = {}

# meal_student_count: Stores a list of unique students who ate each meal type
meal_student_count = {}

# Main processing loop - goes through every transaction in meal_data
# The tuple unpacking assigns each field to a meaningful variable name
for student_id, student_name, day, time_slot, meal_type, price in meal_data:
    
    # TASK 3: Calculate how much each student spends during the week
    # Check if student already exists in the spending dictionary
    if student_name not in student_weekly_spending:
        # If this is the first transaction for this student, add them with this price
        student_weekly_spending[student_name] = price
    else:
        # If student already exists, add this transaction's price to their total
        student_weekly_spending[student_name] += price
    
    # TASK 5: Calculate total weekly revenue generated by each meal type
    # Check if meal type already exists in the revenue dictionary
    if meal_type not in meal_revenue:
        # If this is the first transaction for this meal, add it with this price
        meal_revenue[meal_type] = price
    else:
        # If meal already exists, add this transaction's price to its total
        meal_revenue[meal_type] += price
    
    # TASK 2: Group students according to their meal preference
    # Check if meal type already exists in the student count dictionary
    if meal_type not in meal_student_count:
        # If this is the first time seeing this meal, create a list with this student
        meal_student_count[meal_type] = [student_name]
    else:
        # If meal already exists, check if this student is already in the list
        if student_name not in meal_student_count[meal_type]:
            # If student is not already in the list, add them
            # This prevents duplicate entries for students who ate the same meal multiple times
            meal_student_count[meal_type].append(student_name)

# FUNCTION TO GENERATE THE COMPLETE CAFETERIA REPORT
# This function takes the three dictionaries as parameters and prints a formatted report
def generate_cafeteria_report(student_spending, meal_revenue, meal_student_count):
    
    # Print the report header with decorative borders
    print("=" * 60)
    print("           SCHOOL CAFETERIA WEEKLY REPORT")
    print("=" * 60)
    
    # TASK 2: Display meal groups showing which students prefer each meal
    print("\n--- MEAL GROUPS (Students by Preference) ---")
    for meal, students in meal_student_count.items():
        # Join the list of students into a comma-separated string for clean display
        print(f"{meal}: {', '.join(students)}")
    
    # TASK 3: Display weekly spending for each student
    # Sort students by spending amount from highest to lowest using sorted() with lambda
    print("\n--- STUDENT WEEKLY SPENDING ---")
    for name, total in sorted(student_spending.items(), key=lambda x: x[1], reverse=True):
        # The :, format specifier adds commas to large numbers for readability
        print(f"{name}: {total:,} UGX")
    
    # TASK 4: Identify and display students who spend more than 15,000 UGX per week
    print("\n--- HIGH SPENDERS (> 15,000 UGX) ---")
    # Initialize an empty dictionary to store high spenders
    high_spenders = {}
    # Loop through each student in the spending dictionary
    for name, total in student_spending.items():
        # Check if their total spending exceeds 15,000 UGX
        if total > 15000:
            # Add them to the high spenders dictionary
            high_spenders[name] = total
    
    # If there are high spenders, display them with a warning symbol
    if high_spenders:
        # Sort high spenders from highest to lowest
        for name, total in sorted(high_spenders.items(), key=lambda x: x[1], reverse=True):
            print(f"WARNING: {name}: {total:,} UGX (EXCEEDS LIMIT)")
    else:
        # If no high spenders found, display this message
        print("No students exceeded the 15,000 UGX threshold.")
    
    # TASK 5: Display total weekly revenue generated by each meal type
    # Sort meals by revenue from highest to lowest
    print("\n--- WEEKLY REVENUE BY MEAL TYPE ---")
    for meal, total in sorted(meal_revenue.items(), key=lambda x: x[1], reverse=True):
        print(f"{meal}: {total:,} UGX")
    
    # TASK 6: Determine and display the most popular meal
    print("\n--- MOST POPULAR MEAL ---")
    # Find the meal with the most students using max() with a lambda key
    # len(x[1]) gets the length of the student list for each meal
    most_popular = max(meal_student_count.items(), key=lambda x: len(x[1]))
    print(f"MOST POPULAR: {most_popular[0]} with {len(most_popular[1])} students")
    print(f"   Students: {', '.join(most_popular[1])}")
    
    # Print the report footer
    print("\n" + "=" * 60)
    print("             END OF REPORT")
    print("=" * 60)

# Call the function to generate and display the report
# Pass the three dictionaries containing all the processed data
generate_cafeteria_report(student_weekly_spending, meal_revenue, meal_student_count)