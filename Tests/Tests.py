import pytest


def checkimagefile(image):
    if image.endswith('.png'):
        return True
    elif image.endswith('.jpeg'):
        return True
    else:
        return False

def checkemptyimage(image):
    if image != None:
        return True
    else:
        return False


def checkimagejpeg():
    fileJpeg = 'test.jpeg'
    assert(checkimagefile(fileJpeg)) == True

def checkimagepng():
    filepng = 'test.png'
    assert(checkimagefile(filepng)) == True

def checkemptyfile():
    nonefile =  None
    assert(checkemptyimage(nonefile)) == False

def checkiffileisnotempty():
    existingfile = 'this.jpeg'
    assert(checkemptyimage(existingfile)) == True


