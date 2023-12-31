#! /usr/bin/env bash

version=$1
benchmark=$2
onnx=$3
vnnlib=$4
debug=$5

pkill -9 Marabou
pkill -9 python

home="/opt"
export INSTALL_DIR="$home"
export GUROBI_HOME="$home/gurobi951/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
export GRB_LICENSE_FILE="$home/gurobi.lic"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

benchmark_dir=$(realpath "$SCRIPT_DIR"/benchmarks/)

if [[ ! -d $benchmark_dir ]]
then
    mkdir $benchmark_dir
fi

echo $benchmark

python3 -m onnxsim $onnx "$onnx"-simp
mv "$onnx"-simp $onnx

/Marabou/maraboupy/prepare_instance.py $onnx $vnnlib $benchmark_dir $debug
