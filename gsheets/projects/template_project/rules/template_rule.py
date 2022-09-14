from .rule import Rule
from ..gsheets_update_cell import GSheetsUpdateCell
from ..gsheets_update import GSheetsUpdate
import re


def installer_dates_dropdown(spreadsheet):
    
    # Read the date worksheet
    sheet_dates = spreadsheet.worksheet('CALENDAR INSTALLERS')

    # Read input data
    dates = {}
    for x in range(2, 101):

        row = sheet_dates.row_values(x)

        try: installer = row[0]
        except IndexError: break

        # Stop if the installer name is invalid
        if not re.match(r'[\w\s\d_-]+', installer): break

        installer_dates = []
        for col in range(1, 300):
            
            try: date = row[col]
            except IndexError: break

            # Stop if the date is invalid
            if not re.match(r'\d\d/\d\d/\d\d', date): break

            installer_dates.append(date.strip())
        
        dates.update({installer.strip().lower(): installer_dates})

    # Read the projects worksheet
    sheet_projects = spreadsheet.worksheet('Copy of MAIN - Mike')

    # Get all projects
    all_projects = sheet_projects.col_values(2)

    # Create the update object
    update = GSheetsUpdate()

    # Get dates to be updated and modify available dates
    for installer in dates:

        selected  = []
        to_update = []

        # List of row indexes of projects with the same name
        projects_rows = [i+1 for i, p in enumerate(all_projects) if p.strip().lower() == installer]

        for row in projects_rows:
            project_date_cell = sheet_projects.cell(row, 16)
            project_date = project_date_cell.value

            if project_date in dates[installer]:
                selected.append(project_date)
            else:
                to_update.append(project_date_cell)

        # Remove selected dates from available dates
        for s in selected:
            dates[installer].remove(s)

        # Remove duplicates
        print(f'removing duplicates')
        dates[installer] = list(set(dates[installer]))
        dates[installer].sort(key=lambda x: x[-4::]+x[3:5]+x[0:2])

        for c in to_update:
            print(f'adding request to update')

            # Create the  object
            request = GSheetsUpdateCell('dropdown')

            request.range(c.row-1, c.row, c.col-1, c.col)
            request.sheet_id(sheet_projects.id)
            request.value_list(dates[installer])

            update.add_request(request)

    return update


rule_installer_dates_dropdown = Rule(installer_dates_dropdown)