import funct 

def main():
    args=funct.input()
    score=funct.diff(args)
    out=funct.output(score)
    print ("Score: {} %".format(score*100))
    print(out)
   
main()
