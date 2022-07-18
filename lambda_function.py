import json
from rook.serverless import serverless_rook
import rook
rook.start(token="4bbe3a5e42fc852021d3cc29a4aa4ce14d1efc50fdff8a309df01fe367f73d01", tags=["tag1"])
@serverless_rook
def lambda_handler(event, context):
    return 'Hello World'
def lambda_handler(event, context):
    name = event['firstName'] +' '+ event['lastName']
    return {
    'statusCode': 200,
    'body': json.dumps('thanks for testing rookout, ' + name)
    }