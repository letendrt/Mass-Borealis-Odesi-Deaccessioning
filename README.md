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

1) Start by filling out the CSV sheet below for all of the datasets you wish to deaccession. The original code was written assuming that the to-be deaccessioned files were incomplete duplicates of another dataset due to a migration issue between Nesstar and Dataverse. The CSV sheet reflects this. The code, as it currently stands, does not allow for the deaccessioning of datasets that are unique - these should be deaccessioned manually. There are a few columns that MUST be filled: "DOI", "Duplicate?" (will always be yes given the nature of the code), "Duplicate DOI", "Which should be kept?", and "Deaccession Reason".
              https://docs.google.com/spreadsheets/d/1K07RApf98HVDQhxC0QBldHvUDj3MPArOs6k3liUatGQ/copy
