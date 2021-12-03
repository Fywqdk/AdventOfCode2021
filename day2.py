data = open('day2_data.txt','r')

data_lines = data.readlines()

total_up = 0
total_down = 0
total_forward = 0
aim = 0
depth = 0

for line in data_lines:
  direction, dist = line.split()

  dist = int(dist)
  if direction == 'up':
    total_up += dist
    aim -= dist
  elif direction == 'down':
    total_down += dist
    aim += dist
  elif direction == 'forward':
    total_forward += dist
    depth += aim*dist



total_depth = total_down - total_up

print('Part one:')
print(f'Forward: {total_forward}')
print(f'Depth {total_depth}')
print(f'Result {total_forward * total_depth}')
print('')
print('Part two:')
print(f'Forward: {total_forward}')
print(f'Depth {depth}')
print(f'Result {total_forward * depth}')

