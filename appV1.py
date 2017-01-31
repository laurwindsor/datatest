from flask import Flask
app = Flask(__name__)

@app.route('/')
def v1():
    
    import psycopg2
    import datetime
    import csv
    import pyodbc
    from cookiecutter.main import cookiecutter

# Set working directory 
os.chdir("/Users/lwindsor/Dropbox (Lucid)/Lauren Personal/PythonDataApp")

# Get query options 
with open("Queries/queryOptions.csv", "r") as f:
    queryOptions = csv.reader(f)
    queryOptionsList = list(queryOptions)

# Get user input
print("Select a query: ")
for row in queryOptionsList:
    print(row[0])
selection = input("Selection: ")

# Define output file column headers 
for i in range(0, len(queryOptionsList)-1):
    if(selection == queryOptionsList[i][0]):
        headers = queryOptionsList[i][1]

# Read in query from text file 
with open(str("Queries/"+selection+".txt"), "r") as query:
    querystring = query.read()
    query.close
print("Processing...")

# Date input (where required) 
# x = datetime.date(2017, 1, 10)

# Connect to database
conn = psycopg2.connect(database="dw", user="lwindsor", host="lucid-research.ctr4i8xtibzz.us-east-1.redshift.amazonaws.com", port=5439, password=pw)

# Open a cursor 
cur = conn.cursor()

# Execute query 
cur.execute(querystring)
data = cur.fetchall()

# Close cursor and connection 
cur.close()
conn.close()

# Write csv
with open(str("export_"+selection+".csv"), "w") as ouputFile:
    queryOutput = csv.writer(ouputFile, quotechar="|", quoting=csv.QUOTE_MINIMAL) 
    queryOutput.writerow(headers)
    queryOutput.writerows(data)

print(str("File export_"+selection+".csv can be found in "+os.getcwd()+"."))
