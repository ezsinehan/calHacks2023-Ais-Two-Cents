import json

# Read the input JSON data
with open('../predictions.json', 'r') as input_file:
    input_data = json.load(input_file)

# Initialize data structure to store averages
averages = {}

# Iterate through predictions in the input data
for prediction in input_data[0]['results']['predictions']:
    file_type = prediction['file_type']

    # Check if the file type is "video_no_audio"
    if file_type == "video_no_audio":
        emotions = prediction['models']['face']['grouped_predictions'][0]['predictions']

        # Iterate through emotions
        for emotion_data in emotions:
            frame = emotion_data['frame']
            time = emotion_data['time']
            emotions = emotion_data['emotions']

            # Calculate the second
            second = int(time)

            # Initialize a dictionary for the second if not exists
            if second not in averages:
                averages[second] = {
                    "frame_count": 0,
                    "average_emotions": {}
                }

            # Update the frame count for the second
            averages[second]["frame_count"] += 1

            # Update the emotion scores for the second
            for emotion in emotions:
                name = emotion['name']
                score = emotion['score']

                if name in averages[second]["average_emotions"]:
                    averages[second]["average_emotions"][name].append(score)
                else:
                    averages[second]["average_emotions"][name] = [score]

# Calculate the averages for each emotion
for second_data in averages.values():
    for emotion_name, emotion_scores in second_data["average_emotions"].items():
        average_score = sum(emotion_scores) / len(emotion_scores)
        second_data["average_emotions"][emotion_name] = average_score

# Create the output JSON structure
output_data = [
    {
        "second": second,
        "averaged_emotions": {
            "average_emotions": data["average_emotions"]
        }
    }
    for second, data in averages.items()
]

# Write the output JSON to a file
with open('specificPredictions.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print("Output JSON file created.")
