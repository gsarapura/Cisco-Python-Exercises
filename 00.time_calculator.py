# Calculate the time your event finishes.
# 24-hour format


hour = int(input("Starting hour (24-hour format): "))
min = int(input("Starting minute: "))
duration_hour = int(input("Hours of the event's duration: "))
duration_min = int(input("Minutes of the event's duration: "))


hour_to_min = hour * 60
duration_hour_to_min = duration_hour * 60

total_min = min + hour_to_min + duration_hour_to_min + duration_min

new_hour = (total_min // 60) % 24
new_min = total_min % 60

print(new_hour, str(new_min).zfill(2), sep=":")
