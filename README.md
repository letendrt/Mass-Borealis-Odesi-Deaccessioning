# Mass-Borealis-Odesi-Deaccessioning
This tool is solely for super-admins.

## Code Purpose 🤔❓
1) Creates TXT file holding automatically generated CURL commands for dataset deaccessioning (instructions on specific shell command line found below).
2) Creates dataset backups.
3) Creates JSON files for deaccessioning reason (links DOI of other dataset if it is a duplicate)

## Minimum Python Requirements 🐍🔧
1) Local IDE (Jupyter, Wing, PyCharm, etc.)
2) Minimum python version: 3.6+

## User Guide 🪧🛃

1) Start by filling out the CSV sheet below for all of the datasets you wish to deaccession. The present Sheet holds standardised field entry options that allow for the code to run efficiently. You must use a copy of this sheet to run the script. Any deviation from the column names or entry names could result in unsuccessful file harvesting for backup and JSON file creation.
              https://docs.google.com/spreadsheets/d/1K07RApf98HVDQhxC0QBldHvUDj3MPArOs6k3liUatGQ/copy
