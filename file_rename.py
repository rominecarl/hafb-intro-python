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
    saved_path = os.getcwd()    # save current directory
    # Go to the files' directory
    os.chdir(folder_dir)
    for file in files:
        # Remove digits from name
        # new_file = file.lstrip('0123456789')
        # print("old name:", file, "new name:", new_file)
        # Rename file to new name
        # os.rename(file, new_file, folder_dir, folder_dir) <-- why didn't this work?
        # os.rename(file, new_file)
        os.rename(file, file.lstrip('0123456789'))  # Refactored line
    # Get back home
    os.chdir(saved_path)





def main():
    """
    Test function
    :return: None
    """
    rename_files()


if __name__ == "__main__":
    main()
    exit(0)