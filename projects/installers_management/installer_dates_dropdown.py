from rule import Rule
from gsheets_update_cell import GSheetsUpdateCell
from gsheets_update import GSheetsUpdate
import re


def installer_dates_dropdown(spreadsheet):
    
    # Read the date worksheet
    sheet_dates = spreadsheet.worksheet('CALENDAR INSTALLERS')

    # Read input data
    dates = {}
    values = sheet_dates.get_all_values()
    for row in values[1::]:

        try: installer = row[0]
        except IndexError: break

        installer_dates = row[1::]
        installer_dates = [d.strip() for d in installer_dates if d]
        
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
        dates[installer] = list(set(dates[installer]))
        dates[installer].sort(key=lambda x: x[-4::]+x[3:5]+x[0:2])

        for c in to_update:
            # Create the  object
            request = GSheetsUpdateCell('dropdown')

            request.range(c.row-1, c.row, c.col-1, c.col)
            request.sheet_id(sheet_projects.id)
            request.value_list(dates[installer])

            update.add_request(request)

    return update


rule_installer_dates_dropdown = Rule(installer_dates_dropdown)
