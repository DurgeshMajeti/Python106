import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def freq(data):  ##returns data nad it's frequency
    frequency = {}
    for i in data:
        if(i in frequency.keys()):
            frequency[i]+=1
        else:
            frequency[i]=1
    return list(frequency.keys()),list(frequency.values())

def maximum(data):  ##returns maximum of sorted data
    return data[-1]

def minimum(data):  ##returns minimum of sorted data
    return data[0]

def iqr(data):  ##returns iqr of sorted data
    q1 = int(len(data)/4)
    q3 = int(3*len(data)/4)
    return data[q3]-data[q1]  ##iqr is the difference between q1 and q3

def mean(data):  ##returns mean of the data
    sum = 0
    for i in data:
        sum+=i
    avg = sum/len(data)
    return avg

def median(data):  ##returns median of the sorted data
    size = len(data)
    if(size%2 == 1):
        med = data[int(size/2)]
    else:
        med = (data[int(size/2)] + data[int(size/2)-1])/2
    return med

def std_dev(data,avg):  ##returns standard deviation of the data
    vari = var(data,avg)  ##uses variance method which is available in the library
    return np.sqrt(vari)

def var(data,avg):  ##returns variance of the data
    diff = 0
    for i in data:
        diff += (i-avg)**2
    vari = diff/(len(data)-1)  ## formula for sample variance
    return vari

def dotplot(data,ax):  ##attaches scatterplot of data  as dotplot to the axes
    ax.set_title("Dot Plot")
    x,y = freq(data)
    for i in range(len(x)):
        for j in range(y[i]):
            ax.scatter(x[i],j/3,color='green',s=5)

def histogram(data,pd,ax):  ##attaches histogram of the data to the axes
    ax.hist(data,bins=25,color='chocolate')
    ax.set_title("Histogram and Density Curve")
    x,y = freq(data)
    ax.plot(x,y,color='red')  ##plot the density curve of the data
    ax.plot(data,pd,color='navy')
    ax.legend([plt.Line2D([0],[0],color='navy'),(plt.Line2D([0],[0],color='red'))],['Density curve','Sample Density Curve'])

def boxplot(data,ax):  ##returns boxplot dictionary
    ax.set_title("Box Plot")
    return(ax.boxplot(data,vert = True))

def qq_plot(data,ax):  ##attaches qq_plot to the axes
    q = []
    for i in range(len(data)):
        q.append(stats.norm.ppf((i+0.5)/len(data)))
    ax.scatter(data,q,s=5,color='darkgoldenrod')
    #ax.plot(data,q,color='green')
    ax.set_title("Q-Q Plot")
