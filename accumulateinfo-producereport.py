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
    print(f'Average of {average: 0.1f} hours over {total_days} days')

info_over_time()

#Hours programming: 4
#Hours programming: 8
#Hours programming: 3
#Hours programming: 
#Average of  5.0 hours over 3 days