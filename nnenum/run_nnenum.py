import csv
from pathlib import Path
import argparse
import subprocess
import time


def run_tool(instances_path: str, script_path: str, benchmark_path: str) -> list[dict]:
    results: list[dict] = []
    with Path(instances_path).open("r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            onnx, vnnlib, timeout = row
            start = time.perf_counter()
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
            end = time.perf_counter()
            results.append({
                'idx': idx,
                'duration': end - start
            })
    return results


def get_results(results: list[dict]) -> list[dict]:
    for result in results:
        with Path(f'{result["idx"]}.txt').open('r') as f:
            result['result'] = f.readline()
    return results


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
    results = run_tool(args.instances, args.script, args.path_to_benchmark)
    results = get_results(results)
    print(results)


if __name__ == "__main__":
    main()
