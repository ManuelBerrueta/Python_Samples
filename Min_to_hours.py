str_sec_input = input("How many total seconds?")
sec_input = int(str_sec_input)
total_secs = sec_input 
hours = total_secs // 3600 #3600 Seconds in an hours
secs_remaining = total_secs % 3600 #Defined the leftover seconds from division
minutes = secs_remaining // 60
secs_after_min = secs_remaining % 60
print("Hours:", hours, "Minutes:", minutes, "Seconds:", secs_after_min)

