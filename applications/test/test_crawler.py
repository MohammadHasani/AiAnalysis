import os
import shutil

import pytest

from applications.constant import ROOT_DIR
from applications.model.crawler import Crawler


def get_test_repo():
    path = ROOT_DIR + "/repos/test/"

    return path


def write_new_file(path, file_name, content):
    with open(path + file_name, "a") as writer:
        writer.write(content)
    return writer


@pytest.fixture()
def create_folder_and_files():
    path = get_test_repo()
    does_folder_exist = os.path.isdir(path)
    if does_folder_exist:
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)

    py_content_1 = '''# dummy ai 01
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
    '''
    py_content_2 = '''# dummy ai 02
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(8, activation='relu'))
model.add(       Dense(8, activation='relu'))
model.add ( Dense(      8, activation   =  'relu'))
model.add (   Dense (8, activation='relu'))
model.add ( Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8 , activation   =  'relu'))
model.add(Dense(8, activation=
'relu')   )
model.add(Dense(1, activation='relu'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))'''
    py_content_3 = '''# dummy ai 03
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12
                , input_dim=8
                , activation='relu')  )
model = Sequential()
model.add(Dense(12, input_dim=8, activation
='relu'))
model.add(Dense(8, activation='relu'))
model.add(       Dense(8, activation   =



'relu'))
model.add ( Dense(8 , activation='relu'     ))
model.\
add ( Dense     ( 8, activation='relu'))
model.add ( Dense(8, activation=

'sigmoid')   )
model.add(Dense(8, activation='sigmoid'))
model.add(Dense   (8, activation='sigmoid'))
model.add\
    (Dense(8, activation='relu'))
model.    add (Dense
          (8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))'''
    py_content_4 = '''# dummy ai 03
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))'''

    write_new_file(path + '/', "example.py", py_content_1)
    write_new_file(path + '/', "example2.py", py_content_2)
    write_new_file(path + '/', "example.txt", "print('hi from second new python file !')")

    path_rec = path + '/rec1'
    os.makedirs(path_rec)

    write_new_file(path_rec + '/', "example.py", py_content_3)
    write_new_file(path_rec + '/', "example2.py", py_content_4)
    write_new_file(path_rec + '/', "example.txt", "print('hi from second new python file recursively!')")

    yield
    # teardown
    shutil.rmtree(path)


def test_crawl_all_python_files_of_folder(create_folder_and_files):
    crawler_obj = Crawler()
    path = get_test_repo()

    file_list = crawler_obj.get_all_python_files_in_folder(path)
    assert file_list == [path + 'example.py', path + 'example2.py', path + 'rec1/example.py',
                         path + 'rec1/example2.py']


def test_analysis_python_files(create_folder_and_files):
    crawler_obj = Crawler()
    path = get_test_repo()
    file_list = crawler_obj.get_all_python_files_in_folder(path)
    classify_result = []
    relu_result_list = []
    sigmoid_result_list = []
    for file in file_list:
        classify_result.append(crawler_obj.classify_file(file))

        relu_result = crawler_obj.analysis_python_file(file, crawler_obj.relu_regex)
        sigmoid_result = crawler_obj.analysis_python_file(file, crawler_obj.sigmoid_regex)
        relu_result_list.append(relu_result)
        sigmoid_result_list.append(sigmoid_result)

    assert relu_result_list == [17, 9, 8, 0]
    assert sigmoid_result_list == [4, 0, 4, 0]
    assert classify_result == ['high', 'low', 'medium', None]
