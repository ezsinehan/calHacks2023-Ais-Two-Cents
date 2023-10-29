from hume import HumeBatchClient
from hume.models.config import FaceConfig
import json

client = HumeBatchClient("skiGzxJnlS86cGiGHNtAGrYbABaQEyLv7ru73BeGG8pCRiC4")

# Replace 'file_path.jpg' with the actual path to your local image file.
files = ["../uploads/video.mp4"]

config = FaceConfig()
job = client.submit_job([], [config], files=files)

print(job)
print("Running...")

job.await_complete()
predictions = job.get_predictions()

# Save predictions to a JSON file
with open("predictions.json", "w") as json_file:
    json.dump(predictions, json_file, indent=4)

print("Predictions saved to 'predictions.json'")


