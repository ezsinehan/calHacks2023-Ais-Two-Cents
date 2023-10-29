import openai
import json

openai.api_key = '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'

# Read the dataset from the JSON file
with open('/Users/sinehanezhilmuthu/Desktop/csShit/stev2/backend/gettingData/parsingPredictions/parsed_data.json', 'r') as file:
    dataset = json.load(file)

# Convert the dataset to a string
dataset_str = json.dumps(dataset)

# Create a GPT-3 prompt to generate recommendations based on the dataset
prompt = f"Based on the provided dataset:\n{dataset_str}\n\nPlease provide specific recommendations to the speaker on how to increase positive emotions like interest and reduce negative emotions like confusion."

# Generate a response from GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=500
)

# Extract the generated recommendations from the response
recommendations = response.choices[0].text

# Print or use the recommendations as needed
print(recommendations)
