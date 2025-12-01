
"""
"""
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent
FILE_DIR = BASE_DIR / "fileScannerMaterial"
#FILE_DIR = FILE_DIR.resolve() # echter absoluter Pfad

def collect_data(path_files)-> list[Path]:
    path_collection = []

    if path_files.exists() and path_files.is_dir():
      
      print("Folder Found")
      print(f"The folder is {path_files}")

      for files in  path_files.iterdir():
        if files.is_file():
            print(f"File {files.name} will be added")
            path_collection.append(files)
        else:
           print("Not a file!")

    else:
      print("No such Folder found")
    return path_collection
      

def get_details(elements)-> dict:
    dict_data = {
       "name": elements.name,
       "ending": elements.suffix,
       "path": elements,
       "size": elements.stat().st_size,
       "changed": datetime.fromtimestamp(elements.stat().st_mtime)
    }
    return dict_data

def print_all(data_list):    
   
    for elements in data_list:
       print("-" * 40)
       print()
       print( elements["name"], "|", elements["ending"] , "|", elements["path"] , "|", elements["size"], "|",elements["changed"] )
       print()


path_list = collect_data(FILE_DIR)
data_list = []
for elements in path_list:  
    dict_data = get_details(elements)
    data_list.append(dict_data)

print_all(data_list)