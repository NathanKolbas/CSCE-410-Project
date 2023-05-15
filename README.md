# CSCE-410-Project
Welcome to our CSCE 410 project! We are team Lic-T which stands for Linear Index Creator Tree.

## Getting started
First, please make sure you are using at least python version >= 3.10 as certain functions are required that only exist in these versions.

Once ready, install the packages using `pip install -r requirements.txt` which will install all the needed dependencies for this project.

You can now run the project using the command `python main.py --help` which will display all the valid commands.

If you would like to try using the index, simply run `python main.py -d data`. This is assuming the index is already built.

To build the index run `python main.py -d data -i INDEX` where `data` is the directory relative to the current directory that you would like to build the index for.

Here is some info about the commands:  
 - '-d' or '--dir': The starting directory, defaults to CWD. Can specify a relative path to the CWD.
 - '-i' or '--index': If the index should be built
 - '-e' or '--extension': The file type to build the index for
 - '-c' or '--clean': Removes all built index files
 - '-s' or '--search': Begin search
 - '-compare' or '--compare': Begin comparison

As always, check the code in `main.py` for more information as there are comments to help explain what is going on.
