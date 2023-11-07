import time
mutant_dna = ['AAAA', 'CCCC','GGGG', 'TTTT']
dna_test_vertical = ['','','','','','']
def get_mutant_dna(dna):
    counter = 0
    for element in dna:
        for i in mutant_dna:
            if i in element:
                counter += 1
                #print('Coincidence')
    return counter

def get_verticals(dna):
    for word in dna:
        for index, letter in enumerate(word):
            dna_test_vertical[index] += letter
    return dna_test_vertical

def print_matrix(dna):
    for index, word in enumerate(dna):
        #print('Word index: ', index)
        for index, letter in enumerate(word):
            print(letter, end='    ')
        print('\n')

def get_diagonals(matriz):
    rows = len(matriz)
    columns = len(matriz[0])
    bottom_diagonals = []
    top_diagonals = []
    for i in range(rows):
        bottom_diag = ''
        for j in range(columns):
            if i + j < rows:
                bottom_diag += matriz[i + j][j]
        bottom_diagonals.append(bottom_diag)

    for i in range(rows):
        top_diag = ''
        for j in range(columns):
            if i - j >= 0:
                top_diag += matriz[i - j][j]
        top_diagonals.append(top_diag)

    return bottom_diagonals + top_diagonals

def print_diagonals(diagonals):
    for diagonal in diagonals:
        print(diagonal)

def is_mutant(counter_dna):
    if counter_dna >= 4:
        return True
    return False

def print_intro():
    banner ="""                 _              _         _                                 _                    
 _ __ ___  _   _| |_ __ _ _ __ | |_    __| |_ __   __ _    __ _ _ __   __ _| |_   _ _______ _ __ 
| '_ ` _ \| | | | __/ _` | '_ \| __|  / _` | '_ \ / _` |  / _` | '_ \ / _` | | | | |_  / _ \ '__|
| | | | | | |_| | || (_| | | | | |_  | (_| | | | | (_| | | (_| | | | | (_| | | |_| |/ /  __/ |   
|_| |_| |_|\__,_|\__\__,_|_| |_|\__|  \__,_|_| |_|\__,_|  \__,_|_| |_|\__,_|_|\__, /___\___|_|   
                                                                              |___/              """

    print(banner)
    print('Please enter a 6 x 6 DNA sequence')
    print('The DNA will be mutant if and only if the subject has 4 or more matches with mutant DNA sequences.')