import csv
from pathlib import Path
import argparse
import subprocess


def run_tool(instances_path: str, script_path: str, benchmark_path: str) -> None:
    with Path(instances_path).open("r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            onnx, vnnlib, timeout = row
            subprocess.call(
                [
                    "sh",
                    script_path,
                    "v1",
                    "nn4sys",
                    f"{benchmark_path}/{onnx}",
                    f"{benchmark_path}/{vnnlib}",
                    f"{idx}.txt",
                    timeout,
                ]
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
        "--path_to_benchmark",
        required=True,
        help="Path to the benchmark containing the 'onnx' and 'vnnlib' folders.",
    )
    args = parser.parse_args()
    run_tool(args.instances, args.script, args.path_to_benchmark)


if __name__ == "__main__":
    main()
