import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="shivanggupta",
    user="shivanggupta",
    password= "**********"
)

# Create a cursor object
cur = conn.cursor()

# Execute the CREATE TABLE command, need to only do once
cur.execute("""
    CREATE TABLE mytable (
        insured VARCHAR(255),
        column1 VARCHAR(255),
        column2 VARCHAR(255),
        column3 FLOAT
    );
""")

# Execute the CREATE TABLE command, need to only do once
with open('file_csv.csv', 'r') as file:
    # Read the CSV file
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Loop through each row in the CSV file
    # cur.execute("ALTER TABLE mytable ADD column3 FLOAT")
    for row in reader:
        # Insert the row into the table using an SQL query
        cur.execute("INSERT INTO mytable (insured, column1, column2, column3) VALUES (%s, %s, %s, %s)", ((row[1], ), row[2], row[3], row[4]))


query = "SELECT * FROM mytable"
cur.execute(query)
result = cur.fetchall()
print(result)
# Store the result in another file using python3 starter_code.py > Out.txt


conn.commit()

# Close the cursor and connection
cur.close()
conn.close()






