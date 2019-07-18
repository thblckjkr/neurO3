# Basicamente, es un wraper para el archivo que nos dejo el profe
# @thblckjkr

import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

# 2.7 syntax works on 3.7 on my machine? why? idk.

from tensorflow import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Activation
from tensorflow.python.keras import optimizers

class recognition:
	Inputs = []
	Targets = []
	epochs = 6000
	inputsize = 1
	outputsize = 1

	def __init__(self, ui):
		self.ui = ui

	def set(self, Inputs, Targets, Test, **args):
		self.Inputs = Inputs
		self.Targets = Targets

		# grab sizes of inputs
		self.inputsize = len(Inputs[0])
		self.outputize = len(Targets[0])

		# TODO: this
		# if "epochs" in args.items()
		self.epochs = args['epochs']
		self.middlesize = args['middlesize']
		self.test = Test

		self.ui.show("The size of input network is: " + str(self.inputsize), "warning")
		self.ui.show("The size of the middle network is: " + str(self.middlesize), "warning" )
		self.ui.show("The size of output network is: " + str(self.outputize), "warning" )
		self.ui.show("The epochs to test are: " + str(self.epochs), "warning" )

	def analyze(self):
		# Transform inputs into numpy arrays (?)
		Inputs = np.asarray(self.Inputs)
		Targets = np.asarray(self.Targets)

		# TODO: create layers with push and a for
		# Create the model of layers
		model = Sequential([
			keras.layers.Dense(self.inputsize, activation=tf.nn.sigmoid, input_dim=self.inputsize),
			keras.layers.Dense(self.middlesize, activation=tf.nn.sigmoid),
			keras.layers.Dense(self.outputize, activation=tf.nn.sigmoid)
		])

		sgd = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

		model.compile(
			optimizer=sgd, 
			loss='mean_squared_error',
			metrics=['accuracy']
		)

		# Create a model
		history = model.fit(Inputs, Targets, epochs=self.epochs)

		# Create a test case
		test = np.asarray(self.test)
		predictions = model.predict(test)


		print("Estimaciones = ")
		print(predictions)
		print(np.round(predictions, 2))


		# summarize history for accuracy
		plt.plot(history.history['acc'])
		#plt.plot(history.history['val_acc'])
		plt.title('model accuracy')
		plt.ylabel('accuracy')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()
		# summarize history for loss
		plt.plot(history.history['loss'])
		#plt.plot(history.history['val_loss'])
		plt.title('model loss')
		plt.ylabel('loss')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()
