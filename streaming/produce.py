import argparse
import io
import json
import os
from datetime import datetime
from time import sleep
import random

import numpy as np
from bson import json_util
from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic

parser = argparse.ArgumentParser()

parser.add_argument(
    "-m",
    "--mode",
    default="setup",
    choices=["setup", "teardown"],
    help="Whether to setup or teardown a Kafka topic with driver stats events. Setup will teardown before beginning emitting events.",
)

parser.add_argument(
    "-b",
    "--bootstrap-server",
    default="localhost:9092",
    help="Where the bootstrap server is",
)

parser.add_argument(
    "-c",
    "--schemas_path",
    default="./avro_schemas",
    help="Folder containing all generated Avro schemas",   
)

parser.add_argument(
    "-i",
    "--image_dir",
    default="./images",
    help="Directory containing the images to send."
)

args = parser.parse_args()

image_id_counter = 1

def create_topic(admin, topic_name):
    try:
        topic = NewTopic(
            name=topic_name, 
            num_partitions=1,
            replication_factor=1
        )
        
        admin.create_topics([topic])
        
        print(f"A new topic {topic_name} has been created.")
    except Exception as e:
        print(f"Topic {topic_name} already exists. Skipping creation!")
        pass
    
