import click
from PIL import Image
import cv2
import os,shutil

@click.group()
def cli():
    pass

@cli.command()
@click.argument('image')
@click.argument('filename')
def mask(image,filename):
    '''adds thuglife mask to image'''
    checkImage = imageFilecheck(image)
    if checkImage == True:
        addingMask(image,filename)
    else:
        click.echo("Must enter valid file type")

def imageFilecheck(image):
    '''checks if we have the correct
    file type'''
    if image.endswith('.png'):
        return True
    elif image.endswith('.jpeg'):
        return True
    else:
        return False



@cli.command()
@click.argument('filename')
def view(filename):
    '''takes the file name to view image eg me.png'''
    image = Image.open(filename)
    image.show(filename)
    



def loadThuglifeMask():
   '''loads the file directory of the
   thuglife mask'''
   fileDirectory = 'img/thug.png'
   return fileDirectory


def addingMask(image,filename):
    '''adds thug life mask to image'''
    startingImage = Image.open(image)
    fileformat = '.png'
    filename = str(filename)+fileformat
    readImage = cv2.imread(image)
    maskPath = loadThuglifeMask()
    gray = cv2.cvtColor(readImage,cv2.COLOR_BGR2GRAY)
    face_cassade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
    faces = face_cassade.detectMultiScale(gray,1.15)
    for  (x,y,w,h) in faces:
        cv2.rectangle(readImage,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('face',readImage)
        cv2.waitKey(0)
        mask =  Image.open(maskPath)
        mask = mask.resize((w,h),Image.ANTIALIAS)
        offset = (x,y)
        startingImage.paste(mask,offset,mask=mask)
    startingImage.save(filename)






