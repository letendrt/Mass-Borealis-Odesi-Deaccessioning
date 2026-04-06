# File backup and deaccessioning


# GitHub link: https://github.com/letendrt/Mass-Borealis-Odesi-Deaccessioning

################################################################################
# ------------------------------------LIBRARIES----------------------------------
################################################################################

import os
import csv
import json
import requests
import subprocess
import pandas as pd

import pyDataverse
import pyDataverse.utils as utils
from pyDataverse.api import NativeApi, DataAccessApi


################################################################################
# ----------------------------API AND FUNCTION PARAMETERS------------------------
################################################################################


url_base_origin = 'https://borealisdata.ca'
#url_base_origin = 'https://demo.borealisdata.ca'

api_token_origin = 'PASTE API KEY HERE'  
api_origin = NativeApi(url_base_origin, api_token_origin)


# The CSV file should bebased off of this sheet: 
# https://docs.google.com/spreadsheets/d/1K07RApf98HVDQhxC0QBldHvUDj3MPArOs6k3liUatGQ/copy

# For example of how to fill in the sheet, refer to the example sheet:
# https://docs.google.com/spreadsheets/d/1WzCO-m8e2JI_93013AwKtLGjVMSAEhGgri-gDVGIkzU/
csv_file_directory = r"copy/path/here/file.csv"


create_backup = True
# create_backup = False

create_deaccess_file = True
# create_deaccess_file = False


################################################################################
# ---------------------------CREATING BACKUP: CODE PROPER------------------------
################################################################################

def logger(row, api_token_origin, url_base_origin, api_origin):
    
    json_format = {}
    if row['Which should be kept?'] == 'Duplicate':                     # If standardised field is set to 'Duplicate'
        
        json_format['deaccessionReason'] = row['Deaccession Reason:']        # Extracts the deaccessionign reason, writes it to JSON file
        json_format['deaccessionForwardURL'] = row['Duplicate DOI']          # Links to kept dataset, writes it to JSON file
        print(json_format)

        PID_deac = row['DOI']                                        # Extracts the to-be deleted dataset DOI
        resp = api_origin.get_dataset(PID_deac)                      # API calls dataset information
                    
        print(PID_deac)
        print(resp.json())

        if resp.status_code == 200:                                   # If API pull is successfull
            dataset_id = resp.json()['data']['id']                    # Fetch dataset ID
            latest_version = resp.json()['data']['latestVersion']     # Fetch dataset version
            datasetID = latest_version['datasetId']                   # Fetch dataset version ID
            version_num = float(latest_version['versionNumber'])      # Set dataset version as float variable
            print(latest_version)
            print(version_num)

        print(url_base_origin)
        print(datasetID)
        print(version_num)


    elif (row['Which should be kept?'] == 'First one (more accurate)'     # If the dataset to keep is that of the first DOI entered in the CSV sheet
          or row['Which should be kept?'] == 'Either - Identical'):       # Or if the deleted dataset does not matter (they are identical datasets)

        json_format['deaccessionReason'] = row['Deaccession Reason:']     # Extracts the deaccessionign reason, writes it to JSON file
        json_format['deaccessionForwardURL'] = row['DOI']                 # Links to kept dataset, writes it to JSON file
        print(json_format)

        PID_deac = row['Duplicate DOI']                                   # Extracts the to-be deleted dataset DOI
        resp = api_origin.get_dataset(PID_deac)                           # API calls dataset information
                    
        print(PID_deac)
        print(resp.json())

        if resp.status_code == 200:                                       # If API pull is successfull
            dataset_id = resp.json()['data']['id']                        # Fetch dataset ID
            latest_version = resp.json()['data']['latestVersion']         # Fetch dataset version
            datasetID = latest_version['datasetId']                       # Fetch dataset version ID
            version_num = float(latest_version['versionNumber'])          # Set dataset version as float variable
            print(latest_version)
            print(version_num)

        print(url_base_origin)
        print(datasetID)
        print(version_num)

    else:                                                 # If neither row conditions are met
        print('Skipped')                                  # Do not add the file to the JSON file
        val = 0
        return val


    if 'https://doi.org/' in PID_deac:                                # Check DOI structure in the CSV sheet
        PID_deac = PID_deac.replace('https://doi.org/', 'doi:')       # If in https format, convert do doi: format
    print(PID_deac)
    
    listed_returns = [PID_deac, datasetID, version_num, json_format]
    
    return listed_returns




