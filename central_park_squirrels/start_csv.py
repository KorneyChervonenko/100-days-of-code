""" 228 The Great Squirrel Census Data Analysis """
from __future__ import annotations
import csv
from collections import namedtuple
from string import punctuation
#pylint: disable=E1101

def main():
    """ main function """
    csvfile_name = '228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv'
    color_statistic = {}
    with open(csvfile_name, newline='', encoding='utf-8') as datafile:
        csv_datastream = csv.reader(datafile)
        table_header = next(csv_datastream)
        table_header = normalise_table_header(table_header)
        squirrel_data = namedtuple('Squirrel', table_header)
        for _, line in enumerate(csv_datastream):
            squirrel = squirrel_data(*line)
            color = squirrel.Primary_Fur_Color
            if color == '':
                color = 'Undefined'
            color_statistic[color] = color_statistic.get(color, 0) + 1
    print(color_statistic)


def normalise_table_header(table_header: list) -> list:
    """ replace spaces with _ """
    normalised_table_header = []
    for field_name in table_header:
        field_name = field_name.strip()
        normalised_field_name = ''.join('_' if ch in punctuation + ' ' else ch for ch in field_name)
        normalised_table_header.append(normalised_field_name)
    return normalised_table_header

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
