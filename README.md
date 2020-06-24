# loglobus

Transfer targeted directories (and targeted files inside them) between clusters

## Requirements
* python3
* ssh (to set a password-less access to clusters, see below)

## Installation

```bash
pip install loglobus
```

## Overview

Firstly, make sure you can access to your clusters by using key files. This a pivotal point of the script due to iterations can be performed without manual control. You can learn how to do so [**here**](setPasswordlessAccess.md).

Once key files are created, these can be introduced at the `params_dirs.txt` file, as well as other paramenters (e.g. `userid`, `host`, `path`):

```bash
cat params_dir.txt
```
```bash
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

Finally, this file can be plugged into the main script (i.e. `transferdir`), as well as the file with the list of source directories names:

```bash
transferdirs -f [file with directory names] -p params_dir.txt
```

[Glob patterns](globs.txt) can also be used to take specific files from each source directory by using the option `-g` (see `transferdirs -h` for more information).
