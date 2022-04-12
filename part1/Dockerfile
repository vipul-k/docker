FROM tensorflow/tensorflow:latest-py3 AS base

RUN pip install imageio==2.15.0

ADD train.py classify.py /

RUN ["python",  "./train.py"]
