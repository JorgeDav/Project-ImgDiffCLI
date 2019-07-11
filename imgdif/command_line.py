import imgdif 

def main():
    args=imgdif.input()
    score=imgdif.diff(args)
    out=imgdif.output(score)
    print ("Score: {} %".format(score*100))
    print(out)
    
