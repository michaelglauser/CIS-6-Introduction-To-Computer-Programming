
# 4.17 LAB: Seasons

# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

# Ex: If the input is:

# April
# 11

# the output is:

# Spring

# In addition, check if the string and int are valid (an actual month and day).

# Ex: If the input is:

# Blue
# 65

# the output is:

# Invalid 

# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19


month=input()   #input month
day=int(input())  #input day

if ((month == 'March') and (day >=20   and day<=31)) or ((month == 'April') and (day >=1  and day<=30))  or ((month == 'May') and (day >=1  and day<=31))  or ((month == 'June') and (day>=1 and day<21)) :
	season = 'Spring'  #set season ='Spring'

elif ((month == 'June') and (day >=21   and day<=30)) or ((month == 'July') and (day >=1  and day<=31))  or ((month == 'August') and (day >=1  and day<=31))  or ((month == 'September') and (day>=1 and day<22)) :
	season = 'Summer'   #set season ='Summer'

elif ((month == 'September') and (day >=22   and day<=30)) or ((month == 'October') and (day >=1  and day<=31))  or ((month == 'November') and (day >=1  and day<=30))  or ((month == 'December') and (day>=1 and day<21)) :
	season = 'Autumn'   #set season ='Autumn'

elif ((month == 'December') and (day >=21   and day<=31)) or ((month == 'January') and (day >=1  and day<=31))  or ((month == 'February') and (day >=1  and day<=28))  or ((month == 'March') and (day>=1 and day<20)) :
	season = 'Winter'  #set season ='Winter'
else: #else
    season='Invalid' #set season='Invalid'
print(season)  #print season