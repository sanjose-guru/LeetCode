class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # This is done by unpacking the rows of the matrix as arguments to the
        # zip function. zip(*matrix) couples elements with the same index
        # from each row together, effectively transposing the elements.
        # Then, the zip object is converted into a list of lists, which is the
        # transposed matrix.
        return [list(row) for row in zip(*matrix)]
