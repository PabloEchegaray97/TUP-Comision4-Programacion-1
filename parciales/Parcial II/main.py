from functions import * #get_mutant_dna - get_verticals - get_diagonals - print_matrix - print_diagonals - is_mutant
import time
#dna_test = ['ATACGA','CAATGA','TTATGA','AAAAGA','CCCCTA','TCACTG']
matrix = []
print_intro()
while len(matrix) < 6:
    row = input('Please insert a row: ').upper()

    if len(row) != 6 or any(letter not in 'ACTG' for letter in row):
        print('Please enter a valid row. Example: AACTGG. Valid letters: A, C, T, G.')
    else:
        matrix.append(row)

print('\nMatrix created successfully: \n \n')
print_matrix(matrix)

print('Starting DNA analysis...')
time.sleep(1)


counter_dna = 0
#counter_dna = get_mutant_dna(dna_test) + get_mutant_dna(get_verticals(dna_test)) + get_mutant_dna(get_diagonals(dna_test))
#print_matrix(dna_test)

print("Extracting DNA samples...")
time.sleep(2)

counter_dna = get_mutant_dna(matrix) + get_mutant_dna(get_verticals(matrix)) + get_mutant_dna(get_diagonals(matrix))

print("Analyzing DNA sequences...")
time.sleep(3)
print('Done!')
if is_mutant(counter_dna):
    print('\033[92mThis dna is mutant! The subject is apt to join the army.\033[0m')
else:
    print('\033[91mThis dna isn`t mutant. The subject can`t join the army.\033[0m')
