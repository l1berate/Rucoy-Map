from PIL import Image
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import time
from random import randint

'''
for f in range(1, 6):
	image = Image.open(fr'{f}.png')
	validCoordinates = []
	width, height = image.size
	coord = x, y = 0, 0
	coord_matrix = []
	for _ in range(height):
		width_list = [0]*width
		coord_matrix.append(width_list) 
	for y in range(height):
		for x in range(width):
			#if pixel is not white add to valid coordinates list
			if (image.getpixel((x,y)) == (34, 177, 76, 255)):
				validCoordinates.append(f'{x},{649-y}')
				coord_matrix[649-y][x] = 1
	with open(fr'{f}m.txt', mode="w") as outfile:
		for coord in coord_matrix:
			j = str(coord).replace('[', '').replace(' ', '').replace(']', '')
			outfile.write(f"{j}\n")
'''

start_time = time.time()
#grid = Grid(matrix=coord_matrix)
'''
with open('1m.txt', 'r') as f:
	matrix_1 = [[int(num) for num in line.split(',')] for line in f]
	grid = Grid(matrix=matrix_1)
'''

coord_matrix = []
for _ in range(20):
	width_list = [1]*40
	coord_matrix.append(width_list) 

grid = Grid(matrix=coord_matrix)

end_time = time.time()
print('grid made in {:.4} seconds'.format(end_time-start_time))

for a in range(20):
	b = randint(0, 39)
	coord_matrix[a][b] = 0

# x: 213, y: 218, mx: 224, my: 224
'''
Bot    >>> path: [(213, 218), (212, 218), (211, 218), (210, 218), (209, 218)] runs: 5
Bot    >>> x: 213, y: 218, mx: 213, my: 221
Bot    >>> path: [] runs: 1
Bot    >>> x: 213, y: 218, mx: 209, my: 226
Bot    >>> path: [] runs: 1
Bot    >>> x: 213, y: 218, mx: 217, my: 223
Bot    >>> path: [] runs: 1
Bot    >>> x: 213, y: 218, mx: 224, my: 224
Bot    >>> path: [] runs: 1
Bot    >>> x: 213, y: 218, mx: 209, my: 218
'''
start_time = time.time()

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

x = 20
y = 10
start = grid.node(x,y)
end = grid.node(5,2)
path, runs = finder.find_path(start, end, grid)
print(f'operations: {runs} , path length: {len(path)}')
grid.cleanup()
start = grid.node(x,y)
end = grid.node(35,19)
path, runs = finder.find_path(start, end, grid)
print(f'operations: {runs} , path length: {len(path)}')
grid.cleanup()
start = grid.node(x,y)
end = grid.node(21,14)
path, runs = finder.find_path(start, end, grid)
print(f'operations: {runs} , path length: {len(path)}')
grid.cleanup()
start = grid.node(x,y)
end = grid.node(30,2)
path, runs = finder.find_path(start, end, grid)
print(f'operations: {runs} , path length: {len(path)}')

end_time = time.time()

#print(grid.grid_str(path=path, start=start, end=end))
print('path found in {:.4} seconds'.format(end_time-start_time))

start_time = time.time()
grid.cleanup()
end_time = time.time()
print('grid cleaned up in {:.4} seconds'.format(end_time-start_time))



'''
image2 = Image.open(r'path.png')
px = image2.load() 

for coord in path:
	x, y = coord
	px[x,649-y] = (3, 244, 252, 255)

px[153,649-365] = (3, 11, 252, 255)
px[167,649-361] = (3, 11, 252, 255)


image2.save('path.png')
'''