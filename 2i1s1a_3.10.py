import os
import sys

print("Pain interpeter (also 2i1s1a)")
filename = input("Enter a filename or nothing to skip:")
if not not filename: 
    #not not returns the bool faster. if filename is "", notnot returns false, which won't activate.
    with open(filename, "r") as f:
        tointer = f.read()
a = 0
b = 0
c = ""
d = []
rep = []
iflst = []
l = []
evalif = False

def interpert(i, j,h):

    global a 
    global b
    global c
    global d
    global rep
    global l
    global iflst
    global evalif
    out = sys.stdout

    if i == "+":
        if j =="a":
            a += 1
        elif j=="b":
            b+=1
        else:
            a+=1
    if i == "g":
        checkset = {"a","b","c","d"}
        match j:
            case "c":
                c = input(">>")
            case "a":
                a = ord(input(">>"))
            case "b":
                b = ord(input(">>"))
            case "d":
                d.append(input(">>"))
            case s:
                c = input(">>")
            
        

    if i == "p":
        if j == "a" or j == "b" or j == "c" or j == "d":
            match j:
                case "a":
                    out.write(str(a))
                    out.write("\n")
                case "b":
                    out.write(str(b))
                    out.write("\n")
                case "c":
                    out.write(c)
                    out.write("\n")
                case "d":
                    out.write(d)
                    out.write("\n")
    if i == "-":
        if j =="a":
            a-=1
        elif j =="b":
            b-=1
        else:
            a-=1
    if i == "d":
        b-=1
    while i=="[" and j != "]":
        rep.append(i)
        for index, i in enumerate(l):
            if (index+1 < len(l) and index - 1 >= 0):
             current_i = str(i)
             current_j = str(l[index+1])
             interpert(current_i,current_j)
    if i=="?":
        ifbool = not not a
        evalif = True
    while evalif:
        if i == ":" and j !=":":
            iflst.append(i)
        else:
            if ifbool:
                out.write(ifbool)
                for index, i in enumerate(l):
                    if (index+1 < len(l) and index - 1 >= 0):
                         current_i = str(i)
                         current_j = str(l[index+1])
                         interpert(current_i,current_j)
                         print("done step")
            else:
                break
    if i == "r" and h != "@":
        d.reverse()
    if i == "`":
        out.write(d[len(d)-1])
    if i == "#":
        d.insert(0,int(j))
    if i == "@":
        d.insert(0,j)
    if i ==";":
        for i in d:
            c += str(i)
    if i == "$":
        d = []
    if i == "S":
        if j =="a":
            a*=a
        elif j=="b":
            b*=b
        else:
            out.write("Error: S received argument other than a or b.")
    if i == "A":
        out.write(chr(a))
    if i == "M":
        if h == "a" and j=="b":
            a = a*b
        elif h == "b" and j=="a":
            b = b*a
        else:
            out.write("Missing arguemnt for M.")
    if i == "D":
        if h == "a" and j =="b":
            a=int(a/b)
        if h == "b" and j =="a":
            b=int(b/a)

#makes sure next will not break cuz LiSt InDeX OuT Of RaNGe
l.append("null")
def parse():
    if l[len(l)-1] != "e":
        print("Pain code error: code did not end with terminator \"e\"")
    for index, i in enumerate(l):
        if (index+1 < len(l) and index - 1 >= 0):
            curr_h = str(l[index-1])
            current_i = str(i)
            current_j = str(l[index+1])
            interpert(current_i,current_j,curr_h)
while True:
    a = 0
    b = 0
    c = ""
    d = []
    rep = []
    iflst = []
    print("\n")
    inter = input("Enter code:")
    l = list(inter)
    l.insert(0,"!")
    parse()  
    
    