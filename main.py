from classroom_organizer import ClassroomOrganizer  

def main():
    organizer = ClassroomOrganizer()

    while True:
        print("\nMenu:")
        print("1. View sorted student names")
        print("2. Get students with a specific subject")
        print("3. View all possible student pairs")
        print("4. Get possible combinations of Math and Science students")
        print("5. Add a new student")
        print("6. Remove a student")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("\nSorted Student Names:")
            for name in organizer.sorted_names:
                print(name)

        elif choice == '2':
            subject = input("Enter the subject (e.g., Math, Science): ")
            students = organizer.get_students_with_subject(subject)
            print(f"\nStudents who like {subject}:")
            for name, subj in students:
                print(f"{name} - {subj}")

        elif choice == '3':
            print("\nPossible Student Pairs:")
            pairs = organizer.student_pairs()
            for pair in pairs:
                print(pair)

        elif choice == '4':
            combos = organizer.mns_students_combo(organizer)
            print("\nPossible combinations of Math and Science students:")
            for combo in combos:
                print(combo)

        elif choice == '5':
            name = input("Enter the student's name: ")
            age = int(input("Enter the student's age: "))
            height = int(input("Enter the student's height (in cm): "))
            favorite_subject = input("Enter the student's favorite subject: ")
            favorite_animal = input("Enter the student's favorite animal: ")
            organizer.add_student(name, age, height, favorite_subject, favorite_animal)
            print(f"Student {name} added successfully!")

        elif choice == '6':
            name = input("Enter the name of the student to remove: ")
            result = organizer.remove_student(name)
            print(result)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
