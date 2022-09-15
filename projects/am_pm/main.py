# importing the required libraries
from gsheets.rules.rules import rules
from gsheets.rules.rule import Rule
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/bus/dev/gsheets/credentials.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
spreadsheet_installers = client.open_by_url('https://docs.google.com/spreadsheets/d/10Z31s0rlv-LNQzrMrI-SOl6TPkmoiF0CZYqpYTv277U/edit#gid=1655103781')

# execute all rules
for rule in rules['spreadsheet_installers']: rule(spreadsheet_installers)