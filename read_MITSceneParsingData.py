__author__ = 'charlie'
import numpy as np
import os
import random
from six.moves import cPickle as pickle
from tensorflow.python.platform import gfile
import glob

import TensorflowUtils as utils

# DATA_URL = 'http://sceneparsing.csail.mit.edu/data/ADEChallengeData2016.zip'
DATA_URL = 'http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip'


def read_dataset(data_dir):

    result = create_image_lists(data_dir)
    training_records = result['training']
    validation_records = result['validation']
    del result

    return training_records, validation_records


def create_image_lists(image_dir):
    if not gfile.Exists(image_dir):
        print("Image directory '" + image_dir + "' not found.")
        return None
    directories = ['training', 'validation']
    image_list = {}

    for directory in directories:
        file_list = []
        image_list[directory] = []
       # file_glob = os.path.join(image_dir, "images", directory, '*.' + 'jpg')
        file_glob = os.path.join(image_dir, 'images', directory, '*.jpg')
 #       print(file_glob) test
        file_list.extend(glob.glob(file_glob))
  #      print(file_list) test
        if not file_list:
            print('No files found')
            
        else:
            for f in file_list:
                #filename = os.path.splitext(f.split("/")[-1])[0]
                filename = os.path.splitext(f.split("\\")[-1])[0]
                annotation_file = os.path.join(image_dir, "annotations", directory, filename + '.png')
                if os.path.exists(annotation_file):
                    record = {'image': f, 'annotation': annotation_file, 'filename': filename}
                    image_list[directory].append(record)
                else:
                    print("Annotation file not found for %s - Skipping" % filename)

        random.shuffle(image_list[directory])
        no_of_images = len(image_list[directory])
        print ('No. of %s files: %d' % (directory, no_of_images))

    return image_list

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
