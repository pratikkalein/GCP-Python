from google.cloud import compute_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "key.json"

INSTANCE_NAME = 'python-instance'
MACHINE_TYPE = 'projects/project-id/zones/us-west4-b/machineTypes/e2-medium' 
SUBNETWORK = 'projects/project-id/regions/us-west4/subnetworks/default'
SOURCE_IMAGE = 'projects/project-id/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230831'
NETWORK_INTERFACE = {
    'subnetwork':SUBNETWORK,
    'access_configs': [
        {
            'name':'External NAT'
        }
    ]
}

compute_client = compute_v1.InstancesClient()

config = {
    'name' : INSTANCE_NAME,
    'machine_type' : MACHINE_TYPE,
    'disks': [
        {
            'boot': True,
            'auto_delete': True,
            'initialize_params': {
                'source_image': SOURCE_IMAGE,
            }
        }
    ],

    'network_interfaces' : [NETWORK_INTERFACE]
}

print("Creating instace.....")
operation = compute_client.insert(
    project='project-id',
    zone='us-west4-b',
    instance_resource=config
)

operation.result()

print(f'Created VM Instance:{INSTANCE_NAME}')
