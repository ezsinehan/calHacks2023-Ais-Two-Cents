import json

# Load the emotions data from specificPredictions.json
with open("specificPredictions.json", "r") as emotions_file:
    emotions_data = json.load(emotions_file)

# Load the transcriptions data from text.json
with open("../../uploads/text.json", "r") as transcriptions_file:
    transcriptions_data = json.load(transcriptions_file)

# Create a dictionary for transcriptions for faster lookup
transcriptions_dict = {entry["Second-Start"]: entry["Transcription"] for entry in transcriptions_data.values()}

# Merge the emotions and transcriptions data
merged_data = []

for emotion_entry in emotions_data:
    second = emotion_entry["second"]
    transcription = transcriptions_dict.get(second, "")  # Use an empty string if no transcription is found
    merged_entry = {
        "second": second,
        "top_emotions": emotion_entry["averaged_emotions"]["average_emotions"],
        "transcription": transcription
    }
    merged_data.append(merged_entry)

# Save the merged data to a new JSON file
with open("merged_data.json", "w") as output_file:
    json.dump(merged_data, output_file, indent=4)

print("Merged data saved to merged_data.json")
