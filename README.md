# batch-remove_line-python
A very simple Python script for removing a certain line from multiple text-based files at once. 

Instructions:
1. BE VERY CAREFUL so as to not edit files you do not want to. Move this script to a directory with no files or sub-directories and copy the files you wish to modify there, before moving back and replacing in their original location.
2. open remove-line.py and configure the three constants at the top.  
    a. SELECTED_LINE is the line from the text file you wish to delete (the very top line in your text file is considered "1").  
    b. DIRECTORY is the relative path to your files from the working directory of the script. I have not done thorough testing with this, so please leave this as "./" (unless you want to test it), and instead just have this script and run it in the directory you want to use it in.  
    c. FILE_TYPES is a list of the extensions of files you wish to search for and modify.
