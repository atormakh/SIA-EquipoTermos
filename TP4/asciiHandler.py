def asciiStringToLettersMatrix():
    alphabet="""
 ###  ####   ###  ####  ##### #####  ###  #   # ##### ##### #   # #     #   #
#   # #   # #   # #   # #     #     #     #   #   #     #   #  #  #     ## ##
##### ####  #     #   # ####  ####  #  ## #####   #     #   ###   #     # # #
#   # #   # #   # #   # #     #     #   # #   #   #   # #   #  #  #     #   #
#   # ####   ###  ####  ##### #      ###  #   # ##### ###   #   # ##### #   #

#   #  ###  ####   ###  ####   ###  ##### #   # #   # #   # #   # #   # #####
##  # #   # #   # #   # #   # #       #   #   # #   # #   #  # #   # #     # 
# # # #   # ####  #   # ####   ###    #   #   #  # #  # # #   #     #     #  
#  ## #   # #     #  #  #   #     #   #   #   #  # #  ## ##  # #    #    #   
#   #  ###  #      ## # #   #  ###    #    ###    #   #   # #   #   #   #####"""

    alphabetASCII=[]
    index=1
    l=0
    for h in range(0,5): 
        l=0
        for j in range(0,13):
            if(h ==0):
                alphabetASCII.append([])
            for i in range(0,5):
                alphabetASCII[l].append(alphabet[index])
                index+=1
            index+=1
            l+=1
    index+=1
    for h in range(0,5): 
        l=13
        for j in range(0,13):
            if(h ==0):
                alphabetASCII.append([])
            for i in range(0,5):
                alphabetASCII[l].append(alphabet[index])
                index+=1
            index+=1
            l+=1 
    alphabetASCIIBipolar=[]
    for letter in alphabetASCII:
        bipolarLetter = [1 if e=='#' else -1 for e in letter]
        alphabetASCIIBipolar.append(bipolarLetter)
    return (alphabetASCII,alphabetASCIIBipolar)