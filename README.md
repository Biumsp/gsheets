# Google Sheets Automation

## Structure

```
├── gsheets
│   ├── gsheets_update_cell.py
│   ├── gsheets_update.py
│   ├── gsheets_update_request.py
│   ├── projects
│	│	├──project1
│	│	├──project2
│	│	├──...
│   │   └── template_project
│   │       ├── gsheets_update_cell.py -> ../../gsheets_update_cell.py
│   │       ├── gsheets_update.py -> ../../gsheets_update.py
│   │       ├── main.py
│   │       ├── rules
│   │       │   ├── __init__.py
│   │       │   ├── rule.py -> ../../../rule.py
│   │       │   ├── rules.py
│   │       │   └── template_rule.py
│   │       ├── templates_info.py -> ../../templates_info.py
│   │       └── templates.json -> ../../templates.json
│   ├── rule.py
│   ├── rules.py
│   ├── templates_info.py
│   └── templates.json
└── README.md
```  

- gsheets/ contains all the code
- gsheets/projects are individual automation units: each one with its cloud function and its triggers
- gsheets/projects/template_project is the template for every new project
  
Files  
- gsheets/gsheets_update.py: 			class for a batch update (a list of request)
- gsheets/gsheets_update_request.py: 	class for a single request in a batch update (the elements of the above list)
- gsheets/gsheets_update_cell.py: 		class for an update request of a single cell
- gsheets/rule.py: template for a rule. Rules are stored in the rules/ subfolder of every project
- gsheets/rules.py: intermediate file that collects all the rules in a project in a single list
- gsheets/templates.json: updateCell requests templates
- gsheets/templates_info.json: description of the parameters of the templates 
