########################################################################
# * Assignment 2 Part 2. File written by Peter Wei pw2428@columbia.edu #
########################################################################

import boto
import boto.dynamodb2
import mraa
import time
import json
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey

DYNAMO_TABLE_NAME = #YOUR TABLE NAME
ACCOUNT_ID = #YOUR ACCOUNT ID
IDENTITY_POOL_ID = #YOUR IDENTITY POOL ID
ROLE_ARN = #YOUR ROLE_ARN

class dynamoMethods:
    def __init__(self, dbName):
        self.table_dynamo = None
        ####################################################################
        # YOUR CODE HERE
        try:
            #1. create new table
            self.table_dynamo = #HINT: Table.create; #HINT 2: Use CUID as your hashkey
            print "New Table Created"
        except Exception as e:
            #2.table already exists, so get the table
            self.table_dynamo = #HINT: Remember to use "connection=client_dynamo"
            print "Table Already Exists"
        ####################################################################

    def dynamoAdd(self, cuid, name, password):
        ####################################################################
        # YOUR CODE HERE
        #1. Check table for entries that have the same CUID, if so, UPDATE (Don't delete)
        #2. Otherwise, create a new entry
        print "New entry created.\n"
        ####################################################################

    def dynamoDelete(self, cuid):
        ####################################################################
        # YOUR CODE HERE
        #1. Check table for entries that have the same CUID, if so, DELETE
        ####################################################################

    def dynamoViewAll(self):
        ####################################################################
        string_db = "CUID: NAME\n"
        print string_db
        #1. Get all entries in the table
        #2. Print the CUID: NAME for each entry
        ####################################################################
        

####################################################################
# DON'T MODIFY BELOW HERE -----------------------------------------#
####################################################################




cognito = boto.connect_cognito_identity()
cognito_id = cognito.get_id(ACCOUNT_ID, IDENTITY_POOL_ID)
oidc = cognito.get_open_id_token(cognito_id['IdentityId'])

sts = boto.connect_sts()
assumedRoleObject = sts.assume_role_with_web_identity(ROLE_ARN, "XX", oidc['Token'])

client_dynamo = boto.dynamodb2.connect_to_region(
        'us-east-1',
        aws_access_key_id=assumedRoleObject.credentials.access_key,
        aws_secret_access_key=assumedRoleObject.credentials.secret_key,
        security_token=assumedRoleObject.credentials.session_token)

DB = dynamoMethods(DYNAMO_TABLE_NAME)

state = 0
input_cuid = None
input_name = None
input_password = None

def get_prompt(state_var):
    if state_var == 0:
        return "Choose an option.\n1. Add to DB\n2. Delete from DB\n3. ViewDB\n"
    elif state_var == 1:
        return "Enter CUID to add: "
    elif state_var == 2:
        return "Enter name to add: "
    elif state_var == 3:
        return "Enter password: "
    elif state_var == 4:
        return "Enter CUID to delete: "
    else:
        return "Bad command..."

try:
    while True:
        prompt = get_prompt(state)
        ans = raw_input(prompt)

        if state == 0:
            if ans == "1":
                state = 1
            elif ans == "2":
                state = 4
            elif ans == "3":
                state = 0
                DB.dynamoViewAll()
            else:
                print "Unsupported command.\n"
        elif state == 1:
            state = 2
            input_cuid = ans
        elif state == 2:
            state = 3
            input_name = ans
        elif state == 3:
            state = 0
            input_password = ans
            DB.dynamoAdd(input_cuid, input_name, input_password)
        elif state == 4:
            state = 0
            input_cuid = ans
            DB.dynamoDelete(input_cuid)
        else:
            state = 0
            print "Something is wrong."
except KeyboardInterrupt:
    exit
        

