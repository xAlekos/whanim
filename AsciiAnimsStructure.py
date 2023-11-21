import os

def createanimslist():
    animations = []
    return animations


def loadanimation(filename, animlist):
    f = open("./Anims/%s" % filename, "r")
    info = f.readline().rstrip('\n').split(' ') #legge informazioni su numero di frame e di lines che compongono il frame
    lines = int(info[0])
    frames = int(info[1])
    animation = []

    for j in range(0,frames):
        animation.append([])
        for i in range(0,lines):
            animation[j].append(f.readline().rstrip('\n'))
    animlist.append(animation)
    f.close()

def giveanimfromid(id, animlist):
    if id <= len(animlist):
        return animlist[id]
    else:
        return 0

def printanim(id,animlist):
    if id <= len(animlist):
        anim= animlist[id]
        for i in range(0, len(anim)):
            print("Frame u %i: " % (i + 1) )
            for lines in anim[i]:
                print(lines)
    else:
        return 0


def loadfromfolder(animlist= None, path = "./Anims"):
   anims_detected = os.listdir(path)
   for anim in anims_detected:
       loadanimation(anim,animlist)
