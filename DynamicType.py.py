import time
x=0
print("\n                                  **********Type Speed Tester**********                ")
print("                             Enhance you typing speed by using us as a platform....               \n")

while x==0:
    print("------------------------------------------Type Here----------------------------------------------\n")
    start=time.time()
    sentence=input()
    end=time.time()
    print("-------------------------------------------------------------------------------------------------\n")
    timetaken=int(end-start)
    words=len(list(sentence))
    wpm=words/timetaken
    print("\nyour typing speed is",wpm)
    if(wpm>=4):
        print("     *******Congrauts you are really a excellent typist have a great future******\n")
        print("              -----------you are on level 1-------------  ")
    elif(wpm>=3 and wpm<4):
        print("\n     *******you have a wonderfull typing speed still can be improved******* \n")
        print("              -----------you are on level 2-------------  ")

    elif(wpm>2 and wpm<3):
        print("\n        *******you have an average speed you need to improve a lot********   \n")
        print("              -----------you are on level 3-------------  ")
    else:
        print("      ********your typing speed is poor you have to improve more******* \n")
        print("              -----------you are on level 4-------------  ")
    print("\ndo you want to test your speed again")
    inp=input()
    if(inp=="yes"):
        x=0
    else:
        x=1
print("\n<---------------------------thank you for visiting-------------------------->")
        
    
    
    
