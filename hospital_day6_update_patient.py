# Hospital System - Day 6

patients = []


def add_patient():
    # Name validation
    while True:
        name = input("Enter patient name: ")
        if name.strip() == "":
            print("Name cannot be empty.")
        else:
            break

    # Age validation
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Gender validation
    while True:
        gender = input("Enter gender (male/female): ").lower()
        if gender == "male" or gender == "female":
            break
        else:
            print("Invalid gender. Enter 'male' or 'female'.")

    # Condition (basic input for now)
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


def delete_patient():
    if len(patients) == 0:
        print("No patients to delete.")
        return

    view_patients()

    try:
        choice = int(input("Enter patient number to delete: "))

        if 1 <= choice <= len(patients):
            removed = patients.pop(choice - 1)
            print(f"Patient '{removed['name']}' deleted successfully.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")
        
def update_patient():
    if len(patients) == 0:
        print("No patients to update.")
        return

    view_patients()

    try:
        choice = int(input("Enter patient number to update: "))

        if 1 <= choice <= len(patients):
            patient = patients[choice - 1]

            print("\nLeave blank to keep current value.")

            # Name
            new_name = input(f"Enter new name ({patient['name']}): ")
            if new_name.strip() != "":
                patient["name"] = new_name

            # Age
            while True:
                new_age = input(f"Enter new age ({patient['age']}): ")
                if new_age == "":
                    break
                try:
                    new_age = int(new_age)
                    if new_age > 0:
                        patient["age"] = new_age
                        break
                    else:
                        print("Age must be greater than 0.")
                except ValueError:
                    print("Enter a valid number.")

            # Gender
            while True:
                new_gender = input(f"Enter new gender ({patient['gender']}): ").lower()
                if new_gender == "":
                    break
                if new_gender in ["male", "female"]:
                    patient["gender"] = new_gender
                    break
                else:
                    print("Invalid gender.")

            # Condition
            new_condition = input(f"Enter new condition ({patient['condition']}): ")
            if new_condition.strip() != "":
                patient["condition"] = new_condition

            print("Patient updated successfully.")

        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")

while True:
     print("\n--- Hospital System ---")
     print("1. Add Patient")
     print("2. View Patients")
     print("3. Search Patient")
     print("4. Delete Patient")
     print("5. Update Patient")
     print("6. Exit")
    
     choice = input("Enter choice: ")

     if choice == "1":
        add_patient()
     elif choice == "2":
        view_patients()
     elif choice == "3":
        search_patient()
     elif choice == "4":
        delete_patient()
     elif choice == "5":
        update_patient()
     elif choice == "6":
        print("Exiting system...")
        break
     else:
        print("Invalid choice")
