import mysql.connector
from mysql.connector import errorcode

class DbConn(object):
    def connect(self):
        try:
            self.db = mysql.connector.connect(user='root',
                                              password='12345',
                                              host='localhost',
                                              database='mydb')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("Connected")
            self.cursor = self.db.cursor()

            query = ('''SELECT Name, Surname, ID 
                     FROM person''')

            self.cursor.execute(query)

            for (name, surname, id) in self.cursor:
                print("{}, {}, {}".format(name, surname, id))

            self.cursor.close()
            self.db.close()

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    db = DbConn()
    db.connect()
    sys.exit(app.exec_())