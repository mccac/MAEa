#name of players (input)
player1=raw_input("Player 1 Name: ")
player2=raw_input("Player 2 Name: ")
print "***********************"

print "instructions:"
print " 1- If you want to pull up only one num.you should Enter 0 for second num"
print " 2- you must pull up at least one num\n\n"

import random
s=random.randint(10,20) #last num
arr1=[]
arr2=[] #will content the values which entered by user
for i in range (1,s):
    arr1.append(i)
st=",".join(str(e)for e in arr1)
print "===============>>>",st
z=s-1 #the digits of numbers for arr1
d=True
f=True

while z!=0:
    
        
#player1
    while f==True:
        print (player1)
        x=int(input("num 1: "))
        w=int(input("num 2: "))
        if w!=0:#that means user entered 2 nums
            if x!=0:                
                if x  not in arr2 and  w not in arr2:#checking if x and w exist in array or not?
                    if 0<(x and w)<s:
                        if w==x+1 or x==w+1:
                            arr2.append(x)
                            arr2.append(w)
                            arr1[x-1]=("-")#swap
                            arr1[w-1]=("-")#swap
                            z-=2
                            f=False
                            d=True
                            if z==0:
                                print player1,"WIN"
                                d=False
                                break
                            else:
                                st=",".join(str(e)for e in arr1) 
                                print "===============>>>",st #the new        
                        else:
                            print "shoud be sequence"
                    else:
                        print "out of range"
                else:
                    print"not allwoed"
            else:
                print "out of range"
        #if the user want pull up one num
        else:
            if x!=0:
                if x not in arr2:
                    if 0<x<s:
                        arr2.append(x)
                        arr1[x-1]=("-")
                        f=False
                        d=True
                        z-=1
                        if z==0:
                            print player1,"WIN"
                            d=False
                            break
                        else:
                            st=",".join(str(e)for e in arr1)
                            print"===============>>>",st
                    else:
                        print"out of range"
                else:
                    print"not allowed"
            else:
                print "out of range"

                        
#player2
    while d==True:
        print (player2)
        y=int(input("num 1: "))
        k=int(input("num 2: "))
        if k!=0 :
            if y!=0:
                if y not in arr2 and k not in arr2:#checking if y and k exist in an array or not?
                    if 0<(y and k)<s:
                        if k==y+1 or y==k+1:
                            arr2.append(y)
                            arr2.append(k)
                            arr1[y-1]=("-")#swap
                            arr1[k-1]=("-")#swap
                            z-=2
                            d=False
                            f=True
                            if z==0:
                                print player2,"WIN"
                                f=False
                                break
                            else:
                                st=",".join(str(e)for e in arr1)
                                print "===============>>>",st #the new                
                        else:
                            print "shoud be sequence"  
                    else:
                        print "out of range"
                else:
                    print"not allowed"
            else:
                print "out of range"
        else:
            if y!=0:             
                if y not in arr2:
                    if 0<y <s:
                        arr2.append(y)
                        arr1[y-1]=("-")
                        d=False
                        f=True
                        z-=1
                        if z==0:
                            print player2,"WIN"
                        else:
                            st=",".join(str(e)for e in arr1)
                            print "===============>>>",st 
                    else:
                        print"out of range"
                else:
                    print"not allowed"
            else :
                print "out of range"
        if f==False and d==False:
            break                                
