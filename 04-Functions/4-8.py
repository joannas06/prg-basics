def time_string(hours, minutes, time_format):
    #for 24 hour format
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    
    #for 12-hour format
    elif time_format == '12':
        # Determine AM or PM
        suffix = "am" if hours < 12 else "pm"
        
        # Convert 24h to 12h using modulo
        # 13 % 12 becomes 1. 
        # 0 % 12 is 0, so we manually change that to 12 for midnight.
        display_hour = hours % 12
        if display_hour == 0:
            display_hour = 12
            
        return f"{display_hour}:{minutes:02}{suffix}"

# --- Testing the program ---
print(f"1. {time_string(15, 38, '24')}")   # Expected: 15:38
print(f"2. {time_string(8, 3, '24')}")     # Expected: 08:03
print(f"3. {time_string(0, 5, '24')}")     # Expected: 00:05
print(f"4. {time_string(11, 15, '12')}")   # Expected: 11:15am
print(f"5. {time_string(0, 7, '12')}")     # Expected: 12:07am
print(f"6. {time_string(7, 30, '12')}")    # Expected: 7:30am
print(f"7. {time_string(12, 46, '12')}")   # Expected: 12:46pm
print(f"8. {time_string(13, 10, '12')}")   # Expected: 1:10pm
print(f"9. {time_string(19, 2, '12')}")    # Expected: 7:02pm
    