FILE_NAME = 'hyperskill-dataset-41153137.txt'
with open(FILE_NAME, 'r') as file:
    print(len([x for x in file.readlines() if x == 'summer\n']))
