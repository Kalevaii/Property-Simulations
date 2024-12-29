# Property-Simulations
 Property Management System - GitHub Project Description 🏠 Property Management System The Property Management System is a Python-based application designed to simplify property management and recommendation tasks for real estate administrators and users
It uses JSON files for data storage, making it lightweight and easy to set up without requiring a database.

🚀 Features
Admin Features:

Add new properties with details like name, location, price, size, and type (House/Apartment).
Remove properties using their unique ID.
View all listed properties in a neatly formatted display.
Password-protected admin menu for secure property management.
User Features:

View all available properties.
Search for properties within a specified price range.
Save favorite properties for future reference.
View saved properties by user.
Recommendations:

Get property recommendations based on a price range.
File-Based Storage:

All property data is stored in a property.json file.
User-saved properties are managed using user_saved_properties.json.
Robust Input Validation:

Ensures correct data types for price, size, and other inputs.
Handles missing files gracefully by initializing with default values.
📂 File Structure
property.py: The main program file containing all the core functionalities.
property.json: Stores property data in JSON format.
user_saved_properties.json: Stores user-saved properties in JSON format.
🛠️ How to Use
Clone the repository to your local machine.
Run the property.py file in a Python environment.
Use the admin menu for property management or explore user functionalities for property recommendations and saving preferences.
