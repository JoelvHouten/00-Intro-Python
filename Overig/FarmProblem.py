# Farm Problem

def animals(chickens, cows, pigs):
	chickens *= 2
	cows *= 4
	pigs *= 4
	
	total_legs = chickens + cows + pigs
	print(f"Chickens Legs - {chickens}\nCows Legs - {cows}\nPigs Legs - {pigs}\nTotal Legs - {total_legs}")

animals(5,5,2)