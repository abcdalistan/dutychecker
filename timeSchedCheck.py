from datetime import datetime
<<<<<<< HEAD

flag = True
index = 0

# Input schedules (automatic logout)
schedules = ["06:38:40", "06:38:45"]
=======
import pymysql
>>>>>>> 8cd1b149fe2f7066ff3669de9cc00978a0378c11

def stringToList(string):
    tempList = string.rsplit(":")
    for i in range(0, len(tempList)):
        tempList[i] = int(tempList[i])
    return tempList

def checkTime(time1, time2):
    time1 = stringToList(time1)
    time2 = stringToList(time2)
    if time1[0] > time2[0]:
        return True
    elif time1[0] == time2[0]:
        if time1[1] > time2[1]:
            return True
        elif time1[1] == time2[1]:
            if time1[2] > time2[2]:
                return True
<<<<<<< HEAD

while flag:
    time = datetime.now()
    now = time.strftime("%H:%M:%S")
    if checkTime(now, schedules[index]):
        print("Time's up! {0}".format(schedules[index]))
        if index < len(schedules)-1:
            index += 1
        else:
            flag = False
=======
            else:
                return False
        else:
            return False
    else:
        return False

class staffer:
    
    def __init__(self, stafferID, schedules):
        self.stafferID = stafferID
        self.schedules = schedules
        self.schedTime = 1
        self.index = 0
        self.status = "In Duty"
        self.loggedIn = False
        self.logTime = []
        #self.getSchedule()
        
    def getSchedule(self):
        conn = pymysql.connect("localhost", "root", "", "staffer")
        with conn:
            cursor = conn.cursor()
            query = "SELECT start_time, end_time FROM schedules WHERE student_number = '{0}'".format(self.stafferID)
            cursor.execute(query)
            conn.commit()
            result = cursor.fetchall()
            for time in result:
                self.schedules[(datetime.min + time[0]).time().strftime("%H:%M:%S")] = (datetime.min + time[1]).time().strftime("%H:%M:%S")
            cursor.close()
        return None

    def checkStatus(self):
        if self.loggedIn:
            if self.status == "In Duty":
                return True
            else:
                self.loggedIn = False
                return False
        else:
            return False
    
##    def checkStatus(self):
##        conn = pymysql.connect("localhost", "root", "", "staffer")
##        with conn:
##            cursor = conn.cursor()
##            query = "SELECT status FROM loginstaff WHERE student_number  = '{0}'".format(self.stafferID)
##            cursor.execute(query)
##            conn.commit()
##            status = cursor.fetchone()[0]
##            if status == "In duty":
##                return True
##            else:
##                return False
##            cursor.close()
##        return None

    def logOut(self):
        time = datetime.now()
        now = time.strftime("%H:%M:%S")
        conn = pymysql.connect("localhost", "root", "", "staffer")
        with conn:
            cursor = conn.cursor()
            query = "UPDATE loginstaff SET logout_time = '{0}' WHERE student_number = '{1}'".format(now, self.stafferID)
            cursor.execute(query)
            conn.commit()
            cursor.close()
        return None

    def changeStatus(self, status):
        self.status = status

##    def changeStatus(self, status):
##        conn = pymysql.connect("localhost", "root", "", "staffer")
##        with conn:
##            cursor = conn.cursor()
##            query = "UPDATE loginstaff SET status = '{0}' WHERE student_number = '{1}'".format(status, self.stafferID)
##            cursor.execute(query)
##            conn.commit()
##            cursor.close()
##        return None

    def logoutCheckTime(self, time):
        now = time.strftime("%H:%M:%S")
        keys = list(self.schedules.keys())
        
        if checkTime(now, self.schedules[keys[self.index]]):
            if self.checkStatus():
                self.changeStatus('Off duty')
                self.loggedIn = False
                logTime = self.logTime[self.index].rsplit(":")
                logTime[2] = str(int(logTime[2])-1).zfill(2)
                if checkTime (":".join(logTime), self.schedules[keys[self.index]]):
                    print("FINE +1", self.logTime[self.index], self.schedules[keys[self.index]])
                print(self.stafferID, "logged out:", self.logTime)
                if self.index < len(self.schedules)-1:
                    self.index += 1
            else:
                return
        else:
            return
            
Anazel = staffer ("1810972", {"08:31:00": "06:40:39", "02:00:00": "06:41:30"})
#Zeus = staffer ("1812975", {"10:00:00": "5:08:10", "10:30:00": "05:08:15"})
t = True
t1 = True
while True:
    time = datetime.now()
    Anazel.logoutCheckTime(time)
    
    if checkTime(time.strftime("%H:%M:%S"), "06:39:00"):
        if t:
            Anazel.loggedIn = True
            Anazel.status = "In Duty"
            Anazel.logTime.append("06:31:45")#time.strftime("%H:%M:%S"))
            print(Anazel.status)
            t = False
            
    if checkTime(time.strftime("%H:%M:%S"), "06:41:25"):
        if t1:
            Anazel.loggedIn = True
            Anazel.status = "In Duty"
            Anazel.logTime.append(time.strftime("%H:%M:%S"))
            print(Anazel.status)
            t1 = False
    #Zeus.logoutCheckTime(time)
>>>>>>> 8cd1b149fe2f7066ff3669de9cc00978a0378c11

input("")
