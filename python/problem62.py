from itertools import count

cube_map = {0:[0]}

for i in count(1):
	sorted_cube = int("".join(sorted(list(str(i**3)), reverse=True)))
	
	if sorted_cube not in cube_map:
		cube_map[sorted_cube] = []

	cube_map[sorted_cube].append(i)

	if len(cube_map[sorted_cube]) == 5:
		print(i**3, cube_map[sorted_cube])
		break

