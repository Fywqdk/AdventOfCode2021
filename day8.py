segment_dict = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
    }

data_lines = []
with open('day8_data.txt','r') as f:
    data_lines = f.readlines()

counter = 0
for line in data_lines:
    segments = line.split(' | ')
    output_vals = segments[1].split()
    for val in output_vals:
        if len(val) in [2, 4, 3, 7]:
            counter +=1

print(f'Part 1 result: {counter}')

output_vals = []

for line in data_lines:
    signal_patterns, outputs = line.split(' | ')
    signal_patterns = signal_patterns.split()
    outputs = outputs.split()

    for output in outputs:
        output = sorted(output)

    all_patterns = sorted(signal_patterns + outputs, key=len)

    segment_dict = {}
    letter_dict = {}

    for pattern in all_patterns:
        pattern = sorted(set(pattern))
        
        if len(pattern) == 2:
            segment_dict[1] = pattern
            
        elif len(pattern) == 3:
            segment_dict[7] = pattern
            
        elif len(pattern) == 4:
            segment_dict[4] = pattern
            bd =  [c for c in segment_dict[4] if c not in segment_dict[1]]
            
        elif len(pattern) == 5:
            if segment_dict[1][0] in pattern and segment_dict[1][1] in pattern:
                segment_dict[3] = pattern
            elif bd[0] in pattern and bd[1] in pattern:
                segment_dict[5] = pattern
            else:
                segment_dict[2] = pattern
                
        elif len(pattern) == 6:
            if segment_dict[1][0] in pattern and segment_dict[1][1] in pattern:
                is_nine = True
                for c in segment_dict[4]:
                    if c not in pattern:
                        is_nine = False
                if is_nine:
                    segment_dict[9] = pattern
                else:
                    segment_dict[0] = pattern
            else:
                segment_dict[6] = pattern
            
        elif len(pattern) == 7:
            segment_dict[8] = pattern

    print(outputs, end=': ')
    val = ''
    for output in outputs:
    
        output = sorted(output)
        for number, pattern in segment_dict.items():
            if pattern == output:
                print(number, end='')
                val += str(number)
    output_vals.append(int(val))

    print('')
print(output_vals)
print(sum(output_vals))

##    for letter in segment_dict[7]:
##        if letter not in segment_dict[1]:
##            letter_dict['a'] = letter





    

    
            
    

    
