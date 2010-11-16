from datetime import date
from datetime import timedelta
 
startDate = date(1901, 1, 1)  # year, month, day
endDate = date(2000, 12, 31)  # year, month, day

dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

count=0;
while (startDate != endDate):
	if (date.weekday(startDate) == 6 and startDate.day == 1):
		count += 1;
		print (date.weekday(startDate),  startDate.day)
		print("The day of the week on %s was a %s" % (startDate.strftime("%d%b%Y"), dayofWeek[date.weekday(startDate)]))

	startDate = startDate + timedelta(days=1)

print(count);