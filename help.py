import json

# Load your original JSON file
with open('restaurants.json', 'r') as f:
    lines = f.readlines()

# Add commas between objects and wrap in a list
json_data = "[" + ",".join([line.strip() for line in lines]) + "]"

# Try to load and pretty-print to check validity
try:
    parsed_data = json.loads(json_data)
    with open('restaurants_fixed.json', 'w') as f_out:
        json.dump(parsed_data, f_out, indent=4)
    print("Fixed JSON saved to 'restaurants_fixed.json'")
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
