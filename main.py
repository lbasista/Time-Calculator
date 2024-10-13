def add_time(start, duration, day=None):
    week_days = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    #Starting time in separate variables
    start_time = start.split(" ")[0]
    start_hour = int(start_time.split(":")[0])
    start_min = int(start_time.split(":")[1])

    day_part = start.split(" ")[1]

    #Duration in separate variables
    duration_hour = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])

    #Change time format to 24h
    if day_part == "PM":
        start_hour += 12

    #Final time at 0:00
    fin_h = 0
    fin_min = 0

    #Today is day 0
    fin_day = 0

    #Adding minutes
    fin_min = start_min + duration_min
    if fin_min >= 60:
        fin_min -= 60
        fin_h += 1

    #Adding hours
    fin_h += start_hour + duration_hour
    while fin_h >= 24:
        fin_h -= 24
        fin_day += 1

    #AM or PM?
    if fin_h == 0:
        fin_h = 12
        fin_dp = "AM"
    elif fin_h == 12:
        fin_dp = "PM"
    elif fin_h > 12:
        fin_h -= 12
        fin_dp = "PM"
    else:
        fin_dp = "AM"


    #Message to output
    message = str(fin_h) + ":" + str(fin_min).zfill(2) + " " + fin_dp

    #Day of the week
    if day == None:
        if fin_day == 0:
            return message
        elif fin_day == 1:
            return message + " (next day)"
        else:
            return message + " (" + str(fin_day) + " days later)"
    else:
        start_day = day.lower().capitalize()
        start_day = week_days[start_day]
        fin_day_week = (start_day + fin_day) % 7
        if fin_day_week == 0:
            fin_day_week = 7

        #Reverse dictionary with days
        rev_week_days = {d: n for n, d in week_days.items()}

        #output
        message += ", " + str(rev_week_days[fin_day_week])
        if fin_day == 0:
            return message
        elif fin_day == 1:
            return message + " (next day)"
        else:
            return message + " (" + str(fin_day) + " days later)"

def main():
    print(add_time("3:30 PM", "2:12"))
    print(add_time("3:30 PM", "2:12", "Monday"))
    print(add_time("11:30 AM", "2:30", "Friday"))
    print(add_time("11:30 AM", "0:30", "Monday"))
    print(add_time("11:30 AM", "0:30", "Sunday"))
    print(add_time("3:30 PM", "2:12", "Saturday"))
    print(add_time("10:10 PM", "3:30", "Tuesday"))
    print(add_time("12:00 PM", "12:00"))
    print(add_time("11:59 PM", "24:05"))

# Uruchom program
if __name__ == "__main__":
    main()