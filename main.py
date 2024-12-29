import property

def main():
    user_name = input("Please enter your name: ").strip()

    while True:
        # Display the main menu
        print("\nMain Menu:")
        print("1. View All Properties")
        print("2. Search Properties by Price Range")
        print("3. Save a Property")
        print("4. View Saved Properties")
        print("5. Admin Menu")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            properties = property.load_properties()
            property.display_properties(properties)

        elif choice == "2":
            try:
                min_price = float(input("Enter minimum price: "))
                max_price = float(input("Enter maximum price: "))
                properties = property.load_properties()
                property.search_properties_by_price(properties, min_price, max_price)
            except ValueError:
                print("Invalid input! Please enter numeric values for price.")

        elif choice == "3":
            properties = property.load_properties()
            property.save_property(user_name)

        elif choice == "4":
            property.view_saved_properties(user_name)

        elif choice == "5":
            if property.check_pw():
                property.admin_menu()

        elif choice == "6":
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm_exit == "yes":
                print("Thank you for using the Property Management System. Goodbye!")
                break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
