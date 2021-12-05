data = open('day5_data.txt','r')

data_lines = data.readlines()
##print(len(data_lines))

coords = {}

coords_straight = {}

def clean_lines(line):
    c1, c2 = line.split(' -> ')
    
    x1, y1 = c1.split(',')
    x2, y2 = c2.split(',')
    return int(x1), int(y1), int(x2), int(y2)

def get_range(v1, v2):
    if v1 <= v2:
        v_range = range(v1, v2 + 1)
    elif v1 > v2:
        v_range = range(v1, v2 - 1, -1)
    return v_range

def add_coord(x, y, coord_dict):
    if (x, y) in coord_dict:
        coord_dict[(x, y)] += 1
    else:
        coord_dict[(x, y)] = 1
    return

for line in data_lines:
    x1, y1, x2, y2 = clean_lines(line[:-1])
    x_range = get_range(x1, x2)
    y_range = get_range(y1, y2)

    count_steps = 0
    if len(x_range) > 1 and len(y_range) > 1:
         for i in range(len(x_range)):
            count_steps += 1
            if x_range[0] < x_range[-1] and y_range[0] < y_range[-1]:
                add_coord(x1+i, y1+i, coords)
            elif x_range[0] < x_range[-1] and y_range[0] > y_range[-1]:
                add_coord(x1+i, y1-i, coords)
            elif x_range[0] > x_range[-1] and y_range[0] < y_range[-1]:
                add_coord(x1-i, y1+i, coords)
            elif x_range[0] > x_range[-1] and y_range[0] > y_range[-1]:
                add_coord(x1-i, y1-i, coords)
        
    else:
        for x in x_range:
            for y in y_range:
                count_steps += 1
                add_coord(x, y, coords)
                add_coord(x, y, coords_straight)
                
count_straight_points = 0
for coord in coords_straight:
    if coords_straight[coord] > 1:
        count_straight_points += 1

print('Part 1:')
print(f'Line Intersects (straights only): {count_straight_points}')

count_points = 0
for coord in coords:
    if coords[coord] > 1:
        count_points += 1

print('Part 2:')
print(f'Line Intersects w/diagonals: {count_points}')
