# Install `awscli`

## Install with `conda`

```bash
conda env create -f aws.yml
conda activate aws

aws --version
aws-cli/1.19.53 Python/3.9.2 Darwin/20.3.0 botocore/1.20.53
```

## Use example
As an example, get the [Deutsche-Boerse/dbg-pds](https://github.com/Deutsche-Boerse/dbg-pds) dataset from GitHub (**large download**).

```bash
mkdir ~/xetra
aws s3 sync --no-sign-request s3://deutsche-boerse-xetra-pds/ ~/xetra
```
