# CircuitPython filesystem builder

The python script creates a binary file containing a FAT filesystem. 
The filesystem created is compatible with [Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython?gclid=CjwKCAjwiuuRBhBvEiwAFXKaNI8QoLV-kE01hWlVvdCPmaU6fpLl7aVEPE6ZoyvobWpjv3mwjiCVkRoCrbMQAvD_BwE).


## Preparation

It's good practice to use a virtual environment so that project dependencies
are kept separate from system packages. See [venv](https://docs.python.org/3/library/venv.html) for more detials.

For example, in the directory containing a clone of this repo, run

```shell
python3 -m venv .
```

The virtual environment can then be activated by

```shell
. bin/activate
```

## Installation

The dependency packages are installed with

```shell
pip3 install -r requirements.txt
```


## Building a FAT filesystem file from a directory

After installing the required packages, you can build a FAT filesystem by running `main.py` with two arguments - the directory containing the files to store in the filesystem, and the output file. The output file should have the extension `.cpy` for use with the Notecard and Outboard DFU.

```shell
python3 main.py <directory> <output-file>[.cpy]
```

For more details

```shell
python3 main.py -h
```


## License

Copyright (c) 2022 Blues, Inc. Released under the MIT license. See
[LICENSE](LICENSE.mit) for details.
