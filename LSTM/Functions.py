import numpy as np
import configparser

config = configparser.ConfigParser()
config.read('project.properties')
n_classes = int(config.get('InputParameters', 'n_classes'))

# Define function to generate batches of a particular size

def extract_batch_size(_train, step, batch_size):
    shape = list(_train.shape)
    shape[0] = batch_size
    batch = np.empty(shape)

    for i in range(batch_size):
        index = ((step - 1) * batch_size + i) % len(_train)
        batch[i] = _train[index]

    return batch


# %%

# Define to function to create one-hot encoding of output labels

def one_hot_vector(y_, n_classes=n_classes):
    # e.g.:
    # one_hot(y_=[[2], [0], [5]], n_classes=6):
    #     return [[0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]

    y_ = y_.reshape(len(y_))
    return np.eye(n_classes)[np.array(y_, dtype=np.int32)]  # Returns FLOATS