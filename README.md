
<!-- PROJECT LOGO -->
# Olympus
_Two Part program that either helps consolidate future CodeSet orders or remove low-volume probes from inventory_.

<!-- ABOUT THE PROJECT -->
## About The Program

This program or tool was built to simply a repetitve task that the oligo team needs to perform.
On average it takes about an hour and a half to two hours to set up either process, this allows no manual work and 
accomplishes the same tasks in a fraction of the time.


### Built With

* [tkinter](https://github.com/rdbende/tkinter-docs): Simple GUI to create an interface
* [Pandas](https://github.com/pandas-dev/pandas): Easy processing csv for manipulation
* [Glob](https://github.com/python/cpython/blob/main/Lib/glob.py): Gathering of files
* [Pyodbc](https://github.com/mkleehammer/pyodbc): Connection to Database
* [Collections](https://docs.python.org/3/library/collections.html): Counting item numbers
* [Itertools](https://docs.python.org/3/library/itertools.html): Condense nested arrays



<!-- GETTING STARTED -->
## Getting Started

For proper function make sure you have the proper modules.
The below steps will make sure all modules are available for interpretation.

### Prerequisites

`Pandas` pip install pandas
`Glob` pip install glob
`tkinter` pip install tkinter
`pyodbc` pip install pyodbc
'Collections' pip install collections
'Itertools' pip install itertools


<!-- USAGE EXAMPLES -->
## Usage

The usage is only for whats called pre-rack condensations or low-volume removals.

### What to expect
A GUI interface will show two buttons: pre-rack condensation or low-volume removal. 
After clicking either, a file management window will open, where you will select working folder where both masterfiles are located.
The data pipline will extract the data, transform it and export it back to the selected folder.


