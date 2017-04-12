import boto3

dynamodb = boto3.resource('dynamodb')


def create_table():
    table = dynamodb.create_table(
        TableName='ordertable',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'location',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'items',
                'AttributeType': 'LIST'
            },
            {
                'AttributeName': 'links',
                'AttributeType': 'MAP'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'status',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'message',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='ordertable')
    # Print out some data about the table.
    print(table.item_count)

create_table()
