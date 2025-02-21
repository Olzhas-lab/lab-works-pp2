import datetime
#Exercis1----------------------------------------------------
Current_Date = datetime.datetime.now()
New_Date = Current_Date - datetime.timedelta(days=5)
print(New_Date)
#Exercis2----------------------------------------------------
Today = datetime.datetime.now()
Yesterday = Today - datetime.timedelta(days=1)
Tomorrow = Today + datetime.timedelta(days=1)
print("Yesterday",Yesterday)
print("Today",Today)
print("Tomorrow",Tomorrow)
#Exercis3----------------------------------------------------
Current_Date = datetime.datetime.now()
Microseconds = Current_Date.strftime("%f")
print(Microseconds)
#Exercis4`----------------------------------------------------
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")

date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

time_difference = date2 - date1
difference_seconds = abs(time_difference.total_seconds())
print(difference_seconds)
