# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Time Complexity: (N * 4^L) N is the number of cells in the board and L is the length of the word to be matched.

# For the backtracking function, its execution trace would be visualized as a 4-ary tree,
# each of the branches represent a potential exploration in the corresponding direction.
# Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 4-nary tree,
# which is about 4 ^ L
# We iterate through the board for backtracking, i.e. there could be N times invocation
# for the backtracking function in the worst case.
# Space Complexity: O(L) where L is the length of the word to be matched.

# The main consumption of the memory lies in the recursion call of the backtracking function.
# The maximum length of the call stack would be the length of the word.
# Therefore, the space complexity of the algorithm is O(L).


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret:
                break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret
