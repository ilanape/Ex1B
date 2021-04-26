class TreeNode:
    # constructor
    def __init__(self, letter, freq=0, left=None, right=None):
        self.letter = letter
        self.freq = freq
        self.left = left
        self.right = right

    # < operator
    def __lt__(self, other):
        return self.freq < other.freq

    def get_children(self):
        return self.left, self.right

    def get_letter(self):
        return self.letter

    def has_children(self):
        return self.left is not None or self.right is not None

