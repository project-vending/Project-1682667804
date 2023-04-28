python
from pyspark.streaming import StreamingContext

# Set up the Spark StreamingContext with a batch interval of 10 seconds
ssc = StreamingContext(sparkContext, 10)

# Create a DStream from a Kinesis stream
dstream = KinesisUtils.createStream(
    ssc, "myApp", "myStream", "kinesis.us-west-2.amazonaws.com",
    "us-west-2", InitialPositionInStream.LATEST, 10)

# Perform transformations on the DStream
transformed = dstream.map(lambda x: x.lower())

# Write the transformed data to Redis
transformed.foreachRDD(lambda rdd: rdd.foreachPartition(write_to_redis))

# Start the Spark StreamingContext
ssc.start()
ssc.awaitTermination()
