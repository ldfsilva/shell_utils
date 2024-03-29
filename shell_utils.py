"""shell_utils contains a series of python modules that will
attempt to replicate some of the most used Unix/Linux command
utilities behavior such as:

find
grep

NOTE:
These modules were developed for study purpose only, but feel
free to check it out, use, comment, point out any issues and
improvements that may be necessary.
"""
import sys
import os


def find(file_name, path=None):
    """This module recursively walks through a path searching for
    the given file name.

    If the file name is not found it will return nothing, otherwise
    it will return its details.

    If the path is not passed as the second argument it will search
    on the current directory.

    It expects a file name as its primary argument followed by an
    optional path argument which will be used to initiate the search.
    """

    if not path:
        path = os.getcwd()

    #Traverse through the path looking for the given file name
    for dirpath, dirnames, filenames in os.walk(path):
        if file_name in filenames:
            file_name = os.path.join(dirpath, file_name)
            file_details = get_file_details(file_name)
            print(file_name, file_details)


def get_file_details(file_name):
    """Return details of the given file in a dictionary"""

    stat = str(os.stat(file_name))

    #clean up start return, the slicing is to remove 
    #os.stat_result( at beginning and ) in the end
    stat = stat.replace(' ', '')[15:-1]

    #build the dictionary containing file details
    s_dict = {}
    for item in stat.split(','):
        key, val = item.split('=')
        s_dict.update({key: val})

    return s_dict


def main():
    """If called directly module and its parameters has to
    be specified"""

    n_args = len(sys.argv)
    if n_args > 2 and sys.argv[1] == 'find':
        arg2 = sys.argv[2]
        arg3 = None

        if n_args > 3:
            arg3 = sys.argv[3]

        find(arg2, arg3)
    else:
        message = \
"""You have to specify one of the available modules that you
wish to use with its respective required earameters.

Usage:
    shell-utils module_name module_parameters

Available modules:
    find:
        shell-utils.py find file_name [path]
"""
        print(message)


if __name__ == '__main__':
    main()

