bingo_numbers = (68,30,65,69,5,78,41,73,55,0,76,98,
                 79,42,37,21,9,34,56,33,64,54,24,43,15,58,
                 61,38,12,20,4,26,87,95,94,89,83,74,97,77,
                 67,40,63,88,19,31,81,80,60,14,18,47,93,57,
                 17,90,84,85,48,6,91,7,86,13,51,53,8,16,23,
                 66,36,39,32,82,72,11,52,28,62,70,59,50,1,
                 46,96,71,35,10,25,22,27,99,29,45,44,3,75,
                 92,49,2)



data = open('day4_data.txt','r')

data_lines = data.readlines()

boards = []
board = []
for line in data_lines:
    if len(line) > 1:
        row = list(line.split())
        row = [int(x) for x in row]
        board.append(tuple(row))
    else:
        boards.append(tuple(board))
        board = []
        
def check_board(board, numbers):
    rows = list(board)
    cols = []
    col = []
    for i in range(5):
        for row in rows:
            col.append(row[i])
        cols.append(tuple(col))
        col = []

    bingo = False
    for row in rows:
        bingo = True
        for val in row:
            if val not in numbers:
                bingo = False

        if bingo == True:
            return True
    
    bingo = False
    for col in cols:
        bingo = True
        for val in col:
            if val not in numbers:
                bingo = False

        if bingo == True:
            return True

    return False



def board_score(board, numbers):
    rows = list(board)
    score = 0
    marked = []
    unmarked = []

    for row in rows:
        for val in row:
            if val not in numbers:
                score += val
                marked.append(val)
            else:
                unmarked.append(val)
                
    return score, marked, unmarked

    
pulled_numbers = []
bingoed_boards = []
bingoed_scores = []
for number in bingo_numbers:

#    print(f'Number: {number}... ')

    pulled_numbers.append(number)
    for board in boards:
        if not board in bingoed_boards:
            
            bingo = check_board(board, pulled_numbers)

            if bingo:
                bingoed_boards.append(board)
                bingoed_scores.append(tuple(pulled_numbers))



            

if len(bingoed_boards) > 0:
    winner_board, winner_pulled = bingoed_boards[0], bingoed_scores[0]
    winner_number = winner_pulled[-1]
    last_board, last_pulled = bingoed_boards[-1], bingoed_scores[-1]
    last_number = last_pulled[-1]

    print(f'Board {boards.index(winner_board)} wins!')

    winner_score, winner_unmarked, winner_marked = board_score(winner_board, winner_pulled)
    
    print(f'Unmarked score: {winner_score}')
    print(f'Bingo number: {winner_number}')
    print(f'Final score: {winner_number*winner_score}')

    print('')
    print(f'Last board to win:{boards.index(last_board)}')

 
    last_score, last_unmarked, last_marked = board_score(last_board, last_pulled)
    
    print(f'Unmarked score: {last_score}')
    print(f'Bingo number: {last_number}')
    print(f'Final score: {last_number*last_score}')
    
if not bingo:
    print('No bingos!')
            
