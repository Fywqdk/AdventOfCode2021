import day7_data as data


#step 1
fuel_sum = []
fuel_dict = {}
fuel_dict[0] = 0

for i in range(1,max(data.crabs)+1):
  fuel_dict[i] = i + fuel_dict[i-1]

for i in range(max(data.crabs)):
  point_fuel = 0
  for crab in data.crabs:
    point_fuel += abs(crab-i)
  
  fuel_sum.append(point_fuel)

print(f'Step 1 minimum fuel: {min(fuel_sum)}')

#step 2
fuel_sum2 = []

for i in range(max(data.crabs)):
  point_fuel = 0
  for crab in data.crabs:
    point_fuel += fuel_dict[abs(crab-i)]

  
  fuel_sum2.append(point_fuel)

print(f'Step 2 minimum fuel: {min(fuel_sum2)}')

