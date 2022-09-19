from rule import Rule
from gsheets_update_cell import GSheetsUpdateCell
from gsheets_update import GSheetsUpdate


def installer_dates_dropdown(spreadsheet):

    COLUMN_DATES = 15
    
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
    sheet_projects = spreadsheet.worksheet('Test Enrico')

    # Get all projects
    all_projects = sheet_projects.col_values(2)
    projects_dates = sheet_projects.col_values(COLUMN_DATES)

    # Create the update object
    update = GSheetsUpdate()

    # Get dates to be updated and modify available dates
    for installer in dates:

        selected  = []  # List of already selected dates for this installer
        to_update = []  # List of rows where there is a dropdown list to update

        # List of row indexes of projects with the same name
        projects_rows = [i for i, p in enumerate(all_projects) if p.strip().lower() == installer]

        for row in projects_rows:
            try: project_date = projects_dates[row]
            except: break

            if project_date in dates[installer]:
                selected.append(project_date)

            to_update.append(row)

        # Remove selected dates from available dates
        for s in selected:
            try: dates[installer].remove(s)
            except: pass

        # Remove duplicates and sort
        dates[installer] = list(set(dates[installer]))
        dates[installer].sort(key=lambda x: x[-4::]+x[3:5]+x[0:2])

        for row in to_update:
            # Create the  object
            request = GSheetsUpdateCell('dropdown')

            request.range(row, row+1, COLUMN_DATES-1, COLUMN_DATES)
            request.sheet_id(sheet_projects.id)
            request.value_list(dates[installer])

            update.add_request(request)

    return update


rule_installer_dates_dropdown = Rule(installer_dates_dropdown)
