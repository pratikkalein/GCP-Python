from google.cloud import compute_v1
from collections import defaultdict
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "key.json"

instace_client = compute_v1.InstancesClient()
request = compute_v1.AggregatedListInstancesRequest()
request.project = 'project-id'

agg_list = instace_client.aggregated_list(request=request)

all_instances = defaultdict(list)
print("Instances found:")
for zone, response in agg_list:
        if response.instances:
            all_instances[zone].extend(response.instances)
            print(f" {zone}:")
            for instance in response.instances:
                print(f" - {instance.name} ({instance.machine_type}) {instance.status}")
