# main.py
import json

# Step 1: Define a dictionary
data = {
    "name": "Israel Kolawole",
    "age": 30,
    "profession": "Teacher",
    "skills": ["Python", "Physics", "AI"],
    "country": "Nigeria"
}

# Step 2: Convert dictionary to JSON string
json_data = json.dumps(data, indent=4)

# Step 3: Save JSON data to a file
with open("sample_data.json", "w") as file:
    file.write(json_data)

# Step 4: Read back the file and print the content
with open("sample_data.json", "r") as file:
    loaded_data = json.load(file)

print("✅ JSON file created successfully!")
print("📄 Loaded Data:")

print("="*30)
same_content = json.dumps(loaded_data, indent=4)
print(same_content)
print("="*30)