import json
import openai

# Load data from "parsed_data.json"
with open("../gettingData/parsingPredictions/parsed_data.json", "r") as json_file:
    data = json.load(json_file)

# Extract text transcriptions from the JSON data
text_transcriptions = [entry["transcription"] for entry in data if entry["transcription"]]

# Create a prompt by joining the text transcriptions
prompt = "\n".join(text_transcriptions)

# Define your OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Make a request to the GPT API
response = openai.Completion.create(
    engine="text-davinci-002",  # Choose an appropriate engine
    prompt=prompt,
    max_tokens=100,  # Adjust this as needed
    temperature=0.7,  # Adjust the temperature for creativity
)

# Extract the generated text from the API response
generated_text = response.choices[0].text

# Process the generated text as needed
print(generated_text)
