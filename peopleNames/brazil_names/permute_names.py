import itertools
import sys

def generate_permutations(input_file, output_file):
    with open(input_file, 'r') as file:
        words = file.read().splitlines()

    permutations = list(itertools.permutations(words, 2))
    permuted_lines = ['.'.join(perm) for perm in permutations]
    print(permutations)
    with open(output_file, 'w') as file:
        print(permuted_lines)
        file.write('\n'.join(permuted_lines))

# Usage example
input_file = sys.argv[1]  # Replace with the path to your input file
output_file = 'output.txt'  # Replace with the desired path for the output file

generate_permutations(input_file, output_file)

