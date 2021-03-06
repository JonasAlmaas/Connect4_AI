from .board_manager import BoardManager


class EvaluationManager:
    def evaluate_board(self, board_manager: BoardManager, team):
        score = 0
        matrix = board_manager.matrix
        self.winning_count = board_manager.logic_manager.winning_count

        # Evaluate Horizontal
        for row in range(board_manager.rows):
            for col in range(board_manager.cols - (self.winning_count - 1)):
                window = [(matrix[row][col + i].type) for i in range(self.winning_count)]
                score += self.evaluate_window(window=window, team=team)

        # Evaluate Vertical
        for row in range(board_manager.rows - (self.winning_count - 1)):
            for col in range(board_manager.cols):
                window = [(matrix[row + i][col].type) for i in range(self.winning_count)]
                score += self.evaluate_window(window=window, team=team)

        # Evaluate Positivly Sloped
        for row in range(board_manager.rows - (self.winning_count - 1)):
            for col in range(board_manager.cols - (self.winning_count - 1)):
                window = [(matrix[row + i][col + i].type) for i in range(self.winning_count)]
                score += self.evaluate_window(window=window, team=team)

        # Evaluate Negativly Sloped
        for row in range(board_manager.rows - (self.winning_count - 1)):
            for col in range(board_manager.cols - (self.winning_count - 1)):
                window = [(matrix[row - i][col + i].type) for i in range(self.winning_count)]
                score += self.evaluate_window(window=window, team=team)

        return score

    def evaluate_window(self, window, team):
        score = 0

        if team == 'p1':
            opponent = 'p2'
        else:
            opponent = 'p1'

        for i in range(self.winning_count - 1):
            if window.count(team) == self.winning_count - i and window.count('blank') == i:
                score += self.winning_count - i

                if i == 0:
                    score += 10000

            if window.count(opponent) == self.winning_count - i and window.count('blank') == i:
                score -= self.winning_count - i

                if i == 0:
                    score -= 10000

        return score
