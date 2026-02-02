#write a pthon program to print calender of a given year and month
import calendar
year= int(input("enter year:"))
month= int(input("enter month"))
cal=calendar.month(year,month)
print(cal)
