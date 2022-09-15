# importing the required libraries
from rules import rules
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def main(request):
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    spreadsheet_installers = client.open_by_url('https://docs.google.com/spreadsheets/d/1t9OwWtZHR96VsnzgBSAk1eVHeUVsBMybcEWmW4WgGqA/edit#gid=382931988')

    # execute all rules
    for rule in rules['spreadsheet_installers']: rule(spreadsheet_installers)

    return 200

if __name__=='__main__':
    main('')
