"""
1. Read the file
2. Store in the variable of list
3. Open the file in write mode
4. Update "max_connection" line
"""

def update_server_config(filepath,key,value):
    with open(filepath, "r") as file:
        lines = file.readlines()

    with open(filepath, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_server_config("server.conf", "MAX_CONNECTIONS", "1000")


