news = ["N01","N02","N03","N04","N05","N06","N07","N08","N09","N10",
        "N11","N12","N13","N14","N15","N16","N17","N18","N19","N20",
        "N21","N22","N23","N24","N25","N26","N27","N28","N29","N30"]

emotion = [63,70,66,77,55,64,59,95,55,79,
           70,75,70,90,85,68,72,95,18,99,
           74,85,43,90,25,81,62,45,65,45]

provoke = [77,68,60,82,40,80,60,50,100,11,
           58,68,64,57,77,98,91,50,95,27,
           97,36,63,82,71,79,55,57,40,57]

def checkEmotion(x):
    eLow, eMedium, eHigh = 0,0,0

    if x >= 0 and x <= 35:
        eLow    = 1

    elif x > 35 and x < 39:
        eLow    = (-1*((x-39)/(39-35)))
        eMedium = ((x-35)/(39-35))

    elif x >= 39 and x <= 61:
        eMedium = 1

    elif x > 61 and x <65:
        eMedium = (-1*((x-65)/(65-61)))
        eHigh   = ((x-61)/(65-1))

    elif x >= 65:
        eHigh   = 1

    return eLow, eMedium, eHigh


def checkProvoke(x):
    pLow, pMedium, pHigh = 0,0,0

    if x >= 0 and x <= 55:
        pLow    = 1

    elif x > 55 and x < 60:
        pLow    = (-1*(x-60)/(60-55))
        pMedium = ((x-55)/(60-55))

    elif x >= 60 and x <= 85:
        pMedium = 1

    elif x > 85 and x < 87:
        pMedium = (-1*(x-87)/(82-87))
        pHigh   = ((x-85)/(87-85))

    elif x >= 87:
        pHigh   = 1

    return pLow, pMedium, pHigh

def inference(eLow, eMedium, eHigh, pLow, pMedium, pHigh):
    Y1,Y2,Y3,Y4,Y5 = 0,0,0,0,0
    N1,N2,N3,N4 = 0,0,0,0
    Y,N = 0,0

    if eHigh != 0 and pHigh != 0:
        Y1 = min(eHigh,pHigh)

    if eHigh != 0 and pMedium != 0:
        Y2 = min(eHigh,pMedium)

    if eHigh != 0 and pLow != 0:
        N1 = min(eHigh,pLow)

    if eMedium != 0 and pHigh !=0:
        Y3 = min(eMedium,pHigh)

    if eMedium != 0 and pMedium != 0:
        N2 = min(eMedium,pMedium)

    if eMedium != 0 and pLow != 0:
        N3 = min(eMedium,pLow)

    if eLow != 0 and pHigh != 0:
        Y4 = min(eLow,pHigh)

    if eLow != 0 and pMedium != 0:
        Y5 = min(eLow,pMedium)

    if eLow != 0 and pLow != 0:
        N4 = min(eLow,pLow)

    Y = max(Y1,Y2,Y3,Y4,Y5)
    N = max(N1,N2,N3,N4)
    return Y,N


def defuzzification(Y,N):
    if Y != 0 and N != 0:
        return ((Y*60)+(N*40))/(Y+N)
    elif Y != 0:
        return (Y*60)/Y
    elif N != 0:
        return (N*40)/N


count = 0
while count < 30:
    eLow,eMedium,eHigh = checkEmotion(emotion[count])
    pLow,pMedium,pHigh = checkProvoke(provoke[count])
    Ya,Tidak = inference(eLow,eMedium,eHigh,pLow,pMedium,pHigh)
    hasil = defuzzification(Ya,Tidak)
    if hasil < 55.0:
        hoax = "No"
    elif hasil >= 55.0:
        hoax = "Yes"
    print("News : ",news[count]," Emotion : ",emotion[count]," Provoke : ",provoke[count]," Hoax : ", hoax)

    count += 1
