import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",     # Replace with your MySQL username
    password="#Amol@22", # Replace with your MySQL password
    database="library"  # Replace with your database name
)
cursor = db_connection.cursor()

# Tkinter GUI setup
root = Tk()
root.title("Employee Database Navigation")

# Function to display a record
def show_record(record):
    entry_id.delete(0, END)
    entry_id.insert(END, record[0])
    entry_first_name.delete(0, END)
    entry_first_name.insert(END, record[1])
    entry_last_name.delete(0, END)
    entry_last_name.insert(END, record[2])
    entry_department.delete(0, END)
    entry_department.insert(END, record[3])
    entry_salary.delete(0, END)
    entry_salary.insert(END, record[4])

# Load the first record
def load_first_record():
    cursor.execute("SELECT * FROM employees ORDER BY id ASC LIMIT 1")
    record = cursor.fetchone()
    if record:
        show_record(record)

# Add a new employee
def add_record():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    department = entry_department.get()
    salary = entry_salary.get()
    if first_name and last_name and department and salary:
        cursor.execute("INSERT INTO employees (first_name, last_name, department, salary) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, department, salary))
        db_connection.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        load_first_record()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Update an existing employee
def edit_record():
    emp_id = entry_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    department = entry_department.get()
    salary = entry_salary.get()
    if emp_id and first_name and last_name and department and salary:
        cursor.execute("UPDATE employees SET first_name=%s, last_name=%s, department=%s, salary=%s WHERE id=%s",
                       (first_name, last_name, department, salary, emp_id))
        db_connection.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
    else:
        messagebox.showwarning("Input Error", "Please select a record to update.")

# Delete an employee
def delete_record():
    emp_id = entry_id.get()
    if emp_id:
        cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
        db_connection.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        load_first_record()
    else:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")

# Navigate to the next record
def next_record():
    emp_id = entry_id.get()
    cursor.execute("SELECT * FROM employees WHERE id > %s ORDER BY id ASC LIMIT 1", (emp_id,))
    record = cursor.fetchone()
    if record:
        show_record(record)
    else:
        messagebox.showinfo("End of Records", "No more records available.")

# Navigate to the previous record
def previous_record():
    emp_id = entry_id.get()
    cursor.execute("SELECT * FROM employees WHERE id < %s ORDER BY id DESC LIMIT 1", (emp_id,))
    record = cursor.fetchone()
    if record:
        show_record(record)
    else:
        messagebox.showinfo("Start of Records", "No previous records available.")

# Layout for the GUI
Label(root, text="Employee ID").grid(row=0, column=0)
Label(root, text="First Name").grid(row=1, column=0)
Label(root, text="Last Name").grid(row=2, column=0)
Label(root, text="Department").grid(row=3, column=0)
Label(root, text="Salary").grid(row=4, column=0)

entry_id = Entry(root, state="readonly")
entry_id.grid(row=0, column=1)
entry_first_name = Entry(root)
entry_first_name.grid(row=1, column=1)
entry_last_name = Entry(root)
entry_last_name.grid(row=2, column=1)
entry_department = Entry(root)
entry_department.grid(row=3, column=1)
entry_salary = Entry(root)
entry_salary.grid(row=4, column=1)

Button(root, text="Add", command=add_record).grid(row=5, column=0)
Button(root, text="Edit", command=edit_record).grid(row=5, column=1)
Button(root, text="Delete", command=delete_record).grid(row=5, column=2)
Button(root, text="Previous", command=previous_record).grid(row=6, column=0)
Button(root, text="Next", command=next_record).grid(row=6, column=1)

# Load the first record on start
load_first_record()

# Start the Tkinter loop
root.mainloop()

# Close the database connection on exit
cursor.close()
db_connection.close()
