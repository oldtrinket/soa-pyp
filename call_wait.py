# get the current time 
# then use a while loop to wait 5 seconds 
# use the while loop to count down each second eg 5 4 3 2 1 0 
# every second print the following string  
# “Your call is important to us. We don’t want to hire anyone else to answer your call, so please hold for 3 seconds” 
# Do not use a wait function – use the now() function 


from datetime import datetime, timedelta

current_time = datetime.now()
target_time = current_time + timedelta(seconds=5)

last_message_time = current_time
while datetime.now() < target_time:
    
    if (datetime.now() - last_message_time).seconds >= 1:
        
        remaining_time = round((target_time - datetime.now()).total_seconds())
        
        seconds_word = "seconds" if remaining_time > 1 else "second"
        
        print(f"Your call is important to us. We don't want to hire anyone else to answer your call, so please hold for {remaining_time} {seconds_word}")
        
        last_message_time = datetime.now()
