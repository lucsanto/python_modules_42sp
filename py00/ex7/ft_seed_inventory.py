def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
	seedMap = {
		"packets": "packets available",
		"grams": "grams total",
		"area": "square meters"
	}
	print(f'{seed_type.capitalize()} seeds: {quantity} {seedMap[unit]}')

ft_seed_inventory("lettuce", 12, "area")
