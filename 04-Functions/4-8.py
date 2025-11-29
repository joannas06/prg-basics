def time_string(hours,minutes,time_format):

    if time_format == '12' and hours < 12:
        ampm = 'am'
        hours = hours
    if time_format == '12':
        if hours == 0:
            hours = 12
            ampm = 'am'
        elif hours < 12:
            ampm = 'am'
        elif hours == 12:
            ampm = 'pm'
        else:
            hours = hours - 12
            ampm = 'pm'

    elif time_format == '24' and hours < 9:
        hours =str(hours)
        hours = '0'+hours
        ampm = ''
    else:
        hours = hours
        ampm = ''

    if minutes < 10:
        minutes =str(minutes)
        minutes = '0'+minutes

    return (f'The time is {hours}:{minutes}{ampm}')

if __name__ == '__main__':  
    print(time_string(15, 38, '24'))
    print(time_string(8, 3, '24'))
    print(time_string(0, 5, '24'))
    print(time_string(11, 15, '12'))
    print(time_string(0, 7, '12'))
    print(time_string(13, 10, '12'))

        


