# hydrop SharePoint Sync

A Python package for importing and exporting data to/from hydrop SharePoint folders.

## Installation guide

1. Clone the repository in the local machine
2. Go the project root folder
3. Open  terminal 
4. Execute "pip install ."

The *hydrop-sharepointsync* package will be installed sucessfully 

## How to use it in other projects?

1. Create a .env file in your main project to store the below paths.

`SHAREPOINT_SOURCE_PATH=/remote/path/to/sharepoint/source`  
`LOCAL_DESTINATION_PATH=/path/to/local/destination`  
`LOCAL_SOURCE_PATH=/path/to/local/source`  
`SHAREPOINT_DESTINATION_PATH=/remote/path/to/sharepoint/destination`  

2. Use 'python-dotenv' to load environment variables in the main project and use them as arguments for the functions

## Example usage:

```python
import os
from dotenv import load_dotenv
from hydrop-sharepointsync.sync import import_from_sharepoint, export_to_sharepoint

# Load environment variables from .env file
load_dotenv()

# Get paths from environment variables
sharepoint_source_path = os.getenv('SHAREPOINT_SOURCE_PATH')
local_destination_path = os.getenv('LOCAL_DESTINATION_PATH')
local_source_path = os.getenv('LOCAL_SOURCE_PATH')
sharepoint_destination_path = os.getenv('SHAREPOINT_DESTINATION_PATH')

# Import data from SharePoint
import_from_sharepoint(sharepoint_source_path, local_destination_path)

# Export data to SharePoint
export_to_sharepoint(local_source_path, sharepoint_destination_path)
```

## Important Feature:
The tool will not allow a creation of new directory in the Sharepoint. The files can the copied only if the specified directory is existing in the Sharepoint. 

## Limitation: 
1. The tool cannot copy a specific file in a directory. The tool copies the directories itself.
2. If the copied files are renamed and then again the same directory in imported, then the tool would copy the original file as well. (Duplicates will be creatred in the destination folder)


