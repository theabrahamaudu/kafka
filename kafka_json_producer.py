# Kafka with JSONSerializer

import os
import argparse
from uuid import uuid4
from six.moves import input
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import pandas as pd
from typing import List
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ENDPOINT_SCHEMA_URL = os.getenv("ENDPOINT_SCHEMA_URL")
BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER")
SECURITY_PROTOCOL = os.getenv("SECURITY_PROTOCOL")
SSL_MACHENISM = os.getenv("SSL_MACHENISM")
SCHEMA_REGISTRY_API_KEY = os.getenv("SCHEMA_REGISTRY_API_KEY")
SCHEMA_REGISTRY_API_SECRET = os.getenv("SCHEMA_REGISTRY_API_SECRET")