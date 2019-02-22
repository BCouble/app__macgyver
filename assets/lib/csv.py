
import os
import csv


def creation_area(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_file = os.path.join(directory, "map", data_file)
	structure_area = []
	with open(path_to_file, newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		
		for row in reader:
			structure_area.append(row)


	return structure_area 

def main():
	creation_area('maze.csv')

if __name__ == "__main__":
    main()