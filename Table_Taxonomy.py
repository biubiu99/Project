from pathlib import Path
import csv
class Table:

    def __init__(self, csv_file):
        lines = csv_file.readlines()
        self.lines = lines
        number_of_line = len(list(lines)) - 1
        self.number_of_line = number_of_line
        self.index = [i for i in range(number_of_line)]
        self.columns = lines[0].split(',')
        list_of_data = []
        for line in lines[1:]:
            elements = line.split(',')
            list_of_data.append(elements)
        dictionary_1 = {}
        for i in range(number_of_line):
            dictionary_1[i] = dict(zip(self.columns, list_of_data[i]))
        self.data = dictionary_1


    def __getitem__(self, item):
        if isinstance(item, int):
            return self.data[item]
        elif isinstance(item, tuple):
            return self.data[item[0]item[1]]


    def __repr__(self):
        for i in range(self.number_of_line + 1):
            row = self.lines[i]
            print(row)

csv_file_path = Path.cwd() / 'for_training.csv'
csv_file = csv_file_path.open()
my_table = Table(csv_file)
print(my_table[1,'name'])