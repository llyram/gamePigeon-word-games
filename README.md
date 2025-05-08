# GamePigeon Word Games Solver

This project provides tools to solve word-based puzzles like "Word Hunt" and "Anagrams" using a dictionary of valid words. It includes functionality to find valid words in a grid and generate anagrams from a set of letters.

## Features

- **Word Hunt Solver**:
  - Finds all valid words in a 4x4 grid of letters.
  - Groups words by their first three letters and sorts them by length and alphabetically.

- **Anagram Solver**:
  - Finds all valid anagrams from a given set of 6 letters.
  - Sorts anagrams by length in descending order.

## Files

- `word-hunt.py`: Contains the logic for solving the Word Hunt puzzle.
- `anagrams.py`: Contains the logic for generating anagrams from a set of letters.
- `scrabble.txt`: A dictionary file containing valid words (one word per line).
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Requirements

- Python 3.6 or higher.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gamePigeon-word-games
   ```
2. Ensure scrabble.txt is present in the project directory. This file should contain a list of valid words, one per line.

3. (Optional) Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install any required dependencies (if applicable).

## Usage
Word Hunt Solver
1. Run the word-hunt.py script:
    ```bash
    python word-hunt.py
    ```

2. Enter the 16 letters of the 4x4 grid in a single line (row by row). For example:
    ```
    abcd
    efgh
    ijkl
    mnop
    ```
3. The script will output all valid words found in the grid, grouped by their first three letters.

Anagram Solver
1. Run the anagrams.py script:
    ```bash
    python anagrams.py
    ```

2. Enter 6 letters when prompted.

3. The script will output all valid anagrams sorted by length.

Example Outputs
Word Hunt Solver
```
    Enter the 16 letters (4x4 grid) in a single line:
    abcdijklmnopqrs

    Grid:
    a b c d
    i j k l
    m n o p
    q r s t

    Found 10 words:

    --- Words starting with 'abc' ---
    abc
    abcd
    ...

    --- Words starting with 'ijk' ---
    ijk
    ijkl
    ...
```
Anagram Solver
```
Enter 6 letters: listen

Found anagrams (sorted by length):
silent
listen
inlets
...
```
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.

