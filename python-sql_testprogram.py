import mysql.connector

# Establish connection with MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="20061212",
    database="school"
)

cur = con.cursor()

while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    # CREATE
    if ch == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        query = "INSERT INTO student VALUES (%s, %s, %s)"
        data = (roll, name, marks)

        cur.execute(query, data)
        con.commit()

        print("Record inserted successfully.")

    # READ
    elif ch == 2:
        cur.execute("SELECT * FROM student")
        records = cur.fetchall()

        print("\nRoll No\tName\tMarks")
        for row in records:
            print(row[0], "\t", row[1], "\t", row[2])

    # UPDATE
    elif ch == 3:
        roll = int(input("Enter Roll Number to update: "))
        marks = int(input("Enter new marks: "))

        query = "UPDATE student SET marks = %s WHERE roll_no = %s"
        data = (marks, roll)

        cur.execute(query, data)
        con.commit()

        print("Record updated successfully.")

    # DELETE
    elif ch == 4:
        roll = int(input("Enter Roll Number to delete: "))

        query = "DELETE FROM student WHERE roll_no = %s"

        cur.execute(query, (roll,))
        con.commit()

        print("Record deleted successfully.")

    # EXIT
    elif ch == 5:
        break

    else:
        print("Invalid choice.")

# Close connection
cur.close()
con.close()

print("Database connection closed.")
