# QUESTION 4: CLINIC PATIENT STATUS CLASSIFICATION SYSTEM

# Supplied dataset
patients = [
    ("Alice", 115, 75),
    ("Brian", 128, 84),
    ("Carol", 145, 95),
    ("Daniel", 165, 105),
    ("Grace", 118, 78)
]

# Additional test dataset with edge cases
patients_test = [
    ("Alice", 115, 75),
    ("Brian", 128, 84),
    ("Carol", 145, 95),
    ("Daniel", 165, 105),
    ("Grace", 118, 78),
    ("Henry", 90, 60),
    ("Ivy", 135, 85),
    ("John", 155, 92),
    ("Kevin", 170, 110),
    ("Linda", 110, 70),
    ("Mike", 125, 82),
    ("Nancy", 140, 88),
    ("Oscar", 160, 95),
    ("Peter", 180, 120),
    ("Quinn", 95, 65),
    ("Rose", 130, 80),
    ("Steve", 150, 90),
    ("Tina", 175, 115),
    ("Umar", 105, 72),
    ("Victor", 138, 86)
]

def classify_patient(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic >= 160 or diastolic >= 100:
        return "Urgent"
    elif 140 <= systolic <= 159 or 90 <= diastolic <= 99:
        return "Stage 1"
    elif 120 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "Elevated"
    else:
        return "Normal"

def process_patients(patient_data):
    normal_patients = []
    at_risk_patients = []
    urgent_patients = []
    systolic_sum = 0
    diastolic_sum = 0
    patient_count = 0
    
    for patient_name, systolic, diastolic in patient_data:
        patient_count += 1
        systolic_sum += systolic
        diastolic_sum += diastolic
        
        category = classify_patient(systolic, diastolic)
        
        if category == "Normal":
            normal_patients.append((patient_name, systolic, diastolic))
        elif category == "Urgent":
            urgent_patients.append((patient_name, systolic, diastolic))
        else:
            at_risk_patients.append((patient_name, systolic, diastolic, category))
    
    average_systolic = systolic_sum / patient_count
    average_diastolic = diastolic_sum / patient_count
    
    generate_clinic_report(normal_patients, at_risk_patients, urgent_patients, average_systolic, average_diastolic, patient_data)

def generate_clinic_report(normal_patients, at_risk_patients, urgent_patients, average_systolic, average_diastolic, patient_data):
    print("=" * 70)
    print("                 CLINIC PATIENT STATUS REPORT")
    print("=" * 70)
    
    print("\n--- PATIENT CATEGORIZATION ---")
    print("\nNORMAL PATIENTS:")
    if normal_patients:
        for name, systolic, diastolic in normal_patients:
            print(f"  {name}: Systolic {systolic}, Diastolic {diastolic}")
    else:
        print("  None")
    
    print("\nAT-RISK PATIENTS (Elevated or Stage 1):")
    if at_risk_patients:
        for name, systolic, diastolic, category in at_risk_patients:
            print(f"  {name}: {category} - Systolic {systolic}, Diastolic {diastolic}")
    else:
        print("  None")
    
    print("\nURGENT PATIENTS:")
    if urgent_patients:
        for name, systolic, diastolic in urgent_patients:
            print(f"  URGENT: {name} - Systolic {systolic}, Diastolic {diastolic}")
    else:
        print("  None")
    
    print("\n--- AVERAGE READINGS ---")
    print(f"Average Systolic: {average_systolic:.1f}")
    print(f"Average Diastolic: {average_diastolic:.1f}")
    
    print("\n--- URGENT PATIENT ALERTS ---")
    if urgent_patients:
        for name, systolic, diastolic in urgent_patients:
            print(f"ALERT: {name} requires immediate medical attention!")
            print(f"  Systolic: {systolic}, Diastolic: {diastolic}")
    else:
        print("No urgent patients detected.")
    
    print("\n--- PATIENTS REQUIRING FOLLOW-UP ---")
    follow_up_patients = []
    for name, systolic, diastolic in patient_data:
        category = classify_patient(systolic, diastolic)
        if category != "Normal":
            follow_up_patients.append((name, category))
    
    if follow_up_patients:
        for name, category in follow_up_patients:
            print(f"{name}: {category} - Follow-up required")
    else:
        print("No patients require follow-up.")
    
    print("\n--- SUMMARY STATISTICS ---")
    print(f"Total Patients: {len(patient_data)}")
    print(f"Normal: {len(normal_patients)}")
    print(f"At-Risk: {len(at_risk_patients)}")
    print(f"Urgent: {len(urgent_patients)}")
    
    print("\n" + "=" * 70)
    print("                    END OF REPORT")
    print("=" * 70)

print("\n" + "=" * 70)
print("          RUNNING WITH SUPPLIED DATASET")
print("=" * 70)
process_patients(patients)

print("\n\n" + "=" * 70)
print("          RUNNING WITH ADDITIONAL TEST DATASET")
print("=" * 70)
process_patients(patients_test)