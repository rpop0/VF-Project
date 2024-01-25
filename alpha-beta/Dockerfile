# Dockerfile for vnncomp 2023

FROM ubuntu:20.04
#FROM nvidia/cuda:12.3.1-devel-ubuntu20.04

RUN echo "Starting..."
RUN apt-get update && apt-get install -y bc git # bc is used in vnncomp measurement scripts

################## install tool

ARG TOOL_NAME=alpha-beta-CROWN
ARG REPO=https://github.com/Verified-Intelligence/alpha-beta-CROWN.git
#ARG COMMIT=48a6f68267ee9e96dae7751f902139eac868fff3
ARG COMMIT=3796244e88fdd90daa44cde1d3c8a6cb77ee51b7
ARG SCRIPTS_DIR=vnncomp_scripts

#ARG TOOL_NAME=nnenum
#ARG REPO=https://github.com/stanleybak/nnenum.git
#ARG COMMIT=c93a39cb568f58a26015bd151acafab34d2d4929
#ARG SCRIPTS_DIR=vnncomp_scripts

RUN git clone $REPO
RUN cd $TOOL_NAME && git checkout $COMMIT && cd ..
RUN mkdir /vnncomp2022
RUN mv /alpha-beta-CROWN/* /vnncomp2022/

# Requirements
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bucharest
RUN apt-get update \
  && apt-get install -y wget
#  && apt-get install -y python3 \
#  && apt-get install -y python3-pip

ENV PYTHONPATH=PYTHONPATH:/vnncomp2022/complete_verifier

#################### run vnncomp
COPY scripts/vnncomp_scripts /vnncomp2022/vnncomp_scripts
RUN apt-get install -y sudo
#RUN python3 -m pip install torchvision
RUN /vnncomp2022/vnncomp_scripts/install_tool.sh v1

COPY scripts/benchmarks /vnncomp2022/benchmarks
# missing files wget https://rwth-aachen.sciebo.de/s/Erh54iS6fT3hHCr/download -O large_models.zip

# run all categories to produce out.csv
ARG CATEGORIES="nn4sys"
COPY run_all_categories.sh /vnncomp2022/run_all_categories1.sh
COPY run_single_instance.sh /vnncomp2022/run_single_instance1.sh
RUN sed 's/\r$//' /vnncomp2022/run_all_categories1.sh > /vnncomp2022/run_all_categories.sh
RUN sed 's/\r$//' /vnncomp2022/run_single_instance1.sh > /vnncomp2022/run_single_instance.sh
RUN chmod +x /vnncomp2022/run_all_categories.sh
RUN chmod +x /vnncomp2022/run_single_instance.sh

RUN git clone https://github.com/Verified-Intelligence/auto_LiRPA
WORKDIR /auto_LiRPA
RUN /root/miniconda/envs/alpha-beta-crown/bin/python setup.py install
WORKDIR /

# Verifier modified to run on CPU
#COPY scripts/complete_verifier /vnncomp2022/complete_verifier

# GPU
# Download driver
ARG DRIVER_VERSION=535.146.02
RUN aria2c -x 10 -s 10 -k 1M https://us.download.nvidia.com/XFree86/Linux-x86_64/535.146.02/NVIDIA-Linux-x86_64-535.146.02.run
RUN nvidia-smi -pm 0
RUN chmod +x ./NVIDIA-Linux-x86_64-535.146.02.run
RUN sudo apt-get install linux-headers-5.4.0-169-generic -y

# Run this manually to install the driver
# RUN sudo ./NVIDIA-Linux-x86_64-$DRIVER_VERSION.run --silent --dkms

# Should be run manually in container after installing GPU driver
#RUN /vnncomp2022/run_all_categories.sh v1 vnncomp2022/vnncomp_scripts vnncomp2022 out.csv ./counterexamples "nn4sys" all



# Debugging
#sudo ./NVIDIA-Linux-x86_64-$DRIVER_VERSION.run --no-x-check -a -s --no-kernel-module
# Remove old driver (if already installed) and reload the new one.
#RUN sudo rmmod nvidia_uvm; sudo rmmod nvidia_drm; sudo rmmod nvidia_modeset; sudo rmmod nvidia
#RUN sudo modprobe nvidia; sudo nvidia-smi -e 0; sudo nvidia-smi -r -i 0
#RUN sudo nvidia-smi -pm 1
