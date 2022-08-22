seconds = 317567834
minute = 60
minutes = seconds // minute
hour = minutes // 60
day = hour // 24
weeks = day // 7
month = weeks // 4
secover = seconds - minutes * minute
minover = minutes - hour * minute
hover = hour - day * 24
dayover = day - weeks * 7
veckover = weeks - month * 4
print( seconds, "seconds", "equals to", veckover, "weeks", dayover, "days", hover, "hours", minover, "minutes", secover, "seconds")