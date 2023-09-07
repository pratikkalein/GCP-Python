from google.cloud import compute_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "key.json"

compute_client = compute_v1.InstancesClient()

operation = compute_client.stop(
    project='project-id',
    zone='us-west4-b',
    instance='python-instance'
)

operation.result()
print("Instace Stopped!")
