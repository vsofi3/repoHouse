import random
import math
import turtle

def readFile(filename):
    '''
    (text file)-> dictionary

    Takes in a text file and returns a dictionary of the coordinates
    of every earthquake in the file.
    '''
    with open(filename,'r') as file:
        file.readline()
        datadict = {}
        key = 0

        for aline in file:
            items = aline.strip().split(',')
            key +=1
            lat = float(items[1])
            lon = float(items[2])
            datadict[key] = [lon,lat]

        return datadict

# this part of the code is working (gave me 540 lines of text)

def euclidD(pointA,pointB):
    '''
    (list,list)->float

    Takes a list (pointA) and another list (pointB) and calculates the
    distance between the two points, accessing the first and second elements
    as x and y coordinates. Returns the distance. First longitude, then
    latitude.

    Example of code:
    >>>euclidD([-178.4753,-33.6142],[74.6387,35.6305])
    '''
    total = 0
    for index in range(len(pointA)):
        diff = (pointA[index]-pointB[index])**2
        total+= diff

    euclidDistance = math.sqrt(total)
    return euclidDistance
    
    
def createCentroids(k,datadict):
    '''
    (int,dictionary)-> list

    Takes the number of centroids (k) and the data dictionary as parameters.
    Function continues until k centroids have been selected and placed in the
    list. Then returns that list. 
    '''
    centroids=[]
    centroidCount = 0
    centroidKeys =[]

    while centroidCount<k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount+=1
    return centroids

def createClusters(k, centroids, datadict, repeats):
    '''

    '''
    for apass in range(repeats):
        print('****PASS',apass,'****')
        clusters = []
        for i in range (k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints=datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen!= 0:
                    sums[ind] = sums[ind]/clusterLen

            '''
            for c in clusters:
                print('CLUSTER')
                for key in c:
                    print(datadict[key], end=' ')
                print()

            '''
            

            centroids[clusterIndex] = sums
        return clusters

def eqDraw(k, eqDict, eqClusters): 
    '''
    (int,dictionary, list)-> None

    Takes in three parameters: k(the number of clusters), eqDict(the earthquake
    data dictionary), and eqClusters(the list of clusters generated for the
    earthquake data by the k-means cluster analysis). eqDar will comprise the
    drawing code that is included in visualizeQuakes. 
    '''

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap.gif')
    quakeWin.screensize(1800,900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()
    colorlist=['red','green','blue','orange','cyan','yellow']


    for clusterIndex in range(6): 
        quakeT.color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]: #I need to access clusters from
                                              #visualizeQuakes function
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            quakeT.goto(lon*wFactor,lat*hFactor)
            quakeT.dot()

    turtle.done()

    quakeWin.exitonclick()
 
    
def visualizeQuakes(k, r, datafile):
    '''
    (int,int,file)-> plot

    Takes k(the number of clusters), r(the number of times to repeat cluster
    analysis) and the datafile as parameters. The function will call
    createCentroids and createClusters. Will also call eqDraw, to plot the
    earthquake data on the world map. Should return None.
    '''
    datadict = readFile(datafile)
    quakeCentroids = createCentroids(6, datadict)
    clusters = createClusters(6, quakeCentroids, datadict, 7)

    eqDraw(k, datadict, clusters)

    return None

def main():
    k = 4
    r = 5
    f = 'equakes_world_50f_2019.csv'
    visualizeQuakes(k,r,f)
    return None

main()

    

