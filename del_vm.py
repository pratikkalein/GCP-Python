from google.cloud import compute_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "key.json"

compute_client = compute_v1.InstancesClient()

operation = compute_client.delete(
    project='project-id',
    zone='us-west4-b',
    instance='instance-name'
)

operation.result()
print("Instace deleted successfully!")
