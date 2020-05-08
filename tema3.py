f=open("automat","r")
w=f.readline()
stin=int(f.readline())
nrstfin=int(f.readline())
stfin=[]
for x in f.readline().split():
    if(x.isdigit()):
        stfin.append(int(x))
nrtran=f.readline()
tran=[]
for i in range(100):
    tran.append([])
for i in range(int(nrtran)):
    aux=f.readline().split(" ",1)
    aux[1]=aux[1][0:len(aux[1])-1]
    tran[int(aux[0])].append(aux[1].split())
st=['Z']
q=[(st,stin)]
ql=list()
ql.append(0)
start=0
last=len(q)
curent=0
possol=list()
nr=w.count("$")
w=w.replace("$","")
while(start!=last):
    o=q[start]
    nst=o[0]
    litera=w[ql[start]]
    if litera=='\n':
        possol.append([int(o[1]),nst])
    for x in tran[int(o[1])]:
        if(x[1]==litera and nst[0]==x[2]):
            nst.pop(0)
            rg=0
            for ch in x[3]:
                if ch!='$':
                    nst.insert(rg,ch)
                    rg+=1
            ql.append(ql[start]+1)
            q.append((nst,x[0]))
            last+=1
    start+=1
ok=False
for x in possol:
    if ok==True:
        break
    for y in tran[x[0]]:
        if(x[1][0]=='Z' and y[2]=='Z' and y[3]=='$'):
            if(int (y[0]) in stfin):
                ok=True
                print("Cuvant acceptat")
                break
if(ok==False):
    print("Cuvant neacceptat")




