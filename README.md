# Knights Tour Problem

Solving the Knight's Tour using Warnsdorff algorithm.

## Warnsdorff Algorithm

1. Set P to be a random initial position on the board.
2. Mark the board at P with the move number "1".
3. Do following for each move number from 2 to the number of squares on the board.
    - Let S be the set of positions accessible from P.
    - Set P to be the position in S with minimum accessibiltiy.
    - Mark the board at P with the current move number.
4. Return the marked board - each square will be marked with the move number on which it is visited.

## Running the script

To run the script, you need to first install the requirements.

```bash
pip install -r requirements.txt
```

Then you can run the script by the typing in the erminal

``` bash
python main.py
```

## Input

The program will ask you to enter the starting position of the knight (x, y).

## Output

The program will print a 8x8 2D matrix that represents a chessboard and will display the progress of the knight's tour where yellow is the starting position and green in the final position.
