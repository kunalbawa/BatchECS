import json
import os

commit_id = os.environ['COMMIT_ID']
bucket_name = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    print('Received event: ' + json.dumps(event, indent=2))
    print('COMMIT_ID: %s, S3_BUCKET: %s' % (commit_id, bucket_name))