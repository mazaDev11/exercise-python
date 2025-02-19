import datetime

# convert string to datetime
date_str = "2024-12-15"
date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")

# add 7 days to the date
date_dt += datetime.timedelta(days=7)

# format date to string
date_str = date_dt.strftime("%B %d, %Y")
print(date_str) 