from typing import List


class NQueens:
    n: int
    solution: List[List[int]] | None

    def __init__(self, n: int) -> None:
        self.n = n
        self.solution = [[0 for _ in range(n)] for _ in range(n)]
        if not self.solve(0):
            self.solution = None
        
    def is_safe_to_move(self, row: int, col: int) -> bool:
        for i in range(col):
            if self.solution[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.solution[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.solution[i][j] == 1:
                return False
        
        return True

    def solve(self, col: int) -> bool:
        if col == self.n:
            return True

        for i in range(self.n):
            if self.is_safe_to_move(i, col):
                self.solution[i][col] = 1
                if self.solve(col + 1):
                    return True
                self.solution[i][col] = 0

        return False

    def __str__(self) -> str:
        if self.solution is None:
            return "No solution exists"

        return "\n".join(
            " ".join("Q" if cell == 1 else "-" for cell in row)
            for row in self.solution
        )
            

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    n_queens = NQueens(n)
    print(n_queens)
    