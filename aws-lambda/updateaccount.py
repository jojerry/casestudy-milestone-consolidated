
import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('User')

def lambda_handler(event, context):
    print(event)
    resp = table.get_item(Key={
        "username" : event['username']
      
           }
        )
    if resp:
          table.put_item(Item=event)
    return {
            'statusCode': 200,
            'body': json.dumps('Update success!')
            }