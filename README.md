# Test of developer tools on Apple M1

This `README` covers setup. For some use cases, see subdirectories:
- [`awscli`](awscli/): install the Python [`awscli`](https://aws.amazon.com/cli/) with Anaconda
- [`pyspark-2-and-3`](pyspark-2-and-3/): example running on your choice of PySpark 2 or 3
-[`docker-amd64`](docker-amd64/): build an `x86_64` Docker image on an M1 machine

## Basic tools

```bash
# Command line developer tools - git, clang, curl, vim etc.
xcode-select --install

# Emulation layer to run x86_64 (Intel) binaries on aarch64 (M1)
softwareupdate --install-rosetta --agree-to-license
```

## Homebrew

```bash
bash -c "$(curl -fsSL --proto '=https' --tlsv1.2 https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
source ~/.zprofile
```

## Anaconda via Miniforge

Download from [github.com/conda-forge/miniforge/releases/latest](https://github.com/conda-forge/miniforge/releases/latest)

```bash
# Compute SHA-256 checksum
shasum -a 256 Miniforge3-4.10.0-0-MacOSX-arm64.sh
f939014048e40d127082c41b66bb98760fa2ce586b0b0dc043f6a38c78198e78

# Check if it matches
cat Miniforge3-4.10.0-0-MacOSX-arm64.sh.sha256
f939014048e40d127082c41b66bb98760fa2ce586b0b0dc043f6a38c78198e78

# Install
sh Miniforge3-4.10.0-0-MacOSX-arm64.sh

# Follow on screen instructions
```

## Anaconda for legacy Python versions

```bash
shasum -a 256 Miniforge3-4.10.0-0-MacOSX-x86_64.sh
cat Miniforge3-4.10.0-0-MacOSX-x86_64.sh.sha256

# Install - note the `arch` command
arch -x86_64 sh Miniforge3-4.10.0-0-MacOSX-x86_64.sh
```

## Switch between `arm64 conda` and `x86_64 conda`

This solution is not elegant if you expect to use both versions frequently.

```bash
# Switch to x86_64
/Users/<you>/<path to x86_64 miniforge installation>/bin/conda init zsh
source ~/.zshrc

# Switch back to arm64
/Users/<you>/<path to arm64 miniforge installation>/bin/conda init zsh
source ~/.zshrc
```

## Poetry

[python-poetry.org/docs](https://python-poetry.org/docs/)

```bash
curl -sSL --proto '=https' --tlsv1.2 https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.zshrc
```

## Java 8 and 11

### Manage several Java versions with [`jenv`](https://github.com/jenv/jenv)

```bash
brew install jenv

# Follow on screen instructions - add the following to ~./zshrc
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"

# Update profile
source ~/.zshrc

# Test
jenv doctor
```

### Java 8 and 11

Check package availability at [brew.sh](https://brew.sh).

```bash
brew install AdoptOpenJDK/openjdk/adoptopenjdk8 openjdk@11
# DO NOT add to your $PATH if you want to use `jenv`

# Add environments
jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
jenv add /opt/homebrew/opt/openjdk@11
```
