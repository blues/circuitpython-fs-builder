# CircuitPython filesystem builder

This tool creates a file containing a FAT filesystem from a directory. The filesystem created is compatible with [Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython?gclid=CjwKCAjwiuuRBhBvEiwAFXKaNI8QoLV-kE01hWlVvdCPmaU6fpLl7aVEPE6ZoyvobWpjv3mwjiCVkRoCrbMQAvD_BwE).

The tool converts a directory containing CircuitPython scripts and libraries into a single file that is compatible with CircuitPython. This file can be deployed over-the-air to production devices, or used to program devices at the factory. It is not intended to replace use of the `CIRCUITPY` drive during development.


## Preparation

It's good practice to use a virtual environment so that project dependencies
are kept separate from system packages. See [venv](https://docs.python.org/3/library/venv.html) for more detials.

For example, in the directory containing a clone of this repo, run

```shell
python3 -m venv venv
```

The virtual environment can then be activated by

```shell
. venv/bin/activate
```

## Installation

The tool is installed using `pip`:

```shell
pip3 install .
```


## Building a FAT filesystem file from a directory

After installing the the package, you can build a FAT filesystem by running `cpy-fs` with two arguments - the directory containing the files to store in the filesystem, and the output file. The output file should have the extension `.cpy` for use with [Notecard Outboard Firmware Updates](https://dev.blues.io/guides-and-tutorials/notecard-guides/notecard-outboard-firmware-update/).

```shell
cpy-fs <directory> <output-file>[.cpy]
```

For more details:

```shell
cpy-fs -h
```

## Viewing the Contents of the FAT filesystem

The package provides a simple utility, `cpy-fs-dir` that shows the directory tree of the files in the `.cpy` file.

```
cpy-fs-dir <filesystem-file>
```

## License

Copyright (c) 2022 Blues, Inc. Released under the MIT license. See
[LICENSE](LICENSE.mit) for details.
