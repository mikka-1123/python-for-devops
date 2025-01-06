import os

folders=input("please provide list of folder names with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like folder doest not exists -", folder )
        continue

    print(" ==== Listing files for folder -", folder)
    
    for file in files:
        print(file)
     