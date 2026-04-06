# Mass-Borealis-Odesi-Deaccessioning
This tool is solely for super-admins.

## Code Purpose 🤔❓
1) Creates TXT file holding automatically generated CURL commands for dataset deaccessioning (instructions on specific shell command line found below).
2) Creates dataset backups on local drive.
3) Creates JSON files for deaccessioning reason and actual dataset linkage (links DOI of other dataset if it is a duplicate).
4) Automatically generates Shell command lines.

## Minimum Python Requirements 🐍🔧
1) Local IDE (Jupyter, Wing, PyCharm, etc.)
2) Minimum python version: 3.6+

## File Requirements 📂🔧
1) Start by filling out the Google sheet below for all of the datasets you wish to deaccession. The original code was written assuming that the to-be deaccessioned files were incomplete duplicates of another dataset due to a migration issue between Nesstar and Dataverse. The CSV sheet reflects this. The code, as it currently stands, does not allow for the deaccessioning of datasets that are unique - these should be deaccessioned manually. There are a few columns that MUST be filled: "DOI", "Duplicate?" (will always be yes given the nature of the code), "Duplicate DOI", "Which should be kept?", and "Deaccession Reason". The sheet link can also be found in the Python code above.
              https://docs.google.com/spreadsheets/d/1K07RApf98HVDQhxC0QBldHvUDj3MPArOs6k3liUatGQ/copy
2) Export the filled out Google Sheet in CSV format.
3) Download the python code attached to this GitHub repository, and open it in a local python IDE or environment (Wing, PyCharm, linux environment, etc. - no cloud based IDE like Google Colab).
4) Place the python script and the CSV sheet in a same folder (as depicted in the figure below).

    <kbd><img width="901" height="331" alt="image" src="https://github.com/user-attachments/assets/eecb633a-be96-479f-a920-8f0248e2ee06" /></kbd>

    Note that after running the script, your folder will look like this:
        <kbd><img width="867" height="342" alt="image" src="https://github.com/user-attachments/assets/7cc4ad0c-8eab-4753-b943-b5999f511846" /></kbd>

   The script automatically creates a folder architecture to effectively organise the backup files and the deaccession JSON files created by the script. Note also that the script automatically creates the shell command lines described under the 'Shell-based Commands User Guide 🐚🛃' section. Those generated command lines can be found in the 'generated shell commands' file, as depicted below:
       <kbd><img width="1241" height="144" alt="image" src="https://github.com/user-attachments/assets/f6bf7abc-e106-4e0c-95c7-33ce530b29d3" /></kbd>


## Python Script User Guide 🐍🛃
Make sure to have fulfilled the file requirements above before continuing.

1) Navigate to the "API AND FUNCTION PARAMETERS" section of the code (Line 20).

     <kbd><img width="783" height="103" alt="image" src="https://github.com/user-attachments/assets/f5b20f70-0f92-4c1e-bece-000b516b2c0a" /></kbd>

2) Comment out the undesired url_base_origin (keep either demo or production - default is production URL).

    <kbd><img width="471" height="54" alt="image" src="https://github.com/user-attachments/assets/fa168e3c-81dc-494f-88ce-8ec56953c729" /></kbd>

3) Fill out api_token_origin with your API key.

    <kbd><img width="550" height="52" alt="image" src="https://github.com/user-attachments/assets/e6aae2ea-876b-4e90-b831-dcbe35df874b" /></kbd>

4) Copy the path to the csv file in csv_file_directory.

    <kbd><img width="858" height="149" alt="image" src="https://github.com/user-attachments/assets/1c47f295-6402-4feb-9c36-d53133aa3cb0" /></kbd>

4) Comment out the functions you do not desire running. The default is to run both the dataset backup function and the file deaccession TXT file creation function. Either select True or False for both functions.

    <kbd><img width="433" height="120" alt="image" src="https://github.com/user-attachments/assets/054ad9e6-8658-438c-9e6a-5de0a64965e1" /></kbd>

6) Run the python script.

## Shell-based Commands User Guide 🐚🛃
Note that these commands are to be run in PowerShell. Note also that the script automatically generates these commands. They can be found in the 'generated shell commands' text file once the script has been run.

1) Open your shell of choice. The shell itself shouldn't matter as long as it can run BASH.
2) Define $API_TOKEN in the shell environment (the API key below is a fake).

    <kbd><img width="696" height="190" alt="image" src="https://github.com/user-attachments/assets/76447dee-5b8f-4be8-87a2-c07bf82fccf7" /></kbd>

3) Download backups of datasets by running the following command line - make sure to edit in the path to your backup_commands.txt file created by the python script:

    ```Get-Content "C:\path\to\backup_commands.txt" | ForEach-Object { Invoke-Expression $_ }```
   
   Running this command will download all datasets listed in the log.txt file as ZIP packages. Make sure to navigate to your download directory of choice before initiating the command.

4) Confirm that backups were downloaded.

    <kbd><img width="932" height="337" alt="image" src="https://github.com/user-attachments/assets/f127536b-537b-44c4-b1a1-6565705392b5" /></kbd>

5) Run the commands to deaccession the datasets. Before running the command, make sure that the deac_commands.txt file is in the same directory as the deaccession reason JSON files created by the python script above. This command will only run with the API token of a super-admin.

   ⚠️DEACCESSIONING A DATASET IS FINAL - THERE IS NO GOING BACK⚠️

    ```Get-Content "C:\path\to\deac_commands.txt" | ForEach-Object { Invoke-Expression $_ }```

6) Celebrate - you're done! 🎊🎊

