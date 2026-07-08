def counter(day: int):
	if day == 0:
		print('Harvest time!')
		return
	print('Day', day)
	counter(day - 1)

def ft_count_harvest_recursive():
	counter(int(input('Days until harvest: ')))
