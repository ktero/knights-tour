# Solving the knight's tour problem board using the Warnsdorff algorithm

Algorithm:

1. Set P to be a random initial position on the board.
2. Mark the board at P with the move number "1".
3. Do following for each move number from 2 to the number of squares on the board.
    - Let S be the set of positions accessible from P.
    - Set P to be the position in S with minimum accessibiltiy.
    - Mark the board at P with the current move number.
4. Return the marked board - each square will be marked with the move number on which it is visited.
