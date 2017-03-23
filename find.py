"""This module recursively walks through a path searching for 
the given file name. 

If the file name is not found it will return nothing, otherwise
it will return its details.

If the path is not passed as the sencond argument it will search
on the current directory.

NOTE:
This utility is for study purpose only, it tries to replicate 
the find utility command behavior found in most Unix/Linux systems.
"""
import sys
import os


def find(file_name, path=None):
    """It expects a file name as its primary argument followed by an 
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
    if len(sys.argv) == 2:
        arg1 = sys.argv[1]
        find(arg1)
    elif len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        find(arg1, arg2)
    else:
        print("Please specify the file that you're looking for")
        return(-1)


if __name__ == '__main__':
    main()
