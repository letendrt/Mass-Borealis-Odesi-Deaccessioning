# Mass-Borealis-Odesi-Deaccessioning
This tool is solely for super-admins.

## Code Purpose 🤔❓
1) Creates TXT file holding automatically generated CURL commands for dataset deaccessioning (instructions on specific shell command line found below).
2) Creates dataset backups on local drive.
3) Creates JSON files for deaccessioning reason and actual dataset linkage (links DOI of other dataset if it is a duplicate).

## Minimum Python Requirements 🐍🔧
1) Local IDE (Jupyter, Wing, PyCharm, etc.)
2) Minimum python version: 3.6+

## Python Script User Guide 🐍🛃

1) Start by filling out the Google sheet below for all of the datasets you wish to deaccession. The original code was written assuming that the to-be deaccessioned files were incomplete duplicates of another dataset due to a migration issue between Nesstar and Dataverse. The CSV sheet reflects this. The code, as it currently stands, does not allow for the deaccessioning of datasets that are unique - these should be deaccessioned manually. There are a few columns that MUST be filled: "DOI", "Duplicate?" (will always be yes given the nature of the code), "Duplicate DOI", "Which should be kept?", and "Deaccession Reason". The sheet link can also be foudn in the Python code above.
              https://docs.google.com/spreadsheets/d/1K07RApf98HVDQhxC0QBldHvUDj3MPArOs6k3liUatGQ/copy
2) Export the filled out Google Sheet in CSV format.
3) Download the python code attached to this GitHub repository, and open it in a local python IDE or environment (Wing, PyCharm, linux environment, etc. - no cloud based IDE like Google Colab). 
4) Navigate to the "API AND FUNCTION PARAMETERS" section of the code (Line 20).

     <kbd><img width="783" height="103" alt="image" src="https://github.com/user-attachments/assets/f5b20f70-0f92-4c1e-bece-000b516b2c0a" /></kbd>

5) Comment out the undesired url_base_origin (keep either demo or production - default is production URL).

    <kbd><img width="471" height="54" alt="image" src="https://github.com/user-attachments/assets/fa168e3c-81dc-494f-88ce-8ec56953c729" /></kbd>

6) Fill out api_token_origin with your API key.

    <kbd><img width="550" height="52" alt="image" src="https://github.com/user-attachments/assets/e6aae2ea-876b-4e90-b831-dcbe35df874b" /></kbd>

7) Copy the path to the csv file in csv_file_directory.

    <kbd><img width="858" height="149" alt="image" src="https://github.com/user-attachments/assets/1c47f295-6402-4feb-9c36-d53133aa3cb0" /></kbd>

8) Comment out the functions you do not desire running. The default is to run both the dataset backup function and the file deaccession TXT file creation function. Either select True or False for both functions.

    <kbd><img width="433" height="120" alt="image" src="https://github.com/user-attachments/assets/054ad9e6-8658-438c-9e6a-5de0a64965e1" /></kbd>

9) Run the python script.

## Shell-based Commands User Guide 🐚🛃
Note that these commands were run in PowerShell.

1) Open your shell of choice. The shell itself shouldn't matter as long as it can run BASH.
2) Define $API_TOKEN in the shell environment (the API key below is a fake).

    <kbd><img width="696" height="190" alt="image" src="https://github.com/user-attachments/assets/76447dee-5b8f-4be8-87a2-c07bf82fccf7" /></kbd>

3) Download backups of datasets by running the following command line - make sure to edit in the path to the log.txt file created by the python script:

    ```Get-Content "C:\path\to\log.txt" | ForEach-Object { Invoke-Expression $_ }```
   Running this command will download all datasets listed in the log.txt file as ZIP packages.




