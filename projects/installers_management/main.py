# importing the required libraries
from rules import rules
from oauth2client.service_account import ServiceAccountCredentials
import gspread, time

def main(request):
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    start = time.time()
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    print("ServiceAccount = ", time.time()-start)
    start = time.time()

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    print("Client = ", time.time()-start)
    start = time.time()

    # get the instance of the Spreadsheet
    spreadsheet_installers = client.open_by_url('https://docs.google.com/spreadsheets/d/1t9OwWtZHR96VsnzgBSAk1eVHeUVsBMybcEWmW4WgGqA/edit#gid=382931988')
    print("Spreadsheet = ", time.time()-start)
    start = time.time()

    # execute all rules
    for rule in rules['spreadsheet_installers']: rule(spreadsheet_installers)
    print("Rules = ", time.time()-start)
    start = time.time()

    return 200

if __name__=='__main__':
    main('')
