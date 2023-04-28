python
import boto3
import json

stream_name = 'my-kinesis-stream'

kinesis = boto3.client('kinesis')

shard_it = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST'
)['ShardIterator']

while True:
  record_response = kinesis.get_records(
    ShardIterator=shard_it,
    Limit=100
  )

  for record in record_response['Records']:
      # Print the raw data to the console
      print(json.loads(record['Data']))

  shard_it = record_response['NextShardIterator']
