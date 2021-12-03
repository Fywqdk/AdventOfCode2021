data = open('day3_data.txt','r')

data_lines = data.readlines()

num_lines = len(data_lines)

sum_lines = [0 for x in range(len(data_lines[0])-1)]

line_length = len(sum_lines)
 
for line in data_lines:
    for i in range(line_length):
      sum_lines[i] += int(list(line)[i])


gamma_rate = ""
epsilon_rate = ""

for val in sum_lines:
  if val > num_lines / 2:
    gamma_rate += '1'
    epsilon_rate += '0'
  else:
    gamma_rate += '0'
    epsilon_rate += '1'


gamma = int(gamma_rate, 2)
epsilon = int(epsilon_rate, 2)


print(f'Gamma: {gamma}')
print(f'Epsilon: {epsilon}')
print(f'Power Consumption: {gamma * epsilon}')