print("There are only 2 pieces on a chess board: King and Knight")
print("If the king is able to capture the knight, the program will print: King")
print("If the knight is able to capture the king, the program will print: Knight")
print()
print("NOTE: Input Positions in Capital letters")
print()

letter_board = ["A", "B", "C", "D", "E", "F", "G", "H"]
number_board = ["1", "2", "3", "4", "5", "6", "7", "8"]

knight_letter = input("Enter knight_letter: ")
knight_number = input("Enter knight_number: ")
knight_letter_val = letter_board.index(knight_letter)
knight_number_val = number_board.index(knight_number)

king_letter = input("Enter king_letter: ")
king_number = input("Enter king_number: ")
king_letter_val = letter_board.index(king_letter)
king_number_val = number_board.index(king_number)


if (knight_letter_val == (king_letter_val - 1)) or (knight_letter_val == (king_letter_val + 1)) or (knight_letter_val == king_letter_val):
    if (knight_number_val == (king_number_val - 1)) or (knight_number_val == (king_number_val + 1)) or (knight_number_val == king_number_val):
        print("King")
        
if (king_letter_val == (knight_letter_val -2)) and (king_number_val == (knight_number_val + 1)) or (king_letter_val == (knight_letter_val +2)) and (king_number_val == (knight_number_val + 1)) or (king_letter_val == (knight_letter_val -2)) and (king_number_val == (knight_number_val - 1)) or (king_letter_val == (knight_letter_val +2)) and (king_number_val == (knight_number_val - 1)) or (king_letter_val == (knight_letter_val - 1)) and (king_number_val == (knight_number_val - 2)) or (king_letter_val == (knight_letter_val -1)) and (king_number_val == (knight_number_val + 2)) or (king_letter_val == (knight_letter_val + 1)) and (king_number_val == (knight_number_val -2)) or (king_letter_val == (knight_letter_val +1)) and (king_number_val == (knight_number_val + 2)):
    print("Knight")

else:
    print("Neither")
