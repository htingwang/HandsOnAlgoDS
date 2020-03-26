class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            num_row = [v for v in row if v != "."]
            if len(set(num_row)) < len(num_row):
                
                return False

        col_length = len(board[0])
        row_length = len(board)
        for col in range(col_length):
            col_list = []
            for row in range(row_length):
                col_list.append(board[row][col])

            num_col = [v for v in col_list if v != "."]
            if len(set(num_col)) < len(num_col):
                
                return False

        col_start = 0
        result = []
        for index in range(row_length):
            result.append([board[index][0:3], board[index][3:6], board[index][6:9]])
        zip_result = []
        for zip_time in [0, 3, 6]:
            zip_result.extend(zip(result[zip_time], result[zip_time + 1], result[zip_time + 2]))

        for v in zip_result:
            v_result = v[0] + v[1] + v[2]
            v_result = [val for val in v_result if val != "."]
            if len(v_result) > len(set(v_result)):
                
                return False

        return True
