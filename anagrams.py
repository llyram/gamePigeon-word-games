def load_dictionary(file_path='scrabble.txt'):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def find_anagrams(letters, dictionary, min_length=3):
    letters = letters.lower()
    found_words = set()
    
    def is_valid_word(word, available_letters):
        letter_count = {}
        for letter in available_letters:
            letter_count[letter] = letter_count.get(letter, 0) + 1
            
        for letter in word:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            letter_count[letter] -= 1
        return True

    for word in dictionary:
        if len(word) >= min_length and len(word) <= len(letters):
            if is_valid_word(word, letters):
                found_words.add(word)
    
    return sorted(found_words, key=len, reverse=True)

def main():
    try:
        dictionary = load_dictionary()
        letters = input("Enter 6 letters: ")
        
        if len(letters) != 6:
            print("Please enter exactly 6 letters")
            return
            
        anagrams = find_anagrams(letters, dictionary)
        
        if anagrams:
            print("\nFound anagrams (sorted by length):")
            for word in anagrams:
                print(word)
        else:
            print("No anagrams found")
            
    except FileNotFoundError:
        print("Error: scrabble.txt file not found")

if __name__ == "__main__":
    main()