# time = int(input())
# print(f'{int(time / 60)} \n{int(time % 60)}')

minutes_to_sleep = int(input())
hours = int(input())
minutes = int(input())

hours_to_wake_up = int(minutes_to_sleep / 60 + hours)
minutes_to_wake_up = int(minutes_to_sleep % 60 + minutes)
if minutes_to_wake_up > 60:
	hours_to_wake_up += 1
	minutes_to_wake_up %= 60
print(f'{hours_to_wake_up} \n{minutes_to_wake_up}')
