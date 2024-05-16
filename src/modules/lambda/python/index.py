import json
from datetime import datetime

def lambda_handler(event, context):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        'statusCode': 200,
        'body': json.dumps({'currentTime': current_time})
    }