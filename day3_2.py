data = open('day3_data.txt','r')

data_lines = data.readlines()

num_lines = len(data_lines)


line_length = len(data_lines[0][:-1])

def find_oxy_CO2(i, match, lines):
  # Returns lines where the target is found at the index site

  if len(lines) == 1:
    return lines
    
  new_lines = []


  # First find the number of ones at the i position in the lines variable
  count_ones = 0

  for line in lines:
    if int(line[i]) == 1:
      count_ones += 1
    elif int(line[i]) < 3 and match == 'o':
      print(line[:-1], count_ones, len(lines))

  # If ones is less than half the target for oxygen is 0, else its 1
  if count_ones >= len(lines) / 2:

    if match == 'o':
      target = 1
    else:
      target = 0
  else:
    if match == 'o':
      target = 0
    else:
      target = 1

  # Find matches for target and append to new_lines variable
  for line in lines:
    if int(line[i]) == target:
      new_lines.append(line)

  return new_lines

# Set variables
oxy_lines = data_lines.copy()
co2_lines = data_lines.copy()

for i in range(line_length):
  oxy_lines = find_oxy_CO2(i, 'o', oxy_lines)

  co2_lines = find_oxy_CO2(i, 'c', co2_lines)
  print(i, len(oxy_lines), len(co2_lines))

oxy_bin = oxy_lines[0][:-1]
co2_bin = co2_lines[0][:-1]


Oxygen = int(oxy_bin, 2)
CO2 = int(co2_bin, 2)

print('')
print(f'Oxygen: {Oxygen}')
print(f'CO2: {CO2}')
print(f'Life support: {Oxygen * CO2}')