import math
import turtle
import urllib.request
 
# compute and return the mean of a given list
def mean(alist):
    mean = sum(alist) / len(alist)
    return mean
 
# compute and return the standard deviation of a given list
def standardDev(alist):
    theMean = mean(alist)    
    sum = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        sum = sum + diffsq
         
    sdev = math.sqrt(sum/(len(alist)-1))
    return sdev
 
# compute and return the Pearson's correlation coefficient between two lists
def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd) 
    return corr
 
# given two lists, plot the correlation between them
def plotCorrelation(xlist, ylist):
    wn = turtle.Screen()
    minX = min(xlist)
    minY = min(ylist)
    maxX = max(xlist)
    maxY = max(ylist)
    wn.setworldcoordinates(minX, minY, maxX, maxY)
     
    t = turtle.Turtle()
    t.speed('fastest')
    turtle.tracer(0, 0)
     
    for i in range(0, len(xlist)-1):
        t.up()
        t.goto(xlist[i], ylist[i])
        t.down()
        t.dot()

# open two CSV files from the internet to read them (without downloading them locally)
url1 = urllib.request.urlopen("http://csweb.wooster.edu/jmusgrave/cs100/AMZN.csv")
url2 = urllib.request.urlopen("http://csweb.wooster.edu/jmusgrave/cs100/AAPL.csv")
# Add code to read data from http://csweb.wooster.edu/jmusgrave/cs100/NYT.csv which has the last 10 years worth of stock information
# for the New York Times.	
url3 = urllib.request.urlopen("http://csweb.wooster.edu/jmusgrave/cs100/NYT.csv")
 
# use list comprehension to parse file from website as bytestring into a list of list of strings,
# getting rid of header rows
amazonTable = url1.readlines()
appleTable = url2.readlines()
nytTable = url3.readlines()

amazonStocks = [line.decode("utf-8").split(',') for line in amazonTable[1:] ]
appleStocks = [line.decode("utf-8").split(',') for line in appleTable[1:] ]
nytStocks = [line.decode("utf-8").split(',') for line in nytTable[1:] ] 
# use list comprehension to form a list of just closing price as a floating point number
amazonClose = [ float(amazonStocks[i][4]) for i in range( len(amazonStocks) )]
appleClose = [ float(appleStocks[i][4]) for i in range( len(appleStocks) )]
nytClose = [ float(nytStocks[i] [4]) for i in range( len(nytStocks) )]
# TODO: add code here to answer the next few questions

# 1. Add code to print out Pearson’s correlation coefficient between amazonClose (the closing price of Amazon’s stock over the last 10 years),
# and appleClose (the closing price of Apple’s stock over the last 10 years).
print("The correlation between amazonClose and appleClose is",correlation(amazonClose,appleClose))

# 2. Add code to plot the correlation between amazonClose and appleClose. What does the correlation indicate?
# If Apple’s stock price goes up, is it likely that Amazon’s stock price will go up? Or down? Write your answer as a comment.
plotCorrelation(amazonClose,appleClose)

# Since the correlation between amazonClose and appleClose is 0.95, they have a very high positive correlation.
# Therefore, if Apple's stock price goes up, then Amazon's stock price will go up as well.

# 3. Compute the Pearson’s correlation coefficient to determine how NYT correlates with Apple, and how NYT correlates
# with Amazon. Print the correlation coefficient for both.
print("The correlation between nytClose and appleClose is",correlation(nytClose, appleClose))
print("The correlation between nytClose and amazonClose is",correlation(nytClose, amazonClose))

