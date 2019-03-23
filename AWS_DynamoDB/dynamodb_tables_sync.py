"""Sync dynamoDB tables within the same AWS account or across accounts"""
import argparse
import boto3


def source_dynamo_read(source, destination, masteraccount, targetaccount):
    """Read from the source table"""
    aws_session = boto3.Session(profile_name=masteraccount)
    dynamodb = aws_session.resource('dynamodb')
    table = dynamodb.Table(source)
    response = table.scan()
    for item in response[u'Items']:
        target_daynamo_put(destination, targetaccount, item)


def target_daynamo_put(destination, targetaccount, item):
    """Insert items into the destination table"""
    aws_session = boto3.Session(profile_name=targetaccount)
    dynamodb = aws_session.resource('dynamodb').Table(destination)
    dynamodb.put_item(TableName=destination, Item=item)


def main():
    """Get user input"""
    parser = argparse.ArgumentParser(description='read env name')
    parser.add_argument('-s', '--source', type=str, help='Source table name', required=True)
    parser.add_argument('-d', '--destination', type=str, help='Destination table name', required=True)
    parser.add_argument('-m', '--masteraccount', type=str, help='AWS profile of the source table table name',
                        required=True)
    parser.add_argument('-t', '--targetaccount', type=str, help='AWS profile of the target table table name',
                        required=True)

    args = parser.parse_args()
    source = args.source
    destination = args.destination
    masteraccount = args.masteraccount
    targetaccount = args.targetaccount
    source_dynamo_read(source, destination, masteraccount, targetaccount)


main()
