########################################################################
# * Assignment 2 Part 3. File written by Peter Wei pw2428@columbia.edu #
########################################################################

import boto
import boto.dynamodb2
import mraa
import time
import json


DYNAMO_TABLE_NAME = 'YOUR_TABLE_NAME'
KINESIS_STREAM_NAME = 'YOUR_KINESIS_STREAM_NAME'
ACCOUNT_ID = 'YOUR_ACCOUNT_ID'
IDENTITY_POOL_ID = 'YOUR_IDENTITY_POOL_ID'
ROLE_ARN = 'YOUR_ROLE_ARN'

#################################################
# Instantiate cognito and obtain security token #
#################################################
# Use cognito to get an identity.
cognito = boto.connect_cognito_identity()
cognito_id = cognito.get_id(ACCOUNT_ID, IDENTITY_POOL_ID)
oidc = cognito.get_open_id_token(cognito_id['IdentityId'])

# Further setup your STS using the code below
sts = boto.connect_sts()
assumedRoleObject = sts.assume_role_with_web_identity(ROLE_ARN, "XX", oidc['Token'])

# Connect to dynamoDB and kinesis
client_dynamo = boto.dynamodb2.connect_to_region(
	'us-east-1',
	aws_access_key_id=assumedRoleObject.credentials.access_key,
    aws_secret_access_key=assumedRoleObject.credentials.secret_key,
    security_token=assumedRoleObject.credentials.session_token)

client_kinesis = boto.connect_kinesis(
	aws_access_key_id=assumedRoleObject.credentials.access_key,
	aws_secret_access_key=assumedRoleObject.credentials.secret_key,
	security_token=assumedRoleObject.credentials.session_token)

from boto.dynamodb2.table import table
from boto.dynamodb2.fields import HashKey

######################
# Setup DynamoDB Table
######################

table_dynamo = # YOUR CODE HERE #

#################################################
# Setup switch and temperature sensor #
#################################################

######################
# YOUR CODE HERE #
######################



try:
	while (1):
		#######################################
		# When button pressed:
		# Post into DynamoDB
		# Change LCD Display
		#######################################
		######################
		# YOUR CODE HERE #
		######################

		#######################################
		# When button pressed again:
		# Post into Kinesis Stream
		# Change LCD Display
		#######################################
		######################
		# YOUR CODE HERE #
		######################

except KeyboardInterrupt:
	exit










