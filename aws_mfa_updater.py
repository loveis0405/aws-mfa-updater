import sys
import boto3
import configparser
from os import path

PROFILE_NAME = 'infra'
ARN_OF_THE_MFA_DEVICE = 'MFA_DEVICE_SERIAL'
SESSION_DURATION = 50400

config = configparser.ConfigParser()
config.read([path.join(path.expanduser("~"),'.aws/credentials')])

client = boto3.client('sts')
response = client.get_session_token(DurationSeconds=SESSION_DURATION, SerialNumber=ARN_OF_THE_MFA_DEVICE, TokenCode=sys.argv[1])

access_key = response['Credentials']['AccessKeyId']
secret_key = response['Credentials']['SecretAccessKey']
session_token = response['Credentials']['SessionToken']

if config.has_section(PROFILE_NAME):
    config.remove_section(PROFILE_NAME)
config.add_section(PROFILE_NAME)
config.set(PROFILE_NAME, 'aws_access_key_id', access_key)
config.set(PROFILE_NAME, 'aws_secret_access_key', secret_key)
config.set(PROFILE_NAME, 'aws_session_token', session_token)
config.write(open(path.join(path.expanduser("~"),'.aws/credentials'), "w"))

