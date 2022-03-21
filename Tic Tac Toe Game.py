'''
Tic Tac Toe Game With Python.
We need a wide console window for this game.
'''
def main():
    play_area = [["1", "2", "3"],
			     ["4", "5", "6"],
			     ["7", "8", "9"]]

    player_1_symbol = ""
    player_2_symbol= ""
    turn = 0
    while True:
        player_1_symbol = input("What do you want to be X or O ?: ").upper()
        if player_1_symbol == "X" or player_1_symbol == "O":
            if player_1_symbol == "X":
                player_2_symbol = "O"
            else:
                player_2_symbol = "X"
        
            print(f"Player 1 is '{player_1_symbol}' and Player 2 is '{player_2_symbol}'.\n")
            break
        else:
            print("Please enter 'X' or 'O'.\n")
            continue

    while True:
        symbol = ""
        if turn == 1:
            symbol = player_2_symbol
            turn = 2
        else:
            symbol = player_1_symbol
            turn = 1
        while True:
            print(f"Player {turn}({symbol}) Turn.\n")
            DrawPlayeArea(play_area)
            player_area_choice = int(input("Please select an area: "))
            print("\n")
            if AreaChoice(play_area, player_area_choice, symbol) == 1:
                break
            else:
                continue

        if CheckIfWin(play_area, symbol):
            DrawPlayeArea(play_area)
            if player_1_symbol == symbol:
                print(f"Player 1({symbol}) WINS!!!")
            else:
                print(f"Player 2({symbol}) WINS!!!")
            break




def DrawPlayeArea(play_area):
    for i in range(len(play_area)):
        print(*play_area[i], sep=' | ')
        if i != len(play_area) - 1:
            print("--+---+--")

def AreaChoice(play_area, player_area_choice, symbol):
	if player_area_choice == 1 and (play_area[0][0] != 'X' and play_area[0][0] != 'O'):
		play_area[0][0] = symbol

	elif player_area_choice == 2 and (play_area[0][1] != 'X' and play_area[0][1] != 'O'):
		play_area[0][1] = symbol

	elif player_area_choice == 3 and (play_area[0][2] != 'X' and play_area[0][2] != 'O'):
		play_area[0][2] = symbol

	elif player_area_choice == 4 and (play_area[1][0] != 'X' and play_area[1][0] != 'O'):
		play_area[1][0] = symbol
        
	elif player_area_choice == 5 and (play_area[1][1] != 'X' and play_area[1][1] != 'O'):
		play_area[1][1] = symbol

	elif player_area_choice == 6 and (play_area[1][2] != 'X' and play_area[1][2] != 'O'):
		play_area[1][2] = symbol

	elif player_area_choice == 7 and (play_area[2][0] != 'X' and play_area[2][0] != 'O'):
		play_area[2][0] = symbol

	elif player_area_choice == 8 and (play_area[2][1] != 'X' and play_area[2][1] != 'O'):
		play_area[2][1] = symbol

	elif player_area_choice == 9 and (play_area[2][2] != 'X' and play_area[2][2] != 'O'):
		play_area[2][2] = symbol
	else:
		print("Can't do that. Please select another area.")
		return False
	return True

def CheckIfWin(play_area, symbol):
	# ROWS
	if play_area[0][0] == symbol and play_area[0][1] == symbol and play_area[0][2] == symbol:
		return True
	elif play_area[1][0] == symbol and play_area[1][1] == symbol and play_area[1][2] == symbol:
		return True
	elif play_area[2][0] == symbol and play_area[2][1] == symbol and play_area[2][2] == symbol:
		return True

	# COLLUMS
	elif play_area[0][0] == symbol and play_area[1][0] == symbol and play_area[2][0] == symbol:
		return True
	elif play_area[0][1] == symbol and play_area[1][1] == symbol and play_area[2][1] == symbol:
		return True
	elif play_area[0][2] == symbol and play_area[1][2] == symbol and play_area[2][2] == symbol:
		return True

	# DIAGONALS
	elif play_area[0][0] == symbol and play_area[1][1] == symbol and play_area[2][2] == symbol:
		return True
	elif play_area[2][0] == symbol and play_area[1][1] == symbol and play_area[0][2] == symbol:
		return True
	
	else:
		return False

main()
