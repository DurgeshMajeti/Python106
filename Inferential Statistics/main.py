import numpy as np
import distributions as db
import matplotlib.pyplot as plt
import scipy.stats as stats

binomial = np.random.binomial(100,0.5,1000)
exponential = np.random.exponential(3,1000)
exponential -= exponential%1  ##truncating data
normal = np.random.normal(5,1,1000)
normal -= normal%0.1  ##truncating data
poisson = np.random.poisson(3,1000)
std_nrm = np.random.normal(0,1,1000)
std_nrm -= std_nrm%0.1  ##truncating data
uniform = np.random.uniform(1,5,1000)
uniform -= uniform%0.1  ##truncating data

##########Binomial##############
binomial = np.sort(binomial)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++BINOMIAL++++++++++++")
print("Maximum            :",db.maximum(binomial))
print("Minimum            :",db.minimum(binomial))
print("Mean               :",db.mean(binomial))
print("Median             :",db.median(binomial))
print("Variance           :",db.var(binomial,db.mean(binomial)))
print("Standard Deviation :",db.std_dev(binomial,db.mean(binomial)))
print("IQR                :",db.iqr(binomial))
db.dotplot(binomial,axs[0,0])
y = stats.binom.pmf(binomial,100,0.5)*1000 ##get pdf for each point in x
db.histogram(binomial,y,axs[0,1])
out = db.boxplot(binomial,axs[1,0])
db.qq_plot(binomial,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()

#############Exponential##################
exponential = np.sort(exponential)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++EXPONENTIAL++++++++++++")
print("Maximum            :",db.maximum(exponential))
print("Minimum            :",db.minimum(exponential))
print("Mean               :",db.mean(exponential))
print("Median             :",db.median(exponential))
print("Variance           :",db.var(exponential,db.mean(exponential)))
print("Standard Deviation :",db.std_dev(exponential,db.mean(exponential)))
print("IQR                :",db.iqr(exponential))
db.dotplot(exponential,axs[0,0])
y = stats.expon.pdf(exponential,0)*400  ##get pdf for each point in x
db.histogram(exponential,y,axs[0,1])
out = db.boxplot(exponential,axs[1,0])
db.qq_plot(exponential,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()

##########Normal##############
normal = np.sort(normal)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++NORMAL++++++++++++")
print("Maximum            :",db.maximum(normal))
print("Minimum            :",db.minimum(normal))
print("Mean               :",db.mean(normal))
print("Median             :",db.median(normal))
print("Variance           :",db.var(normal,db.mean(normal)))
print("Standard Deviation :",db.std_dev(normal,db.mean(normal)))
print("IQR                :",db.iqr(normal))
db.dotplot(normal,axs[0,0])
y = stats.norm.pdf(normal,5,1)*200
db.histogram(normal,y,axs[0,1])
out = db.boxplot(normal,axs[1,0])
db.qq_plot(normal,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()

##########Poisson##############
poisson = np.sort(poisson)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++POISSON++++++++++++")
print("Maximum            :",db.maximum(poisson))
print("Minimum            :",db.minimum(poisson))
print("Mean               :",db.mean(poisson))
print("Median             :",db.median(poisson))
print("Variance           :",db.var(poisson,db.mean(poisson)))
print("Standard Deviation :",db.std_dev(poisson,db.mean(poisson)))
print("IQR                :",db.iqr(poisson))
db.dotplot(poisson,axs[0,0])
y = stats.poisson.pmf(poisson,3)*600
db.histogram(poisson,y,axs[0,1])
out = db.boxplot(poisson,axs[1,0])
db.qq_plot(poisson,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()

##########Standard Normal##############
std_nrm = np.sort(std_nrm)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++STANDARD NORMAL++++++++++++")
print("Maximum            :",db.maximum(std_nrm))
print("Minimum            :",db.minimum(std_nrm))
print("Mean               :",db.mean(std_nrm))
print("Median             :",db.median(std_nrm))
print("Variance           :",db.var(std_nrm,db.mean(std_nrm)))
print("Standard Deviation :",db.std_dev(std_nrm,db.mean(std_nrm)))
print("IQR                :",db.iqr(std_nrm))
db.dotplot(std_nrm,axs[0,0])
y = stats.norm.pdf(std_nrm)*200
db.histogram(std_nrm,y,axs[0,1])
out = db.boxplot(std_nrm,axs[1,0])
db.qq_plot(std_nrm,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()

##########Uniform##############
uniform = np.sort(uniform)
fig,axs = plt.subplots(2,2,figsize = (10,10))
print("+++++++++++UNIFORM++++++++++++")
print("Maximum            :",db.maximum(uniform))
print("Minimum            :",db.minimum(uniform))
print("Mean               :",db.mean(uniform))
print("Median             :",db.median(uniform))
print("Variance           :",db.var(uniform,db.mean(uniform)))
print("Standard Deviation :",db.std_dev(uniform,db.mean(uniform)))
print("IQR                :",db.iqr(uniform))
db.dotplot(uniform,axs[0,0])
y = stats.uniform.pdf(uniform,1,5)*200
db.histogram(uniform,y,axs[0,1])
out = db.boxplot(uniform,axs[1,0])
db.qq_plot(uniform,axs[1,1])
outliers = list(item.get_ydata() for item in out['fliers'])
outliers = list(outliers[0])
outliers,y = db.freq(outliers)
print("Outliers           :",outliers)
plt.show()