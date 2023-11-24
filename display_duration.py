def display_duration():
    end_time = datetime.now()
    duration = end_time - start_time
    minutes, seconds = divmod(duration.seconds, 60)
    print(f"You've used the system for {minutes} minutes and {seconds} seconds.")
    time.sleep(2)  # delay for 2 seconds

# In your main_menu function:
elif choice == '6' or choice == 'exit':
    display_duration()
    br
