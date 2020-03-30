import requests
import numpy
import tensorflow as tf
import tflearn
model = tf.keras.Sequential()


# remove active players from data set later -- DONE

#to load csv and indicate the first column represents labels
from tflearn.data_utils import load_csv

#Mehdi Abdesmad,/A/AbdeMe00.htm,DE,False,1.0,False
data, labels = load_csv('DataModeling/positionCSVs/RB.csv', target_column=3, categorical_labels=True, n_classes= 2, columns_to_ignore=[1,2,5,6])

#for p in data:
#    if p[1]=='female':
 #       p[1]=1
  #  else: p[1]=0



net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net,32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=10, batch_size=16, show_metric=True)

print("My odds of surviving on the titanic")
print(model.predict([[12]])[0][1])



#passenger class, gender, age, siblings/spouses on board, parents,children on board , money spent on ticket
#chance of dying, chance of surviving
