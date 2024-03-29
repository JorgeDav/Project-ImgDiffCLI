#funct.py , __init__.py
# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2


def inputs():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--first", required=True,
    help="first input image")
    ap.add_argument("-s", "--second", required=True,
    help="second")
    return vars(ap.parse_args())

def diff(args):
    # load the two input images
    image1 = cv2.imread(args["first"])
    image2 = cv2.imread(args["second"])

    # convert the images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(gray1, gray2, full=True)
    return score

def output(score):
    if score == 1:
        return(True)
    else:
        return(False)

def final():
    args=inputs()
    score=diff(args)
    out=output(score)
    print ("Score: {} %".format(score*100))
    print(out)
