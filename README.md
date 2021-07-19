# Lines

Command line tool to count the lines of code in a project folder

## Installation

```
# clone the repo
$ git clone https://github.com/siddharthroy12/lines.git

# change the working directory to lines
$ cd lines


# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```
python3 lines.py -h
usage: lines path [options]

Count the lines of code in a project folder

positional arguments:
  path                  the path to the project folder

optional arguments:
  -h, --help            show this help message and exit
  -e                    Count empty lines
  -i [Files [Files ...]]
                        Files to ignore
  -v, --verbose         Show files that are counted
```

To count lines of code in this project
```
python3 lines.py ./
```

To count empty lines too
```
python3 lines.py ./ -e
```

To ignore additional files
```
python3 lines.py ./ -i README.md requirements.txt
```

To show the files that are counted
```
python3 lines.py ./ -v
```

## Note

Files and folders defined in .gitignore file will be ingored (whether -i is used or not)

## License

MIT © Siddharth Roy
