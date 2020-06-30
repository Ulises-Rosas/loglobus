# loglobus

Transfer targeted directories (and targeted files inside them) between clusters

## Requirements
* python3
* ssh (to set a password-less access to clusters, see below)

## Installation

```bash
pip install loglobus
```

Using `git` (Optional):
```bash
git clone https://github.com/Ulises-Rosas/loglobus.git
cd loglobus
python setup.py install
```

## Overview

Firstly, make sure you can access to your clusters by using key files. This a pivotal point of the script due to iterations can be performed without manual control. You can learn how to do so [**here**](setPasswordlessAccess.md).

Once key files were created, these can be introduced into a [file](params_dir.txt) with other transfer parameters (e.g. `userid`, `host`, `path`). This file should look like this (i.e. json format):

```
{
    "from": {
        "userid": "userid",
        "host": "login.colonialone.gwu.edu",
        "path": "source_path",
        "key": "key_file_path"
    },
    "to": {
        "userid": "userid",
        "host": "pegasus.colonialone.gwu.edu",
        "path": "destination_path",
        "key": "key_file_path"
    }
}
```

The first `path` parameter (i.e. within "from" values) indicates the directory where target directories are located. The second one (i.e. within "to" values), indicates the destination directory where target directories will be located. Finally, this json file with parameters is plugged into the main script (i.e. `transferdir`), as well as the file with the list of target directories names:

```bash
transferdirs -f [file with directory names] -p [file with parameters]
```

[Glob patterns](globs.txt) can also be used to take specific files from each target directory by using the option `-g` (see `transferdirs -h` for more information).
