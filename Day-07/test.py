import sys

type = sys.argv[1]

if type == "t2.micro":
    print ("it will charge you 2 dollars a day")
elif type == "t2.medium":
    print ("it will charge you 4 dollars a day")
elif type == "t2.xlarge":
    print ("it will charge you 8 dollars a day")
else:
    print ("Please provide valid instance type")
    