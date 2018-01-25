time = 34

time = time + 20

my_Variable = "<html><head><title>My Favorite Song Right Now</title></head><body><h1>MAROON5 COLD</h1><a href='https://youtu.be/XatXy6ZhKZw?t=" + str(time) + "'>Click Here</a></body></html>"

my_html_file = open("/Users/0SIRIS/Documents/Python Beginning Programs/my_html_file.html", "w")

my_html_file.write(my_Variable)

my_html_file.close()
