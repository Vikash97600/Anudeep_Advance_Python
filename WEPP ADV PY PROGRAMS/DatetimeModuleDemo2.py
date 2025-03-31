from datetime import datetime

currentTime=datetime.now()
currentHour=currentTime.hour

if 1<=currentHour<12:
    greet="Good Morning"
elif 12<=currentHour<18:
    greet="Good Afternoon"
else:
    greet="Good Evening"

print(f"{greet}! The current time is : {currentTime.strftime('%H:%M')}")
 