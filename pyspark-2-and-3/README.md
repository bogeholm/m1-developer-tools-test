## Get the data

The [`read-xetra.py`](read-xetra.py)-example assumes that (a subset of) the [Deutsche-Boerse/dbg-pds](https://github.com/Deutsche-Boerse/dbg-pds) dataset is available at `~/xetra/`. See [`awscli`](../awscli) for examples.

## Python 3.9 + PySpark 3
```bash
# Create `spark3` environment
conda env create -f spark3.yml
conda activate pyspark3

# Set Java version 11
jenv global 11

# Run script
python read-xetra.py

# Output
- - - - - - - - - - Software versions - - - - - - - - - - -
Python version: Python 3.9.2

Java version: openjdk version "11.0.10" 2021-01-19
OpenJDK Runtime Environment (build 11.0.10+9)
OpenJDK 64-Bit Server VM (build 11.0.10+9, mixed mode)

PySpark version: 3.1.1
- - - - - - - - - - Most traded by volume - - - - - - - - -
+--------+-------------------+
|Mnemonic|Total Traded Volume|
+--------+-------------------+
|     CBK|          9497475.0|
|     DBK|          8143939.0|
|    EOAN|          5944206.0|
|     DTE|          5667301.0|
|     LHA|          4758715.0|
+--------+-------------------+
only showing top 5 rows

Aggregated 24 files in 1.38 seconds.
```


## Python 3.7 + PySpark 2

```bash
# Install x86_64 version of Miniforge
arch -x86_64 sh Miniforge3-4.10.0-0-MacOSX-x86_64.sh

# Activate Miniforge x86_64 - assuming binaries live in `/Users/you/miniforge3-x86_64`
/Users/you/miniforge3-x86_64/bin/conda init zsh
source ~/.zshrc

# Create `spark2` environment
conda env create -f spark2.yml
conda activate pyspark2

# Set Java version 8
jenv global 1.8

# Run script
python read-xetra.py

# Output
- - - - - - - - - - Software versions - - - - - - - - - - -
Python version: Python 3.7.10

Java version: openjdk version "1.8.0_282"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_282-b08)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.282-b08, mixed mode)

PySpark version: 2.4.6

...

- - - - - - - - - - Most traded by volume - - - - - - - - -
+--------+-------------------+
|Mnemonic|Total Traded Volume|
+--------+-------------------+
|     CBK|          9497475.0|
|     DBK|          8143939.0|
|    EOAN|          5944206.0|
|     DTE|          5667301.0|
|     LHA|          4758715.0|
+--------+-------------------+
only showing top 5 rows

Aggregated 24 files in 3.80 seconds.

# Clean up: reactivate arm64 conda
/Users/you/miniforge3/bin/conda init zsh
source ~/.zshrc
```
