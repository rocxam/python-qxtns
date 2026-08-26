# QUESTION 2: COMMUNITY LIBRARY BOOK DONATION MANAGER

# Supplied dataset
donations = [
    ("Alice", "Fiction", 3),
    ("Brian", "Technology", 6),
    ("Carol", "History", 2),
    ("Alice", "Technology", 3),
    ("Daniel", "Fiction", 7),
    ("Grace", "Science", 5)
]

# Additional test dataset with edge cases
donations_test = [
    ("Alice", "Fiction", 3),
    ("Brian", "Technology", 6),
    ("Carol", "History", 2),
    ("Alice", "Technology", 3),
    ("Daniel", "Fiction", 7),
    ("Grace", "Science", 5),
    ("Eve", "Fiction", 10),
    ("Frank", "History", 1),
    ("Grace", "History", 4),
    ("Henry", "Technology", 8),
    ("Ivy", "Science", 2),
    ("John", "Fiction", 5),
    ("Kevin", "Technology", 5),
    ("Linda", "Science", 6),
    ("Mike", "History", 3),
    ("Nancy", "Fiction", 4),
    ("Oscar", "Technology", 2),
    ("Peter", "Science", 1),
    ("Quinn", "History", 9),
    ("Rose", "Fiction", 2),
    ("Steve", "Technology", 7),
    ("Tina", "Science", 8),
    ("Umar", "History", 5),
    ("Victor", "Fiction", 6),
    ("Wendy", "Technology", 4),
    ("Xavier", "Science", 3),
    ("Yvonne", "History", 7),
    ("Zachary", "Fiction", 8),
    ("Amos", "Technology", 3),
    ("Betty", "Science", 9),
    ("Charles", "History", 2),
    ("Diana", "Fiction", 5),
    ("Emmanuel", "Technology", 6),
    ("Faith", "Science", 4),
    ("George", "History", 8),
    ("Hannah", "Fiction", 1),
    ("Isaac", "Technology", 9),
    ("Jessica", "Science", 2),
    ("Kevin", "History", 6),
    ("Linda", "Fiction", 7),
    ("Moses", "Technology", 1),
    ("Naomi", "Science", 5),
    ("Oscar", "History", 4),
    ("Peter", "Fiction", 9),
    ("Quinn", "Technology", 2),
    ("Rose", "Science", 7),
    ("Steve", "History", 3),
    ("Tina", "Fiction", 6),
    ("Umar", "Technology", 5),
    ("Victor", "Science", 8)
]

def process_donations(donation_data):
    donor_total = {}
    genre_total = {}
    genre_donor_count = {}
    overall_total = 0
    
    for donor_name, genre, number_of_books in donation_data:
        if donor_name not in donor_total:
            donor_total[donor_name] = number_of_books
        else:
            donor_total[donor_name] += number_of_books
        
        if genre not in genre_total:
            genre_total[genre] = number_of_books
        else:
            genre_total[genre] += number_of_books
        
        if genre not in genre_donor_count:
            genre_donor_count[genre] = [donor_name]
        else:
            if donor_name not in genre_donor_count[genre]:
                genre_donor_count[genre].append(donor_name)
        
        overall_total += number_of_books
    
    gold_donors = {}
    for donor, total in donor_total.items():
        if total >= 5:
            gold_donors[donor] = total
    
    sorted_donors = sorted(donor_total.items(), key=lambda x: x[1], reverse=True)
    top_3_donors = sorted_donors[:3]
    
    most_popular_genre = max(genre_total.items(), key=lambda x: x[1])
    
    generate_donation_report(donor_total, genre_total, gold_donors, overall_total, most_popular_genre, top_3_donors, genre_donor_count)

def generate_donation_report(donor_total, genre_total, gold_donors, overall_total, most_popular_genre, top_3_donors, genre_donor_count):
    print("=" * 70)
    print("              COMMUNITY LIBRARY DONATION REPORT")
    print("=" * 70)
    
    print("\n--- TOTAL BOOKS DONATED BY EACH DONOR ---")
    for donor, total in sorted(donor_total.items(), key=lambda x: x[1], reverse=True):
        print(f"{donor}: {total} books")
    
    print("\n--- GOLD DONORS (5 or more books) ---")
    if gold_donors:
        for donor, total in sorted(gold_donors.items(), key=lambda x: x[1], reverse=True):
            print(f"GOLD: {donor} - {total} books")
    else:
        print("No gold donors found.")
    
    print("\n--- OVERALL NUMBER OF BOOKS DONATED ---")
    print(f"Total books donated: {overall_total}")
    
    print("\n--- BOOKS RECEIVED PER GENRE ---")
    for genre, total in sorted(genre_total.items(), key=lambda x: x[1], reverse=True):
        print(f"{genre}: {total} books")
    
    print("\n--- MOST POPULAR GENRE ---")
    print(f"MOST POPULAR: {most_popular_genre[0]} with {most_popular_genre[1]} books")
    
    print("\n--- TOP 3 DONORS ---")
    for i, (donor, total) in enumerate(top_3_donors, 1):
        print(f"#{i}: {donor} with {total} books")
    
    print("\n--- DONORS PER GENRE ---")
    for genre, donors in genre_donor_count.items():
        print(f"{genre}: {', '.join(donors)}")
    
    print("\n" + "=" * 70)
    print("                    END OF REPORT")
    print("=" * 70)

print("\n" + "=" * 70)
print("          RUNNING WITH SUPPLIED DATASET")
print("=" * 70)
process_donations(donations)

print("\n\n" + "=" * 70)
print("          RUNNING WITH ADDITIONAL TEST DATASET")
print("=" * 70)
process_donations(donations_test)