from collections import defaultdict

def load_dictionary():
    # Try to load the system dictionary
    with open('scrabble.txt', 'r') as f:
        return {word.strip().lower() for word in f if len(word.strip()) >= 3}
            
def is_valid_position(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def get_neighbors(x, y, rows, cols):
    directions = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0),  (1,1)]
    
    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_position(new_x, new_y, rows, cols):
            neighbors.append((new_x, new_y))
    return neighbors

def find_words(grid, dictionary):
    rows = len(grid)
    cols = len(grid[0])
    found_words = {}

    def dfs(x, y, current_word, path, visited):
        current_word += grid[x][y]
        current_path = path + [(x, y)]
        
        # If the word exists in dictionary, add it to found words
        if current_word in dictionary:
            found_words[current_word] = current_path
            
        # Visit neighbors
        visited.add((x, y))
        for next_x, next_y in get_neighbors(x, y, rows, cols):
            if (next_x, next_y) not in visited:
                dfs(next_x, next_y, current_word, current_path, visited.copy())
    
    # Start DFS from each position in grid
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, "", [], set())
            
    return found_words

def group_similar_words(found_words):
    # Group words by their first three letters
    groups = defaultdict(list)
    for word, path in found_words.items():
        prefix = word[:3]
        groups[prefix].append((word, path))
    
    # Sort groups by:
    # 1. Number of words (descending)
    # 2. Maximum word length in group (descending)
    # 3. Prefix (alphabetically)
    sorted_groups = sorted(
        groups.items(),
        key=lambda x: (
            -len(x[1]),                    # number of words in group (negative for descending)
            -max(len(word) for word, _ in x[1]),  # max word length in group (negative for descending)
            x[0]                           # prefix alphabetically
        )
    )
    
    return sorted_groups
      
def main():
    print("Loading dictionary...")
    dictionary = load_dictionary()
    print(f"Dictionary loaded with {len(dictionary)} words")

    print("\nEnter the 16 letters (4x4 grid) in a single line:")
    try:
        input_letters = input().strip().lower()
        if len(input_letters) != 16:
            raise ValueError("Input must be exactly 16 letters")
        if not input_letters.isalpha():
            raise ValueError("Input must contain only letters")
    except ValueError as e:
        print(f"Error: {e}")
        return

    grid = []
    for i in range(0, 16, 4):
        grid.append(list(input_letters[i:i+4]))

    print("\nGrid:")
    for row in grid:
        print(' '.join(row))

    found_words = find_words(grid, dictionary)
    
    # Group similar words
    word_groups = group_similar_words(found_words)

    print(f"\nFound {len(found_words)} words:")
    for prefix, words in word_groups:
        print(f"\n--- Words starting with '{prefix}' ---")
        # Sort words within each group by length (longest first) and alphabetically
        sorted_words = sorted(words, key=lambda x: (len(x[0]), x[0]))
        for word, path in sorted_words:
            print(f"{word}")
            
if __name__ == "__main__":
    main()