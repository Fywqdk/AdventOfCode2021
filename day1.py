data = open('day1_data.txt','r')

data_lines = data.readlines()

last_depth = 0
last_depth2 = 0
last_sum = 0
increases = 0
sum_increases = 0
count = 0
for line in data_lines:
  depth = int(line)
  if last_depth < depth:
    if count > 1:
      increases += 1
  if depth + last_depth + last_depth2 > last_sum:
    if count > 2:
      sum_increases += 1

  last_sum = depth + last_depth + last_depth2
  last_depth2 = last_depth
  last_depth = depth
  count += 1


print(f'Increases: {increases}')
print(f'Sum Increases: {sum_increases}')
