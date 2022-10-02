export = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
interlock = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
# digital, analog1, analog2, analog3, analog4, analog4, analog5, analog6, analog7, analoag8
r=1
A=0
B=0
C=0
output0=0
output1=0
output2=0
output3=0
output4=0
output5=0
output6=0
output7=0
output8=0
trip=0
#r is row counter


f=open("lb.01.csv","r")

(f.readline())
(f.readline())
(f.readline())
(f.readline())
(f.readline())
(f.readline())
for line in f:
    #print (line)
    list1 = (line.split('","'))
    list1[2]=list1[2].replace('"',"")
    list1[4]=list1[4].replace('"',"")
    list1[6]=list1[6].replace('"',"")
    #print (list1[2])
    #print (list1[4])
    #print (list1[6])
    if list1[4]=="1F3":
        #print ("found 1F3")
        digitalA = list1[6].split(" ")
        outputdig = output0
        output0 = int(digitalA[0])
        export[0].append(output0)
        export[1].append(export[1][r-1])
        export[2].append(export[2][r-1])
        export[3].append(export[3][r-1])
        export[4].append(export[4][r-1])
        export[5].append(export[5][r-1])
        export[6].append(export[6][r-1])
        export[7].append(export[7][r-1])
        export[8].append(export[8][r-1])
        A=A+1
        if outputdig!=output0:
            interlock[0].append(output0)
            interlock[1].append(output1)
            interlock[2].append(output2)
            interlock[3].append(output3)
            interlock[4].append(output4)
            interlock[5].append(output5)
            interlock[6].append(output6)
            interlock[7].append(output7)
            interlock[8].append(output8)
            interlock[9].append(r)
            trip=trip+1
            
                                                   
        
    if list1[4]=="2F3":
        #print ("found 2F3")
        analogA = list1[6].split(" ")
        output1 = int(analogA[1]+analogA[0],16)
        output2 = int(analogA[3]+analogA[2],16)
        output3 = int(analogA[5]+analogA[4],16)
        output4 = int(analogA[7]+analogA[6],16)
        export[0].append(export[0][r-1])
        export[1].append(output1)
        export[2].append(output2)
        export[3].append(output3)
        export[4].append(output4)
        export[5].append(export[5][r-1])
        export[6].append(export[6][r-1])
        export[7].append(export[7][r-1])
        export[8].append(export[8][r-1])
        B=B+1
        
    if list1[4]=="3F3":
        #print ("found 3F3")
        analogB = list1[6].split(" ")
        output5 = int(analogB[1]+analogB[0],16)
        output6 = int(analogB[3]+analogB[2],16)
        output7 = int(analogB[5]+analogB[4],16)
        output8 = int(analogB[7]+analogB[6],16)
        export[0].append(export[0][r-1])
        export[1].append(export[1][r-1])
        export[2].append(export[2][r-1])
        export[3].append(export[3][r-1])
        export[4].append(export[4][r-1])
        export[5].append(output5)
        export[6].append(output6)
        export[7].append(output7)
        export[8].append(output8)
        C=C+1
            
    r=r+1
#print (export)

f.close()
print(A, B, C)
f=open("Can_output.csv", "w+")
for row in range(r):
    lineout = str(export[0][row])+","+str(export[1][row])+","+str(export[2][row])+","+str(export[3][row])+","+str(export[4][row])+","+str(export[5][row])+","+str(export[6][row])+","+str(export[7][row])+","+str(export[8][row])+"\n"
    f.write(lineout)

f.close()
f=open("interlock.csv", "w+")
for row in range(trip):
    lineout = str(interlock[0][row])+","+str(interlock[1][row])+","+str(interlock[2][row])+","+str(interlock[3][row])+","+str(interlock[4][row])+","+str(interlock[5][row])+","+str(interlock[6][row])+","+str(interlock[7][row])+","+str(interlock[8][row])+","+str(interlock[9][row])+"\n"
    f.write(lineout)

f.close()
    
#print (export)
print (str(len(export[0]))+" " +str(len(export[1]))+" " +str(len(export[2]))+" " +str(len(export[3]))+" " +str(len(export[4]))+" " +str(len(export[5]))+" " +str(len(export[6]))+" " +str(len(export[7]))+" " +str(len(export[8])))
print ("number of export rows: " +str(r))
#for line in f:
#   print(line)
    
