import json

# Constants
ADMIN_PASSWORD = "password"
PROPERTY_FILE = "property.json"
USER_SAVED_PROPERTIES_FILE = "user_saved_properties.json"

# Load property data from a JSON file
def load_properties():
    try:
        with open(PROPERTY_FILE, 'r') as file:
            data = json.load(file)
            return data.get("property", {})  # Return an empty dict if "property" key doesn't exist
    except FileNotFoundError:
        print("Property file not found. Initializing with an empty property list.")
        return {}

# Save properties to a JSON file
def save_properties(properties):
    with open(PROPERTY_FILE, 'w') as file:
        json.dump({"property": properties}, file, indent=4)

# Display all available properties
def display_properties(properties):
    if properties:
        print("\nAvailable Properties:")
        for property_id, property_info in properties.items():
            print(f"ID: {property_id}, {property_info['name']} in {property_info['location']}, "
                  f"Price: ${property_info['price']}, Type: {property_info['type']}, "
                  f"Size: {property_info['size']} sqft")
    else:
        print("No properties to display.")

# Recommend properties based on a price range
def recommend_property(properties, min_price, max_price):
    recommendations = []
    for property_info in properties.values():
        if min_price <= property_info["price"] <= max_price:
            recommendations.append(property_info)
    return recommendations

# Admin menu for managing properties
# Verify the admin password
def check_pw():
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        print("Access granted.")
        return True
    else:
        print("Access denied. Incorrect password.")
        return False
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New Property")
        print("2. Remove Property")
        print("3. View All Properties")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_property()
        elif choice == "2":
            remove_property()
        elif choice == "3":
            view_properties()
        elif choice == "4":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Exiting admin menu.")
                break
        else:
            print("Invalid choice, please try again.")

# Add a new property
def add_property():
    name = input("Enter property name: ")
    location = input("Enter property location: ")
    try:
        price = float(input("Enter property price: "))
        size = int(input("Enter property size (in sqft): "))
    except ValueError:
        print("Invalid input for price or size. Please try again.")
        return

    property_type = input("Enter property type (House/Apartment): ")

    new_property = {
        "name": name,
        "location": location,
        "price": price,
        "size": size,
        "type": property_type
    }

    # Load existing properties and add the new property
    properties = load_properties()
    properties[str(len(properties) + 1)] = new_property

    # Save updated properties back to the file
    save_properties(properties)

    print("New property added successfully.")

# Remove a property
def remove_property():
    property_id = input("Enter the property ID to remove: ")

    properties = load_properties()

    if property_id in properties:
        del properties[property_id]
        save_properties(properties)
        print("Property removed successfully.")
    else:
        print("Property ID not found.")

# View all properties
def view_properties():
    properties = load_properties()
    if properties:
        display_properties(properties)
    else:
        print("No properties to display.")

# Save a property for a user
def save_property(user_name):
    properties = load_properties()
    display_properties(properties)
    
    property_name = input("\nEnter the name of the property you want to save: ")
    
    if property_name in [prop['name'] for prop in properties.values()]:
        # Load or create user_saved_properties
        user_saved_properties = load_user_saved_properties()
        
        if user_name not in user_saved_properties:
            user_saved_properties[user_name] = []
        
        user_saved_properties[user_name].append(property_name)
        
        # Save the updated user saved properties
        save_user_saved_properties(user_saved_properties)
        
        print(f"\n'{property_name}' has been saved for {user_name}!")
    else:
        print("\nInvalid property name. Please try again.")

# View saved properties for a user
def view_saved_properties(user_name):
    user_saved_properties = load_user_saved_properties()

    if user_name in user_saved_properties and user_saved_properties[user_name]:
        print(f"\n{user_name}'s Saved Properties:")
        for saved_property in user_saved_properties[user_name]:
            print(f"- {saved_property}")
    else:
        print(f"\nNo properties saved for {user_name}.")

# Load user saved properties from a file
def load_user_saved_properties():
    try:
        with open(USER_SAVED_PROPERTIES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user saved properties to a file
def save_user_saved_properties(user_saved_properties):
    with open(USER_SAVED_PROPERTIES_FILE, 'w') as file:
        json.dump(user_saved_properties, file, indent=4)

# Search properties by price range
def search_properties_by_price(properties, min_price, max_price):
    print(f"\nProperties in the price range ${min_price} - ${max_price}:")
    found = False
    for property_id, property_info in properties.items():
        if min_price <= property_info["price"] <= max_price:
            print(f"ID: {property_id}, {property_info['name']} in {property_info['location']}, "
                  f"Price: ${property_info['price']}, Type: {property_info['type']}, "
                  f"Size: {property_info['size']} sqft")
            found = True
    if not found:
        print("No properties found in this price range.") 
