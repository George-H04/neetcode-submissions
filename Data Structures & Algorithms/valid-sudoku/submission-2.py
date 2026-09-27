class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = len(board)
        # Handle rows
        for row in board:
            digits = [x for x in row if x.isdigit()]

            unique = set(digits)

            if len(digits) != len(unique):
                return False

        # Handle columns
        for i in range(BOARD_SIZE):
            col = []
            for row in board:
                col.append(row[i])
            
            digits = [x for x in col if x.isdigit()]

            unique = set(digits)

            if len(digits) != len(unique):
                return False
            

        # Handle 3 x 3 boxes | sliding window approach
        BOX_SIZE = 3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [row[box_row:box_row+3] for row in board[box_col:box_col+3]]
                print(box)

                empty = sum(row.count(".") for row in box)

                if empty == BOARD_SIZE:
                    continue

                occupied = {x for row in box for x in row}  # Also contains the element "."

                if len(occupied) == BOARD_SIZE:
                    continue

                total_size = empty + len(occupied) - 1
                
                # One of the rows contains a duplicate value
                if total_size != BOARD_SIZE:
                    print("Failed at boxes")
                    return False


        return True