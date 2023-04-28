
import os

# Define the directories to create
directories = [
  'data/raw',
  'data/transformed',
  'data/output',
]

# Create the directories
for d in directories:
  os.makedirs(d, exist_ok=True)

# Define the files to create
files = [
  'streaming.py',
  'transform.py',
  'redis_loader.py',
  's3_loader.py',
]

# Create the files in each directory
for d in directories:
  for f in files:
    open(os.path.join(d, f), 'w').close()

# Create the Streamlit visualization file
open('visualization.py', 'w').close()

# Create a requirements.txt file with the necessary dependencies
with open('requirements.txt', 'w') as f:
  f.write('aws-sdk\n')
  f.write('boto3\n')
  f.write('redis\n')
  f.write('pyspark\n')
  f.write('streamlit\n')

print("Project file structure created successfully!")
