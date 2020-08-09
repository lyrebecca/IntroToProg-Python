# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RLy,8.6.2020,Created started script
# RLy,8.6.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
with open("ToDoList.txt") as file:
    for row in file: # Loops through each row in the file
        dicRow = {} # Creates a new dictionary to hold row data
        (task, priority) = row.split(",") # Separates the list by a comma
        dicRow["task"] = task.strip() # Stores task into dictionary, removes extra spaces
        dicRow["priority"] = priority.strip() # Stores priority into dictionary, removes extra spaces
        lstTable.append(dicRow) # Adds what's in the file to lstTable
    print(lstTable) # Prints what is in the file that is in the lstTable

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for dicRow in lstTable: # Loops through contents of the lstTable
            print(dicRow["task"] + ',' + dicRow["priority"]) # Prints out the keys

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("What task would you like to add?") # Collects task value from user
        strPriority = input("What is the priority?") # Collects priority value from user
        dicRow = {"task": strTask.strip(), "priority": strPriority.strip()} # Strips inputs of any extra spaces
        lstTable.append(dicRow) # Appends user input to lstTable

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strTask = input("Task to Remove: ") # Collects task value from user
        numTasks = len(lstTable) # Grabs length of the table
        for row in lstTable:
            if row["task"].lower() == strTask.lower(): # Checks if the input matches an existing task
                lstTable.remove(row) # Remove task/row
                print("row removed") # Prints confirmation to user
                print(lstTable, '<< List with Dictionary objects') # Prints the lstTable
        if numTasks == len(lstTable): # If no tasks were removed, print "row not found" to user
            print("row not found")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        with open("ToDoList.txt", "w") as file: # Opens ToDoList.txt
            for dicRow in lstTable: # Loops through lstTable by row
                file.write(dicRow["task"] + ',' + dicRow["priority"] + "\n") # Writes tasks & priorities from lstTable to the file
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Goodbye")
        break  # and Exit the program
