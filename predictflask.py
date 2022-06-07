from flask import Flask
from matplotlib import pyplot as plt

import cv2 
import numpy as np
import tensorflow as tf
from object_detection.builders import model_builder
from object_detection.utils import config_util

app = Flask(__name__)
CONFIGS = config_util.get_configs_from_pipeline_file('./pretrained_model/pipeline.config')
MODEL = model_builder.build(model_config=CONFIGS['model'], is_training=False)


@app.route('/predict')
def predict():
    #get image by http-get
    image_from_api = #GET API
    img = cv2.imread(image_from_api)
    images_np = np.array(img)

    # change file image into numpy array
    input_tensor = tf.convert_to_tensor(np.expand_dims(images_np, 0), dtype=tf.float32)

    image, shapes = MODEL.preprocess(input_tensor)
    prediction_dict = MODEL.predict(image, shapes)
    detections = MODEL.postprocess(prediction_dict, shapes)

    print(detections)
    
    return detections['detection_classes']

if __name__ == '__main__':
    app.run(host='127.0.0.1')