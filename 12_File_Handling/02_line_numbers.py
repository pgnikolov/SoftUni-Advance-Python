def process_file(input_file, output_file):
    total_letters = 0
    total_punctuation = 0
    punctuation_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line_number, line in enumerate(lines, start=1):
            line_letters = sum(c.isalpha() for c in line)
            line_punctuation = sum(c in punctuation_chars for c in line)

            total_letters += line_letters
            total_punctuation += line_punctuation

            outfile.write(f"Line {line_number}: {line.strip()} ({line_letters})({line_punctuation})\n")


input_filename = '02_text.txt'
output_filename = '02_output.txt'

process_file(input_filename, output_filename)
