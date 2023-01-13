import mysql.connector as conn # Importing My sql connector

try:
    mydb = conn.connect (host ='localhost',user='root',passwd = 'Amrit@12345')
    # Making connection with MYSQL( Defining user and password )
    query = 'SHOW DATABASES' # Showing Databases

    cursor = mydb.cursor()
    cursor.execute(query) # Executing the query .
    print(cursor.fetchall()) # Printing the available DATABASES

except Exception as e:
    mydb.close()
    print(str(e))


