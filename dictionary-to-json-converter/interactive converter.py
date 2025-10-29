import json
from datetime import datetime

# Step 1: Get user input
print(" Welcome to the Dictionary → JSON Converter!")
print("Let's create your custom data file.\n")

data = {}

# Step 2: Loop to collect key-value pairs
while True:
    key = input("Enter key (or 'done' to finish): ")
    if key.lower() == "done":
        break
    value = input(f"Enter value for '{key}': ")
    data[key] = value

# Step 3: Add timestamp
data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Step 4: Convert dictionary to JSON and save
json_data = json.dumps(data, indent=4, sort_keys=True)
filename = "user_data.json"

with open(filename, "w") as file:
    file.write(json_data)

# Step 5: Display saved data
print("\n JSON file created successfully!")
print(" Here's what it looks like:")
print(json_data)

