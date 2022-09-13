# importing the required libraries
import gspread
from gsheets.rules.rules import rules
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import json

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/bus/quantum-conduit-362307-65d4233c5be8.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
spreadsheet_installers = client.open_by_url('https://docs.google.com/spreadsheets/d/1t9OwWtZHR96VsnzgBSAk1eVHeUVsBMybcEWmW4WgGqA/edit#gid=1421917402')

# execute all rules
for rule in rules: rule(spreadsheet_installers)