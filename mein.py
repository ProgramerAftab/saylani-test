def analyze_file(filename):
    try:
        with open(filename, 'r',) as file:
            lines = file.readlines()
            
            total_lines = len(lines)
            total_words = 0
            total_chars = 0
            
            for line in lines:
                total_chars += len(line) 
                total_words += len(line.split()) 

        return {
            'characters': total_chars,
            'words': total_words,
            'lines': total_lines
        }

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def search_word(filename, target_word):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()  
            target_word = target_word.lower()
            
            word_count = content.split().count(target_word)

        return word_count

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None