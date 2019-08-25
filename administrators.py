import pymysql

# Display existing administrators
def display ():
    print("ADMINISTRATOR ACCOUNTS:\n")
    connection = pymysql.connect('localhost', 'root', '', 'staffer')
    cursor = connection.cursor()
    query = "SELECT username, password FROM adminlogin"
    cursor.execute(query)
    output = cursor.fetchall()
    if len(output) == 0:
        print("WARNING:\n\n\tThe adminlogin table has no values. " +
              "Create atleast one account to access the next window")
        return
    desc = cursor.description # Inserts the name of each column from cursor.description
    # Example output:
    # desc = (('username', 253, None, 1020, 1020, 0, True), ('password', 253, None, 1020, 1020, 0, True))
    administrators = [dict(zip([col[0] for col in desc], row)) for row in output]
    # Organizes the values obtained by the "output" and pass it to "administrators" as a list
    NumAccounts = 0
    for administrator in administrators:
        NumAccounts += 1
        print("ACCOUNT {0}:".format(NumAccounts))
        print("{0}: '{1}'".format(desc[0][0], administrator[desc[0][0]]))
        print("{0}: '{1}'\n".format(desc[1][0], administrator[desc[1][0]]))
    return
