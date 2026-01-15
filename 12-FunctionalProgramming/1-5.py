def avg_speed(distance,hours,minutes):
    average = distance/(hours+(minutes/60))
    return average

if __name__ == "__main__":
    print(avg_speed(70,1,23))