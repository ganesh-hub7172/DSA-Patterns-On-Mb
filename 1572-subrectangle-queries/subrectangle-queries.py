class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rect = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rect[r][c] = newValue

    def getValue(self, row, col):
        return self.rect[row][col]
