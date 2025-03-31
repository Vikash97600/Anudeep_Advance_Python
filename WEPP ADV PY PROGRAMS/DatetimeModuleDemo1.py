from datetime import datetime
def calculateDays():
    date1_str=input("Enter the first date (YYYY-MM-DD):")
    date2_str=input("Enter the second date (YYYY-MM-DD):")

    try:
        date1=datetime.strptime(date1_str,"%Y-%m-%d")
        date2=datetime.strptime(date2_str,"%Y-%m-%d")
        
        diff=abs(date2-date1)
        print(f"Number of days between {date1_str} and {date2_str} is {diff.days} days.")

    except ValueError:
        print("Invalid date format! Please use the formate like YYYY-MM-DD ")

calculateDays()