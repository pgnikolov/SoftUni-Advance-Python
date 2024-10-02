def even_lines(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            if line_number % 2 == 0:
                for char in {"-", ",", ".", "!", "?"}:
                    line = line.replace(char, "@")

                words = line.split()
                reversed_words = " ".join(reversed(words))

                print(reversed_words)


even_lines('text1.txt')
