import json

# Load the merged data
with open('merged_data.json', 'r') as merged_file:
    merged_data = json.load(merged_file)

# Create a new list to store the parsed data
parsed_data = []

# Function to get the top three emotions closest to 1
def get_top_three_emotions(emotions):
    sorted_emotions = sorted(emotions.items(), key=lambda x: abs(1 - x[1]))
    return dict(sorted_emotions[:3])

# Iterate through the merged data and extract the required information
for entry in merged_data:
    parsed_entry = {
        "second": entry["second"],
        "transcription": entry["transcription"],
        "top_emotions": get_top_three_emotions(entry["top_emotions"])
    }
    parsed_data.append(parsed_entry)

# Save the parsed data to a new JSON file
with open("parsed_data.json", "w") as output_file:
    json.dump(parsed_data, output_file, indent=4)

print("Parsed data saved to parsed_data.json")