"""
Rename files from a folder
Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
# Downloaded and extracted to: C:\Users\carlromine\Downloads\prankOrig\

import os


def rename_files():
    """
    Rename files in a folder
    :return: Nothing
    """

    folder_dir = r"C:\Users\carlromine\Downloads\prankOrig"
    files = os.listdir(folder_dir)
    for file in files:
        print(files)




def main():
    """
    Test function
    :return: None
    """
    pass


if __name__ == "__main__":
    main()
    exit(0)