import numpy as np

class perceptron:
    def __init__(self, in_data, lr=0.01, epochs=1000 ):
        self.lr= lr
        self.epochs= epochs
        self.weigths=np.random.rand(in_data.shape[1])

    def fit(self, x, y):

        for epochs in range(self.epochs):
            predicted=[]
            for i_index, sample in enumerate(x):
                y_hat=self.predict(sample)
                predicted.append(y_hat)
                for j_index, feature in enumerate(self.weigths):
                    delta=self.lr * (y[i_index]- y_hat)
                    delta = delta * sample[j_index]
                    self.weigths[j_index]=self.weigths[j_index] + delta
            print('[Epoch{ep}] Accuracy:{acc}'.format(ep=epochs, acc=self.calculate_accuracy(y,predicted)))

    def calculate_accuracy(self,actual,predicted):
        return sum(np.array(predicted)== np.array(actual)/float(len(actual)))


    def predict(self, x):
        res=np.sum(np.dot(x, np.transpose(self.weigths)))
        return 1 if res>0 else 0



if __name__ == '__main__':

    x=np.array([[0,0], [1,0],[1,1], [0,1]])
    y=np.array([1,1,0,0])

    p=perceptron(x)
    p.fit(x,y)