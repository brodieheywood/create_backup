# Brodie Heywood
# November 26, 2018

"""Backup"""


def backup(file_name):
    """Backup a file.

    Create a .bak copy of a .txt file.
    PARAM: file_name, name of .txt file that will be backed up
    PRECONDITION: file_name must be a string and must exactly match the filename of a .txt file in the system
    POSTCONDITION: contents of file are copied in memory; writes a new file with same content but with .bak extension
    RETURN: none
    """
    file_to_be_backed_up = file_name + '.txt'
    backup_file = file_name + '.bak'

    try:
        with open(file_to_be_backed_up) as file_object:
            content = file_object.read()
        with open(backup_file, 'w') as file_object:
            file_object.write(content)

        print('generated  ' + backup_file)

    except FileNotFoundError:
        print('Sorry, file does not exist!')


def main():
    backup('backup_test')


if __name__ == '__main__':
    main()
