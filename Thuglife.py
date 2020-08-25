import click
from PIL import image
import cv2

@click.group()
def cli():
    pass

@cli.command()
@click.argument('image')

def mask(image):
    '''adds thuglife mask to image'''
    checkImage = imageFilecheck(image)
    checkForemptyFile = checkEmptyfile(image)
    if checkImage == True and checkForEmptyFile !=True:
        addingMask(image)
    else:
        click.echo("Must enter valid file type")

def imageFilecheck(image):
    '''checks if we have the correct
    file type'''
    if image.endswith('.png'):
        return True
    elif image.endswith('jpeg'):
        return True
    else:
        return False

def checkEmptyfile(image):
    '''checks for empty file'''
    if image!= None:
        return True
    else:
        return False


def loadThuglifeMask():
   '''loads the file directory of the
   thuglife mask'''
    fileDirectory = 'img/thug.png'
    return fileDirectory


def addingMask(image):
    '''adds thug life mask to image'''
    startingImage = Image.open(image)
    readImage = cv2.imread(image)
    maskPath = loadThuglifeMask()
    gray = cv2.cvtColour(readImage,cv2.COLOUR_BGR2GRAY)
    face_cassade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
    faces = face_cassade.detectMultiScale(gray,1.15)
    for face in faces:
        cv2.rectangle(readImage,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('face',readImage)
        cv2.waitKey(0)
        mask =  Image.open(maskPath)
        mask = mask.resize((x,h),Image,Image.ANTIALIAS)
        offset = (x,y)
        startingImage.paste(mask,offset,mask=mask)
    startImage.save('out.png')


