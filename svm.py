#SVM
import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline

def svm(w,lr,epochs):
    for ep in range(1,epochs):
        for data_point in data:
            x=data_point[0:len(data_point)-1]
            y=data_point[len(data_point)-1]
            if y*(np.dot(x,w)) < 1:
                w=w-lr*(float(epochs/ep))*(2*(1/ep)*w-x*y)
            else:
                w=w-lr*(float(epochs/ep))*(2*(1/ep)*w)
    print(w)

def plot_result(data,w):
    for data_point in data:
        x=data_point[0:len(data_point)-1]
        y=data_point[len(data_point)-1]
        if y == -1:
            plt.scatter(x[0],x[1],s=120,marker='_',linewidths=2)
        else:
            plt.scatter(x[0],x[1],s=120,marker='+',linewidths=2)
    #testing
    plt.scatter(6,3,s=120,marker='+',linewidths=2,color='yellow')
    plt.scatter(2,4,s=120,marker='_',linewidths=2,color='yellow')
    x2=[w[0],w[1],-w[1],w[0]]
    x3=[w[0],w[1],w[1],-w[0]]

    x2x3=np.array([x2,x3])
    X,Y,U,V=zip(*x2x3)
    ax=plt.gca()
    ax.quiver(X,Y,U,V,scale=3,color='red')
    plt.show()
    plt.plot([0,0],[1.245,1.3125])

if __name__ == '__main__':
    print('about to start')
    data=np.array([[2,3,-1],[4,1,-1],[4,7,+1],[3,4,-1],[6,8,1],[7,2,1]])
    w=np.zeros(len(data[0])-1)
    epochs=100
    lr=0.05
    svm(w,lr,epochs)
    plot_result(data,w)
