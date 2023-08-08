""" 228 The Great Squirrel Census Data Analysis with Pandas """
import pandas as pd
def main():
    """ main function """
    csvfile_name = '228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv'
    csv_dataframe = pd.read_csv(csvfile_name)
    print(csv_dataframe['Primary Fur Color'].value_counts())
    # print(csv_dataframe['Primary Fur Color'])
    # print(csv_dataframe.head(0))
    # print(csv_dataframe.columns)
    # print(csv_dataframe.keys())
    # print(csv_dataframe['Primary Fur Color'].describe())
    # csv_dataframe.to_excel('squirrels.xlsx')



if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
