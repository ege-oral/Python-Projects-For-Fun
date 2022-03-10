
'''
Hangman Game With Python.
We need a wide console window for this game.
'''
def mistakes(play_area, mistake_count):
    if mistake_count == 1:
        play_area[20][3] = "_"
        play_area[20][4] = "_"
        play_area[20][5] = "_"
        play_area[20][6] = "_"
        play_area[20][7] = "_"

    elif mistake_count == 2:
        play_area[19][5] = "|"
        play_area[18][5] = "|"
        play_area[17][5] = "|"
        play_area[16][5] = "|"
        play_area[15][5] = "|"

    elif mistake_count == 3:
        play_area[14][5] = "|"
        play_area[13][5] = "|"
        play_area[12][5] = "|"
        play_area[11][5] = "|"
        play_area[10][5] = "|"
        
    elif mistake_count == 4:
        play_area[9][5] = "|"
        play_area[8][5] = "|"
        play_area[7][5] = "|"
        play_area[6][5] = "|"
        play_area[5][5] = "|"

    elif mistake_count == 5:
        play_area[4][5] = "|"
        play_area[3][5] = "|"
        play_area[2][5] = "|"
        play_area[1][5] = "|"
        play_area[0][5] = "/"

    elif mistake_count == 6:
        play_area[0][6] = chr(8254)
        play_area[0][7] = chr(8254)
        play_area[0][8] = chr(8254)
        play_area[0][9] = chr(8254)
        play_area[0][10] = chr(8254)

    elif mistake_count == 7:
        play_area[1][10] = "|"
        play_area[2][10] = "|"
        play_area[3][10] = "|"
        play_area[4][10] = "|"
        play_area[5][10] = "|"

    elif mistake_count == 8:
        play_area[6][10] = "1"
        play_area[7][9] = "1"
        play_area[8][10] = "1"
        play_area[7][11] = "1"

    elif mistake_count == 9:
        play_area[9][10] = "|"
        play_area[10][10] = "|"
        play_area[11][10] = "|"
        play_area[12][10] = "|"
        play_area[13][10] = "|"
    
    elif mistake_count == 10:     
        play_area[10][9] = "1"
        play_area[11][8] = "1"

    elif mistake_count == 11:
        play_area[10][11] = "1"
        play_area[11][12] = "1"

    
    elif mistake_count == 12:
        play_area[14][9] = "1"
        play_area[15][8] = "1"

    elif mistake_count == 13:
        play_area[14][11] = "1"
        play_area[15][12] = "1"


row, collum = 21, 20
play_area = [[" " for x in range(collum)] for y in range(row)]
word = input("Please enter a word: ")
word_list = [x for x in word]
word_matrix = ["_" for x in range(len(word))]
mistake_count = 0
while True:
    player_guess = input("Please enter a single character: ")
    if player_guess == "exit":
        print("EXITING.")
        break
    else:
        player_guess = player_guess[0]

    res = [i for i in range(len(word)) if word.startswith(player_guess, i)]
    
    if res:
        for index in res:
            word_matrix[index] = player_guess
            word = word.replace(player_guess, "0")
        if "_" not in word_matrix:
            print(word_matrix)
            print(*play_area, sep="\n")
            print("You WINN")
            break

    else:
        mistake_count += 1
        mistakes(play_area, mistake_count)
        if mistake_count == 13:
            print(word_matrix)
            print(*play_area, sep="\n")
            print("YOU LOSE")
            break
    print("WORD: ", end=' ')
    print(*word_matrix)
    print(*play_area, sep="\n")