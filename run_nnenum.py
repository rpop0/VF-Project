import csv
from pathlib import Path
import argparse
import subprocess


def run_tool(instances_path: str, script_path: str) -> None:
    with Path(instances_path).open("r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            onnx, vnnlib, timeout = row
            subprocess.call(
                ["sh", script_path, "v1", "nn4sys", onnx, vnnlib, timeout, f"{idx}.txt"]
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--instances", required=True, help="instances.csv file to process."
    )
    parser.add_argument(
        "-s", "--script", required=True, help="Shell script to run the tool."
    )
    parser.add_argument(
        "-p",
        "--path-to-benchmark",
        required=True,
        help="Path to the benchmark containing the 'onnx' and 'vnnlib' folders.",
    )
    args = parser.parse_args()
    run_tool(args.instances, args.script)


if __name__ == "__main__":
    main()
