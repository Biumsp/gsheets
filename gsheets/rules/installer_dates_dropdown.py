from rules.rule import Rule
from gsheets.gsheets_update_cell import GSheetsUpdateCell
import re


def installer_dates_dropdown(spreadsheet):
    
    # Read the date worksheet
    sheet_dates = spreadsheet.worksheet('CALENDAR INSTALLERS')

    # Read input data
    dates = {}
    for row in [sheet_dates.row_values(x) for x in range(sheet_dates.row_count)]:

        installer = row[0].value

        # Stop if the installer name is invalid
        if not re.match(r'[\w\s\d_-]+', installer): break

        installer_dates = []
        for col in range(sheet_dates.col_count):

            date = row[col+1].value

            # Stop if the date is invalid
            if not re.match(r'\d\d/\d\d/\d\d', date): break

            installer_dates.append(date.strip())
        
        dates.update({installer.strip().lower(): installer_dates})

    # Read the projects worksheet
    sheet_projects = spreadsheet.worksheet('Copy of MAIN - Mike')

    # Get all projects
    all_projects = sheet_projects.col_values(2)

    # Get dates to be updated and modify available dates
    for installer in dates:
        selected  = []
        to_update = []

        projects = [p for p in projects if p.value.strip().lower() == installer]

        for p in projects:
            project_date_cell = sheet_projects.cell(p.row, 10)
            project_date = project_date.value

            if project_date:
                selected.append(project_date)
            else:
                to_update.append(project_date_cell)

        # Remove selected dates from available dates
        for s in selected:
            dates[installer] = dates[installer].remove(s)

        # Remove duplicates
        dates[installer] = set(dates[installer])

        # Create the  object
        request = GSheetsUpdateCell('dropdown')

        for 



    requests = []

    

    # Create the update object
    update = GSheetsUpdate()

    # Add requests to update
    for r in requests: update.add_request(request)

    return update.body


rule_installer_dates_dropdown = Rule(installer_dates_dropdown)