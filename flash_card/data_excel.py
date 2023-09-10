""" convert excel to list """
from pprint import pprint
import pandas as pd
import pickle
from collections import namedtuple

Word = namedtuple('Word', ('Index', 'EN', 'RU', 'Count'))

def get_data_from_file(filename : str='data.pickle') -> dict:
    """ load data_base from file """
    try:
        with open(filename, 'rb') as datafile:
            data = pickle.load(datafile)
            return data
    except:
        print('something went wrong')
        return [Word(0, 'word', 'слово', 0),]
    
def save_data_to_file(data_object: object, filename: str='data.pickle'):
    """ save object to file """
    with open(filename, 'wb') as datafile:
        pickle.dump(data_object, datafile, protocol=pickle.HIGHEST_PROTOCOL)
        print('data was saved')



def main():
    """ main function """
    excel_file_name = 'oxford2000.xlsx'
    # excel_file_name = 'test_dict.xlsx'
    excel_df = pd.read_excel(excel_file_name)
    table = [Word(i, en, ru, 0) for i, (en, ru) in enumerate(zip(excel_df.EN, excel_df.RU))]
    save_data_to_file(table)
    loaded_table = get_data_from_file()
    pprint(loaded_table)


if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
