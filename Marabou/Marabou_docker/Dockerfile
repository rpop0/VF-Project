# Dockerfile for vnncomp 2021
# this is an example that uses the tool_example scripts

FROM ubuntu:20.04

RUN echo "Starting..."
RUN apt-get update && apt-get install -y bc git # bc is used in vnncomp measurement scripts

################## install tool

ARG TOOL_NAME=Marabou
ARG REPO=https://github.com/NeuralNetworkVerification/Marabou.git
#ARG COMMIT=48a6f68267ee9e96dae7751f902139eac868fff3
ARG COMMIT=a2077b465c71b11f8596ea07f6858a704ec4e604
ARG SCRIPTS_DIR=vnn-comp-scripts

#ARG TOOL_NAME=nnenum
#ARG REPO=https://github.com/stanleybak/nnenum.git 
#ARG COMMIT=c93a39cb568f58a26015bd151acafab34d2d4929
#ARG SCRIPTS_DIR=vnncomp_scripts

RUN git clone $REPO
RUN cd $TOOL_NAME && git checkout $COMMIT && cd ..

# Requirements
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bucharest
RUN apt-get update \
  && apt-get install -y wget \
  && apt-get install -y python3 \
  && apt-get install -y python3-pip \
  && apt-get install -y cmake protobuf-compiler
#  && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install numpy
#RUN /$TOOL_NAME/$SCRIPTS_DIR/install_tool.sh v1
#ENV PYTHONPATH=PYTHONPATH:/Marabou/maraboupy/

#################### run vnncomp
COPY scripts/vnncomp_scripts /vnncomp2022/vnncomp_scripts
#RUN mkdir -p /mytest/build1

RUN /vnncomp2022/vnncomp_scripts/install_tool.sh v1

ENV PYTHONPATH=/Marabou

COPY scripts/benchmarks /vnncomp2022/benchmarks

# run all categories to produce out.csv
ARG CATEGORIES="nn4sys"
COPY run_all_categories.sh /vnncomp2022/run_all_categories.sh
COPY run_single_instance.sh /vnncomp2022/run_single_instance.sh

RUN pip install torchvision 
COPY new_prepare.py /Marabou/maraboupy/prepare_instance.py
COPY VNNLibParser.py /Marabou/maraboupy/VNNLibParser.py

RUN vnncomp2022/run_all_categories.sh v1 vnncomp2022/vnncomp_scripts vnncomp2022 out.csv ./counterexamples "$CATEGORIES" all
#RUN vnncomp2022/run_all_categories.sh v1 /$TOOL_NAME/$SCRIPTS_DIR vnncomp2022 out.csv ./counterexamples "$CATEGORIES" all