# Function that creates a .txt file with curl commands
# These curl commands are used to download datasets in ZIP format
# .txt file must be run in terminal to download dataset files - see GitHub for instructions
# Takes 4 arguments, all of which are defined above in the parameters section
# Basically works the exact same way as the other function below
def backup_creator(csv_file_directory, api_token_origin, url_base_origin, api_origin):
    
    with open(csv_file_directory, newline='', encoding='utf-8-sig') as csvfile:          # Reads CSV file defined above
        reader = csv.DictReader(csvfile)                                                 # Create reader
        
        with open('backup_commands.txt', 'w') as f:                                 # Create the .txt file
            for row in reader:                                                      # Parse through CSV rows
                #print(row)
                
                contents = logger(row, api_token_origin, url_base_origin, api_origin)
                
                if contents == 0:
                    continue
                
                else:
                    curl_call = f'curl -L -O -J -H "X-Dataverse-key:$API_TOKEN" {url_base_origin}/api/access/dataset/:persistentId/?persistentId={contents[0]}'       # Create CURL command
                
                    f.write(curl_call)                            # Write CURL command to JSON txt file
                    f.write('\n')                                 # Skip a line in .txt file

                    print(curl_call)
                    print()                                       # Space added for human readability in the python shell log 


################################################################################
# -------------------DEACCESSIONING FILE CREATOR: CODE PROPER--------------------
################################################################################


# Function that creates a .txt file with curl commands
# These curl commands are used to deaccession and link datasets in dataverse
# .txt file must be run in terminal to download dataset files - see GitHub for instructions
# Takes 4 arguments, all of which are defined above in the parameters section
# Basically works the exact same way as the function above
def deaccess_creator(csv_file_directory, api_token_origin, url_base_origin, api_origin):
    print('STARTING DEACCESSION FILE CREATION PROCESS')
    
    with open(csv_file_directory, newline='', encoding='utf-8-sig') as csvfile:        # Reads CSV file defined above
        reader = csv.DictReader(csvfile)                                               # Create reader
        
        with open('deaccession_commands.txt', 'w') as g:                               # Create the .txt file
            for row in reader:                                                         # Parse through CSV rows 
                #print(row)
                
                contents = logger(row, api_token_origin, url_base_origin, api_origin)   # Run the log function
                if contents == 0:
                    continue
                
                else:
                    # Sanitize PID_deac for filename creation by replacing problematic characters
                    sanitized_pid_deac = contents[0].replace(':', '_').replace('/', '_').replace('.', '_')
                    name = f'deac_{sanitized_pid_deac}.json'
                
                    with open(name, "w") as f:                        # Create JSON file
                        json.dump(contents[3], f)                     # Write deaccession reason to JSON file
        
                        curl_call = f'curl -H "X-Dataverse-key:$API_TOKEN" -X POST "{url_base_origin}/api/datasets/{contents[1]}/versions/{contents[2]}/deaccession" -H "Content-type:application/json" --upload-file {name}'
                        g.write(curl_call)
                        g.write('\n')
        
                        print(curl_call)
                        print()            



################################################################################
# -----------------RUNNING FUNCTIONS AND CREATING MASTER COMMANDS---------------
################################################################################

current_dir = os.getcwd()
with open('generated_shell_commands.txt', 'w') as p:


    if create_backup == True:
        os.chdir(f'{current_dir}')
        os.mkdir('Backup File Folder')
        
        exp = '{ Invoke-Expression $_ }'
        cur_file_dir = rf'{current_dir}\Backup File Folder\backup_commands.txt'
        p.write('BACKUP COMMAND')
        p.write('\n')
        p.write(f'Get-Content "{cur_file_dir}" | ForEach-Object { exp }')
        p.write('\n')
        p.write('\n')
        
        os.chdir(rf'{current_dir}\Backup File Folder')
        backup_creator(csv_file_directory, api_token_origin, url_base_origin, api_origin)


    if create_deaccess_file == True:
        os.chdir(f'{current_dir}')
        os.mkdir('Deaccession JSONs and Commands')
        
        exp = '{ Invoke-Expression $_ }'
        cur_file_dir = rf'{current_dir}\Deaccession JSONs and Commands\deaccession_commands.txt'
        p.write('DEACCESSION COMMAND')
        p.write('\n')
        p.write(f'Get-Content "{cur_file_dir}" | ForEach-Object { exp }')
        p.write('\n')
        p.write('\n')        
        
        os.chdir(f'{current_dir}/Deaccession JSONs and Commands')
        deaccess_creator(csv_file_directory, api_token_origin, url_base_origin, api_origin)
