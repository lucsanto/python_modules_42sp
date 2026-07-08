def	ft_count_harvest_iterative():
	total_days = int(input('Days until harvest: '))
	remaining_days = range(1, (total_days + 1))

	for n in remaining_days:
		print('Day', n)
	print('Harvest time!')
