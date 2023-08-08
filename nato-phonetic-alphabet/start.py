"""  """
# from pprint import pprint
# import pandas as pd

table = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
         'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
         'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
         'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

def main():
    """ main function """
    # csvfile_name = 'nato_phonetic_alphabet.csv'
    # csv_df = pd.read_csv(csvfile_name)
    # table = {letter : code for letter, code in zip(csv_df.letter, csv_df.code)}
    # table = {row.letter : row.code for index, row in csv_df.iterrows()}
    # print(table)
    word = 'House'
    word = ' '.join(list(word.upper()))
    coded_word = word.translate(str.maketrans(table))
    print(coded_word)

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
