def info_over_time():
    total_days = 0
    total_hours = 0
    while True:
        daily = input('Hours programming: ')
        if not daily:
            break
        total_days += 1
        total_hours += float(daily)
        average = total_hours/total_days
    print(f'Average of {total_hours: 0.1f} hours over {total_days} days')

info_over_time()

#Hours programming: 7
#Hours programming: 9
#Hours programming: 5
#Hours programming: 
#Average of  21.0 hours over 3 days