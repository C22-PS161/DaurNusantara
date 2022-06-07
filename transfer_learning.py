from posixpath import abspath
import tensorflow as tf
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
import os

PRETRAINED_MODEL_PATH = os.path.abspath('./pretrained_model')
TFRECORD_PATH = os.path.abspath('./tfrecord_dataset')

def customize_pipeline_config(pipeline_config_path):
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    with tf.io.gfile.GFile(pipeline_config_path, "r") as fio:                                                                                                                                                                                                                     
        proto_str = fio.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)
    
    pipeline_config.model.center_net.num_classes = 8
    pipeline_config.train_config.batch_size = 4
    pipeline_config.train_config.fine_tune_checkpoint = PRETRAINED_MODEL_PATH + '/centernet_resnet50_v1_fpn_512x512_coco17_tpu-8/checkpoint/ckpt-0'
    pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
    pipeline_config.train_input_reader.label_map_path= PRETRAINED_MODEL_PATH + '/labels.pbtxt'
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [TFRECORD_PATH + '/train.record']
    pipeline_config.eval_input_reader[0].label_map_path = PRETRAINED_MODEL_PATH + '/labels.pbtxt'
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [TFRECORD_PATH + '/test.record']
    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile(pipeline_config_path, "wb") as f:                                                                                                                                                                                                                     
        f.write(config_text)   

customize_pipeline_config(PRETRAINED_MODEL_PATH + "/pipeline.config")

