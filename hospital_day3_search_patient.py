# Hospital System - Day 3
# Added search functionality
# Author: Ezekiel Kang'ombe

patients = []


def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    condition = input("Enter condition: ")

    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "condition": condition
    }

    patients.append(patient)
    print("Patient added successfully.")


def view_patients():
    if len(patients) == 0:
        print("No patients found.")
    else:
        print("\n--- Patient List ---")
        
        for index, patient in enumerate(patients, start=1):
            print(f"\nPatient {index}:")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Condition:", patient["condition"])


def search_patient():
    search_name = input("Enter patient name to search: ")

    found = False

    for patient in patients:
        if patient["name"].lower() == search_name.lower():
            print("\nPatient Found:")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Condition:", patient["condition"])
            found = True

    if not found:
        print("Patient not found.")


while True:
    print("\n--- Hospital System ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")
