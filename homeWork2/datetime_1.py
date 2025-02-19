import datetime

# convert string to datetime
date_str = "2024-12-15"
date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_dt)  
