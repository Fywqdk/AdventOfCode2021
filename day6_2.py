s_f_a = [3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4]

days = 256

fish_dict = {}
for i in range(9):
  fish_dict[i] = 0

for i in range(len(s_f_a)):
  fish_dict[s_f_a[i]] +=1

for day in range(0,days+1):
  sum_fish = 0
  birthing_fish = int(fish_dict[0])
  for i in range(8):
    fish_dict[i] = int(fish_dict[i+1])
    sum_fish += fish_dict[i]
  
  fish_dict[6] += birthing_fish
  fish_dict[8] = birthing_fish
  sum_fish += birthing_fish

  if day == 80 or day == 256:
    print(f'Day {day}: {sum_fish} fish. ({birthing_fish} new today)')
