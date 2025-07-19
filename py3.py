from numpy import loadtxt
from keras.layers import Dense
from keras.models import Sequential
dataset=loadtxt('/pima-indians-diabetes.csv',delimiter=',')
X=dataset[:,0:8]
Y=dataset[:,8]
X
model=Sequential()
model.add(Dense(12,activation='relu',input_dim=8))
model.add(Dense(8,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X,Y,epochs=100,batch_size=4,verbose=0)
_,accuracy=model.evaluate(X,Y)
print('Accuracy:%.2f'%(accuracy*100))
