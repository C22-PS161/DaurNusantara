# DaurNusantara
> Object detection using Tensorflow

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Libraries](#libraries)
* [Setup](#setup)
* [Train and Evaluate](#train-and-evaluate)
* [Object Detection Labels](#object-detection-labels)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Object detection using Tensorflow with pre-trained model Centernet. 

## Screenshots
![Example screenshot](./img/screenshot(1).png)

## Libraries
* Matplotlib
* Pandas
* Numpy
* Pillow
* Tensorflow - version 2.9.1
* Apache-beam
* lxml
* Cython
* Contextlib2
* Tf-slim
* Six
* Pycocotools
* lvis
* Pyparsing - version 2.4.7
* object-detection
* tf-object-detection-util
* protoc - version 3.19.4
* git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

## Setup
1. git clone <a href=https://github.com/tensorflow/models.git>tensorflow-model</a>
2. Download <a href=https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.4>protoc 3.19.4</a>
3. Pindah ke folder `/research`
3. `pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI`
4. `protoc object_detection/protos/*.proto --python_out=.`
5. `cp tensorflow\research\object_detection\packages\tf2\setup.py`
6. `pip install --upgrade`
7. `pip install .`
8. Test the installation with `python object_detection/builders/model_builder_tf2_test.py` (inside models\research)

## Train and Evaluate
1. Annotate image using <a href=https://makesense.ai>Makesense</a>
2. Run script.py to create CSV files
3. Run split.py to split CSV files into train and test CSV files
4. Run `python generate_tfrecord.py --csv_input='[CSV FILE]' --output_path='[OUPUT FILE RECORD]'` to generate train and test TFRecord
5. Download pre-trained model from <a href=https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md>Tensorflow 2 model zoo</a> 
6. Change .pbtxt file according to your category images label
7. Run `python transfer_learning.py`
8. (Train model) Run `python model_main_tf2.py` from tensorflow model 
    >"Tensorflow\models\research\model_main_tf2.py" --model_dir="./models" --pipeline_config_path="./pretrained_model/pipeline.config" --num_train_steps=2000
9. (Evaluate model) Run `python model_main_tf2.py` from tensorflow model 
    >"Tensorflow\models\research\object_detection\model_main_tf2.py" --model_dir="./models" --pipeline_config_path="./pretrained_model/pipeline.config" --checkpoint_dir="./models"
10. (WIP)

## Object Detection Labels
* kantong (ID: 0) 
* kertas (ID: 1) 
* piring (ID: 2) 
* sampah_organik (ID: 3)
* kardus (ID: 4) 
* cup (ID: 5) 
* kaleng (ID: 6)
* botol (ID: 7)

## Status
Project is: _in progress_

## Inspiration
Project inspired by Google Bangkit Product Capstone Project.

## Contact
> If you have a question, please write `Object Detection` as email's subject
* Benidictus Galih Mahar Putra - benidictusgalih@gmail.com
* Leo Cardhio Sih Pratama - leocardhio@gmail.com
* Victor Sean Lambert - vlotusan@gmail.com