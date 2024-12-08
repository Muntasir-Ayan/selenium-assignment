import os

# Define the directory structure
structure = {
    "vacation_rental_testing": {
        "main.py": "",
        "config": {
            "settings.py": "",
            "test_data.py": ""
        },
        "utils": {
            "browser_setup.py": "",
            "excel_report.py": "",
            "helper.py": ""
        },
        "tests": {
            "base_test.py": "",
            "h1_test.py": "",
            "image_alt_test.py": "",
            "url_status_test.py": "",
            "currency_filter_test.py": "",
            "script_data_test.py": ""
        },
        "reports": {
            "test_results.xlsx": ""
        }
    }
}

# Function to create the directory structure
def create_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            # Create the directory
            os.makedirs(path, exist_ok=True)
            # Recursively create subdirectories/files
            create_structure(path, value)
        else:
            # Create the file
            with open(path, 'w') as f:
                f.write(value)

# Create the folder structure
base_path = "."  # You can specify the directory where you want to create the structure
create_structure(base_path, structure)

print("Folder structure created successfully!")
