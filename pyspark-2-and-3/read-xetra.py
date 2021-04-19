from pathlib import Path
from pyspark.sql import SparkSession
from typing import Any, List

import pyspark
import pyspark.sql.functions as spark_f
import subprocess
import sys
import time

data_path = Path.home() / "xetra"
# Pick single day for testing - comment to read all files
data_path = data_path / "2017-07-03"


def print_section(section: str) -> None:
    format_section = section + " "
    LEFT_NUM_SEP = 10
    RIGHT_NUM_SEP = 20
    SEP_TEXT = "- "
    left_pad = LEFT_NUM_SEP*SEP_TEXT
    right_pad_len = int(max(0, RIGHT_NUM_SEP*len(SEP_TEXT) - len(format_section)) / len(SEP_TEXT))
    right_pad = SEP_TEXT*right_pad_len

    print()
    print(f"{left_pad}{format_section}{right_pad}")


print_section("Software versions")
python_version = subprocess.check_output(['python', '--version'], stderr=subprocess.STDOUT)
java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)


print(f"Python version: {python_version.decode()}")
print(f"Java version: {java_version.decode()}")
print(f"PySpark version: {pyspark.__version__}")


def show_examples_from_list(some_list: List[Any]) -> None:
    MAX_EXAMPLES_HEAD_AND_TAIL = 3

    def print_list_as_list(sub_list: List[Any]) -> None:
        for element in sub_list:
            print(f" - {element}")

    if len(some_list) <= 2*MAX_EXAMPLES_HEAD_AND_TAIL:
        print_list_as_list(some_list)

    else:
        skipped = len(some_list) - 2*MAX_EXAMPLES_HEAD_AND_TAIL
        print_list_as_list(some_list[0:MAX_EXAMPLES_HEAD_AND_TAIL])
        print(f"... ({skipped} elements not shown) ...")
        print_list_as_list(some_list[-MAX_EXAMPLES_HEAD_AND_TAIL:])



if not data_path.exists():
    print(f"Data path{data_path} not found.")
    sys.exit(1)


print_section("How many files did we find?")
files = list(data_path.glob("**/*.csv"))
print(f"Found {len(files)} files:")
show_examples_from_list(files)


print_section("Spark warning section")
spark = SparkSession.builder.master("local").appName("xetra-spark3").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


print_section("Data example")
t_start = time.time()
df = spark.read.csv([str(file) for file in files], header=True)
t_end = time.time()
print("Read {} files in {:.2f} seconds.".format(len(files), t_end - t_start))

df.show(5)


print_section("Most traded by volume")
total_traded_volume = "Total Traded Volume"

t_start = time.time()
volume = df.groupBy("Mnemonic").agg(spark_f.sum("TradedVolume").alias(total_traded_volume)).orderBy(total_traded_volume, ascending=False)
volume.show(5)
t_end = time.time()
print("Aggregated {} files in {:.2f} seconds.".format(len(files), t_end - t_start))
