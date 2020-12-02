import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('User')


def lambda_handler(event, context):
    print(event)
    cust_name = event['params']['path']['username']
    resp =  table.get_item(Key={
        "username" : cust_name
    })
    
    return resp['Item']
    # TODO implement
   