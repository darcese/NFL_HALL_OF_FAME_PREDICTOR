#import requests
import numpy
import tflearn



#to load csv and indicate the first column represents labels
from tflearn.data_utils import load_csv #also get rid of players who are still active later from the set
data, labels = load_csv('positionCSVs/QB.csv', target_column=3, categorical_labels=True, n_classes= 2, columns_to_ignore=[0,1,2,5])

for p in data:
    if p[3]=='False':
        p[3]=0
    else: p[3]=1

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
#print(model.predict([[8]])[0][1])



#passenger class, gender, age, siblings/spouses on board, parents,children on board , money spent on ticket
#chance of dying, chance of surviving
