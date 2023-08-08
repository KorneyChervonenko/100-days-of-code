""" Mail Merge Project """
import os

def main():
    """ main function """
    names_filename = 'invited_names.txt'
    names_filepath = './Input/Names/'
    names_file_fullname = names_filepath + names_filename
    print(names_file_fullname, os.path.exists(names_file_fullname))
    names = []
    with open(names_file_fullname, 'r', encoding='utf-8') as names_file_data:
        for line in names_file_data:
            names.append(line.strip())
            # print('>' + line + '<')
    print(names)
    template_filename = 'starting_letter.txt'
    template_filepath = './Input/Letters/'
    template_file_fullname = template_filepath + template_filename
    print(template_file_fullname, os.path.exists(template_file_fullname))

    with open(template_file_fullname, 'r', encoding='utf-8') as template_file_data:
        template_first_line = template_file_data.readline()
        print(f'{template_first_line = }')
        template_lines = template_file_data.readlines()

    output_letters_directory = './Output/ReadyToSend/'
    for name in names:
        new_letter_file_name_fullpath = output_letters_directory + \
                                        'letter_for_' + \
                                        name + \
                                        '.txt'
        personalized_first_line = template_first_line.replace('[name]', name)
        with open(new_letter_file_name_fullpath, 'w', encoding='utf-8') as new_letter_file:
            new_letter_file.write(personalized_first_line)
            new_letter_file.writelines(template_lines)

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
