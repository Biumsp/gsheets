from .rule import Rule
from ..gsheets_update_cell import GSheetsUpdateCell
from ..gsheets_update import GSheetsUpdate
import re


def installer_dates_dropdown(spreadsheet):
    
    # Read the date worksheet
    print('reading calendar installers')
    sheet_dates = spreadsheet.worksheet('CALENDAR INSTALLERS')

    # Read input data
    dates = {}
    for row in [sheet_dates.row_values(x+1) for x in range(sheet_dates.row_count)]:

        print(f'getting row {row}')
        installer = row[0].value

        # Stop if the installer name is invalid
        if not re.match(r'[\w\s\d_-]+', installer): break

        installer_dates = []
        for col in range(1, sheet_dates.col_count+1):
            
            print(f'getting column {col}')
            date = row[col+1].value

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

        projects = [p for p in all_projects if p.value.strip().lower() == installer]

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

        for c in to_update:
            # Create the  object
            request = GSheetsUpdateCell('dropdown')

            request.range(c.row-1, c.row, c.col-1, c.col)
            request.sheet_id(sheet_projects.id)

            update.add_request(request)

    return update.body


rule_installer_dates_dropdown = Rule(installer_dates_dropdown)