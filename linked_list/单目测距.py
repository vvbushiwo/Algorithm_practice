import numpy as np
import math
import sys
import scipy.io as scio
import PIL.Image as image
import scipy.misc
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import axes3d


def xrange(x):
    n=0
    while n<x:
        yield n
        n+=1


def HTline(image,stepTheta =1 ,stepRho = 1):
    rows,cols = image.shape
    L = round(math.sqrt(pow(rows - 1, 2.0)+ pow(cols - 1,2.0))) +1
    numtheta = int(180.0 / stepTheta)
    numRho = int(2 * L/stepRho + 1 )
    accumulator = np.zeros((numRho, numtheta), np.int32)
    accuDict = {}
    for k1 in range(numRho):
        for k2 in range(numtheta):
            accuDict[(k1,k2)] = []

    for y in range(rows):
        for x in range(cols ):
            if(image[y][x] == 255):
                for m in range(numtheta):
                    rho = x*math.cos(stepTheta*m/180.0*math.pi)+y*math.sin(stepTheta*m/180.0*math.pi)
                    n = int(round(rho+L)/stepRho)
                    accumulator[n,m] += 1
                    accuDict[(n,m)].append((y,x))

    return accumulator,accuDict


if __name__ == "__main__":
    imgData = image.open("1.png")
    L = imgData.convert('L')
    img = np.array(L)
    edge = cv2.Canny(img, 50, 160)
    rows, cols = edge.shape
    for i in range(rows):
        for j in range(cols):
            if edge[i][j]  0:

                if yy1 > yy2:
                    cc[i][j] = 255
                else:
                    cc[i][j] = 0
    scipy.misc.imsave('outfile.jpg', cc)
    cv2.imshow("edge",edge)
    cv2.waitKey(0)
    accumulator, accuDict = HTline(edge, 1, 1)
    rows,cols = accumulator.shape
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    X,Y = np.mgrid[0:rows:1, 0:cols:1]
    surf = ax.plot_wireframe(X,Y,accumulator,cstride=1,rstride=1,color = 'gray')
    ax.set_xlabel(u"$\\rho$")
    ax.set_ylabel(u"$\\theta$")
    ax.set_zlabel("accumulator")
    ax.set_zlim3d(0, np.max(accumulator))

    grayAccu = accumulator/float(np.max(accumulator))
    grayAccu = 255*grayAccu
    grayAccu = grayAccu.astype(np.uint8)

    voteThresh = 255
    for r in xrange(rows):
        for c in xrange(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r, c)]
                cv2.line(img,points[0],points[len(points) - 1], (255),2)
    cv2.imshow('accumulator', grayAccu)
    cv2.imshow("I",img)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()




