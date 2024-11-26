import datetime, bday_messages

today = datetime.date.today() # generates todays date

next_bday = datetime.date(2007, 8, 6) # year, month, date, format

time_diff = today - next_bday

if next_bday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {time_diff} days away!')