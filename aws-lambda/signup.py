import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('User')

def lambda_handler(event, context):
    print(event)
    table.put_item(Item=event)
    return {
        'statusCode': 200,
        'body': json.dumps('User added successfully!')
    }