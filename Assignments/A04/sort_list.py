
# Example Transpositional Matrix
trans_matrix = {
    'Q':['D','A','G','F','F','X'],
    'U':['F','D','A','D','X','A'],
    'A':['F','G','D','A','D','G'],
    'R':['F','G','A','A','D'],
    'K':['A','F','G','D','G']
}

# print out original
for k,v in trans_matrix.items():
    print(f"{k} : {v}")

# sort the matrix
sorted_matrix = sorted(trans_matrix.items())

# sorted_matrix now contains "tuples"
# tuple = (item0,item1,....,itemN)
# Example: item = ('A', ['F', 'G', 'D', 'A', 'D', 'G'])
# You can access the 'A' using item[0]
# you can access the letters list by using item[1]
# New list looks like: 
#[('A', ['F', 'G', 'D', 'A', 'D', 'G']), ('K', ['A', 'F', 'G', 'D', 'G']), ('Q', ['D', 'A', 'G', 'F', 'F', 'X']), ('R', ['F', 'G', 'A', 'A', 'D']), ('U', ['F', 'D', 'A', 'D', 'X', 'A'])]

print("")

# printing out the sorted "tuples"
for item in sorted_matrix:
    print(f"{item[0]} : {item[1]}")


