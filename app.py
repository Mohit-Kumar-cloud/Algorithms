from tkinter import *
import sys
sys.path.append('/Data/')
sys.path.append('/src/')
import Data.random_file
import src.Lcs
import src.edit_distance
import src.knapsack
import src.Lis
import src.mcm
import src.Partition
import src.rodcut
import src.Scs
import src.Word_break
import src.Coin_change

front='red'
back='grey'
design='black'

optionlist=['file1','file2','file3','file4','file5','file6','file7','file8','file9','file10']
window1=""
window2=""
window3=""
window4=""
window5=""  
window6=""
window7=""
window8=""
window9=""
window10=""
entry1=""
entry2=""
entry3=""
def get_lcs():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file("lcs",s) 
    a=var[0]
    b=var[1] 
    entry1.insert(END,a)
    entry2.insert(END,b)      

def lcs_result():
    a=entry1.get()
    b=entry2.get()
    r1 ="Length of Lcs is:" + str(src.Lcs.lcs_len(a,b))
    r2= "Lcs is :"+"".join (src.Lcs.lcs(a,b))
    w=Text(window1,height=10,width=40)
    w.grid(row=6,column=0,sticky='s')
    w.insert(END,r1)
    w.insert(END,"\n")
    w.insert(END,r2)

def Lcs():
    global window1
    window1 = Toplevel(root)
    window1['bg']=design
    window1.geometry("500x500")
    window1.title("Longest Common Subsequence")
    lbl = Label(window1,text="Longest Common Subsequence",fg=front,bg=design)
    lbl2 = Label(window1,text="X:",fg=front,bg=design) 
    lbl3 = Label(window1,text="Y:",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10)

    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    entry1 = Entry(window1)
    global entry2 
    entry2= Entry(window1)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    o=OptionMenu(window1,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window1,text="Generate Random Files",command=lambda:Data.random_file.generate_file("lcs"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window1,text="Select File",command=get_lcs)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window1,text="Submit",command=lcs_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window1,text="Close Me",command=lambda:window1.destroy())
    btn2.grid(row=4,column=1)
    
    


def get_scs():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file("scs",s) 
    a=var[0]
    b=var[1] 
    entry1.insert(END,a)
    entry2.insert(END,b)      

def scs_result():
    a=entry1.get()
    b=entry2.get()
    r1 ="Length of Scs is:" + str(src.Scs.Scs_len(a,b))
    r2= "scs is :"+"".join (src.Scs.scs(a,b))
    w=Text(window2,height=10,width=40)
    w.grid(row=6,column=0,sticky='s')
    w.insert(END,r1)
    w.insert(END,"\n")
    w.insert(END,r2)

def Scs():
    global window2
    window2 = Toplevel(root)
    window2['bg']=design
    window2.geometry("500x500")
    window2.title("Shortest Common Supersequence")
    lbl = Label(window2,text="Shortest Common Supersequence",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window2,text="X:",fg=front,bg=design) 
    lbl3 = Label(window2,text="Y:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10)
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    entry1 = Entry(window2)
    global entry2 
    entry2= Entry(window2)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    o=OptionMenu(window2,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window2,text="Generate Random Files",command=lambda:Data.random_file.generate_file("scs"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window2,text="Select File",command=get_scs)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window2,text="Submit",command=scs_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window2,text="Close Me",command=lambda:window2.destroy())
    btn2.grid(row=4,column=1)




def get_edit_distance():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file("edit_distance",s) 
    a=var[0]
    b=var[1] 
    entry1.insert(END,a)
    entry2.insert(END,b)      

def edit_distance_result():
    a=entry1.get()
    b=entry2.get()
    r1 ="Length of Edit Distance is:" + str(src.edit_distance.edit_distance(a,b))
    w=Text(window3,height=10,width=40)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def Edit_distance():
    global window3
    window3 = Toplevel(root)
    window3['bg']=design
    window3.geometry("500x500")
    window3.title("Levenshtein Distance(Edit Distance)")
    lbl = Label(window3,text="Levenshtein Distance(Edit Distance)",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window3,text="X:",fg=front,bg=design) 
    lbl3 = Label(window3,text="Y:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10)
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    entry1 = Entry(window3)
    global entry2 
    entry2= Entry(window3)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    o=OptionMenu(window3,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window3,text="Generate Random Files",command=lambda:Data.random_file.generate_file("edit_distance"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window3,text="Select File",command=get_edit_distance)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window3,text="Submit",command=edit_distance_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window3,text="Close Me",command=lambda:window3.destroy())
    btn2.grid(row=4,column=1)



def get_lis():
    entry1.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_1("lis",s)
    b=""
    for line in var:
        b+=str(line)
        b+=","
    a=b[:len(b)-1]

    entry1.insert(END,a)      

def lis_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    r1 ="Length of Longest increasing supersequence is:" + str(src.Lis.lis(c))
    w=Text(window4,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def Lis():
    global window4
    window4 = Toplevel(root)
    window4['bg']=design
    window4.geometry("500x500")
    window4.title("Longest Increasing Supersequence")
    lbl = Label(window4,text="Longest Increasing Supersequence",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window4,text="Arr:",fg=front,bg=design)
    lbl2['font']=("Arial",10) 
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    global entry1
    entry1 = Entry(window4)
    entry1.grid(row=1,column=1,sticky='w')
    o=OptionMenu(window4,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window4,text="Generate Random Files",command=lambda:Data.random_file.generate_file_1("lis"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window4,text="Select File",command=get_lis)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window4,text="Submit",command=lis_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window4,text="Close Me",command=lambda:window4.destroy())
    btn2.grid(row=4,column=1)

def get_mcm():
    entry1.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_1("mcm",s)
    b=""
    for line in var:
        b+=str(line)
        b+=","
    a=b[:len(b)-1]

    entry1.insert(END,a)      

def mcm_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    m=src.mcm.matrixChainOrder(c)    
    j=len(c)-1
    r1 ="Optimal Parenthesization is:" + str(src.mcm.matrixChainOrderPar(m,j-1))
    r2 = "Minimum Cost is :"+ str(src.mcm.matrixChainOrderCost(c))
    w=Text(window5,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)
    w.insert(END,'\n')
    w.insert(END,r2)

def Mcm():
    global window5
    window5 = Toplevel(root)
    window5['bg']=design
    window5.geometry("500x500")
    window5.title("Matrix Chain Multipllication")
    lbl = Label(window5,text="Matrix Chain Multiplication",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window5,text="Arr:",fg=front,bg=design)
    lbl2['font']=("Arial",10) 
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    global entry1
    entry1 = Entry(window5)
    entry1.grid(row=1,column=1,sticky='w')
    o=OptionMenu(window5,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window5,text="Generate Random Files",command=lambda:Data.random_file.generate_file_1("mcm"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window5,text="Select File",command=get_mcm)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window5,text="Submit",command=mcm_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window5,text="Close Me",command=lambda:window5.destroy())
    btn2.grid(row=4,column=1)





def get_knapsack():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_2("knapsack",s)
    a=var[0]
    b=""
    c=""
    count=0
    for line in var[1:len(var)]:
        for l in line:
            count+=1
            if count%2==1:
               b+=str(l)
               b+=","
            else:
               c+=str(l) 
               c+=","
    b=b[:len(b)-1]
    c=c[:len(c)-1]
    entry1.insert(END,c)
    entry2.insert(END,b)
    entry3.insert(END,a)      

def knapsack_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    d=entry2.get()
    e=d.split(',')
    f=[]
    for line in e:
         f.append(int(line))
    l=min(len(f),len(c))
    c=c[:l]
    f=f[:l]
    g=entry3.get()
    g=int(g)  
    r1 ="Knapsack:" + str(src.knapsack.knapSack(g,f,c))
    w=Text(window6,height=10,width=50)
    w.grid(row=6,column=0)
    w.insert(END,r1)

def Knapsack():
    global window6
    window6 = Toplevel(root)
    window6['bg']=design
    window6.geometry("500x500")
    window6.title("0/1 Knapsack")
    lbl = Label(window6,text="0/1 Knapsack",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window6,text="Values:",fg=front,bg=design)
    lbl3 = Label(window6,text="Weights:",fg=front,bg=design) 
    lbl4 = Label(window6,text="Weight Limit:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10)
    lbl4['font']=("Arial",10)
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    lbl4.grid(row=3,column=0)
    global entry1
    global entry2
    global entry3
    entry1 = Entry(window6)
    entry2 = Entry(window6)
    entry3 = Entry(window6)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    entry3.grid(row=3,column=1,sticky='w')
    
    
    o=OptionMenu(window6,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=4,column=0)
    btn11=Button(window6,text="Generate Random Files",command=lambda:Data.random_file.generate_file_2("knapsack"))
    btn11.grid(row=5,column=0,)
    btn12=Button(window6,text="Select File",command=get_knapsack)
    btn12.grid(row=5,column=1,sticky='w')
    btn10=Button(window6,text="Submit",command=knapsack_result)
    btn10.grid(row=2,column=2)
    btn2=Button(window6,text="Close Me",command=lambda:window6.destroy())
    btn2.grid(row=6,column=1)



def get_partition():
    entry1.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_1("partition",s)
    b=""
    for line in var:
        b+=str(line)
        b+=","
    a=b[:len(b)-1]

    entry1.insert(END,a)      

def partition_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    r1 ="Can be Partitioned ? :" + str(src.Partition.findPartition(c))
    w=Text(window7,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def Partition():
    global window7
    window7 = Toplevel(root)
    window7['bg']=design
    window7.geometry("500x500")
    window7.title("Partition Problem")
    lbl = Label(window7,text="Partition Problem",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window7,text="Arr:",fg=front,bg=design)
    lbl2['font']=("Arial",10) 
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    global entry1
    entry1 = Entry(window7)
    entry1.grid(row=1,column=1,sticky='w')
    o=OptionMenu(window7,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window7,text="Generate Random Files",command=lambda:Data.random_file.generate_file_1("partition"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window7,text="Select File",command=get_partition)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window7,text="Submit",command=partition_result)
    btn10.grid(row=2,column=1)
    btn2=Button(window7,text="Close Me",command=lambda:window7.destroy())
    btn2.grid(row=4,column=1)




def get_rodcut():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_2("rodcut",s)
    a=var[0]
    b=""
    c=""
    count=0
    for line in var[1:len(var)]:
        for l in line:
            count+=1
            if count%2==1:
               b+=str(l)
               b+=","
            else:
               c+=str(l) 
               c+=","
    b=b[:len(b)-1]
    c=c[:len(c)-1]
    entry1.insert(END,c)
    entry2.insert(END,a)     

def rodcut_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    d=entry2.get()
    d=int(d)
    c=c[:len(c)-1] 
    e=[i for i in range(1,len(c)+1)] 
    r1 ="Maximum Obtainable Value:" + str(src.rodcut.cutRod(c,d,e))
    w=Text(window8,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def Rodcut():
    global window8
    window8 = Toplevel(root)
    window8['bg']=design
    window8.geometry("500x500")
    window8.title("Rod Cut Problem")
    lbl = Label(window8,text="Rod Cut Problem",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window8,text="Price:",fg=front,bg=design)
    lbl3 = Label(window8,text="Size:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10) 
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    global entry2
    entry1 = Entry(window8)
    entry2 = Entry(window8)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    
    o=OptionMenu(window8,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=4,column=0)
    btn11=Button(window8,text="Generate Random Files",command=lambda:Data.random_file.generate_file_2("rodcut"))
    btn11.grid(row=5,column=0,)
    btn12=Button(window8,text="Select File",command=get_rodcut)
    btn12.grid(row=5,column=1,sticky='w')
    btn10=Button(window8,text="Submit",command=rodcut_result)
    btn10.grid(row=2,column=2)
    btn2=Button(window8,text="Close Me",command=lambda:window8.destroy())
    btn2.grid(row=5,column=1)






def get_coin_change():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_1("coin_change",s)
    b=""
    for line in var:
        b+=str(line)
        b+=","
    a=b[:len(b)-1]

    entry1.insert(END,a)
    entry2.insert(END,'160')      

def coin_change_result():
    a=entry1.get()
    d=entry2.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(int(line))
    d=int(d)
    r1 ="Count of Coins is:" + str(src.Coin_change.count(c,d))
    w=Text(window9,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def coin_change():
    global window9
    window9 = Toplevel(root)
    window9['bg']=design
    window9.geometry("500x500")
    window9.title("Coin Change Problem")
    lbl = Label(window9,text="Coin Change Problem",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window9,text="Arr:",fg=front,bg=design) 
    lbl3 = Label(window9,text="Change:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10)
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    global entry2
    entry1 = Entry(window9)
    entry2 = Entry(window9)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    o=OptionMenu(window9,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=3,column=0)
    btn11=Button(window9,text="Generate Random Files",command=lambda:Data.random_file.generate_file_1("coin_change"))
    btn11.grid(row=4,column=0,)
    btn12=Button(window9,text="Select File",command=get_coin_change)
    btn12.grid(row=4,column=1,sticky='w')
    btn10=Button(window9,text="Submit",command=coin_change_result)
    btn10.grid(row=2,column=2)
    btn2=Button(window9,text="Close Me",command=lambda:window9.destroy())
    btn2.grid(row=4,column=1)



def get_word_break():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    s=option.get()
    s=s[4:]
    s=int(s)
    s-=1
    var = Data.random_file.get_file_3("word_break",s)
    b=""
    c="mohitkumar"
    for line in var:
        b+=str(line)
        b+="," 
    b=b[:len(b)-1]
    entry1.insert(END,b)
    entry2.insert(END,c)     

def word_break_result():
    a=entry1.get()
    b=a.split(',')
    c=[]
    for line in b:
        c.append(line)
    d=entry2.get()
    c=c[:len(c)-1] 
    r1 ="Can Be segmented ? :" + str(src.Word_break.wordBreak(c,d))
    w=Text(window10,height=10,width=50)
    w.grid(row=6,column=0,sticky="s")
    w.insert(END,r1)

def Word_break():
    global window10
    window10 = Toplevel(root)
    window10['bg']=design
    window10.geometry("500x500")
    window10.title("Word Break Problem")
    lbl = Label(window10,text="Word Break Problem",fg=front,bg=design)
    lbl['font']=("Arial",20)
    lbl2 = Label(window10,text="Dictionary:",fg=front,bg=design)
    lbl3 = Label(window10,text="String:",fg=front,bg=design)
    lbl2['font']=("Arial",10)
    lbl3['font']=("Arial",10) 
    lbl.grid(row=0,column=1,sticky='w')
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    global entry1
    global entry2
    entry1 = Entry(window10)
    entry2 = Entry(window10)
    entry1.grid(row=1,column=1,sticky='w')
    entry2.grid(row=2,column=1,sticky='w')
    
    o=OptionMenu(window10,option,*optionlist)
    o["menu"].config(bd=0)
    o["highlightthickness"]=0
    o.grid(row=4,column=0)
    btn11=Button(window10,text="Generate Random Files",command=lambda:Data.random_file.generate_file_3("word_break"))
    btn11.grid(row=5,column=0,)
    btn12=Button(window10,text="Select File",command=get_word_break)
    btn12.grid(row=5,column=1,sticky='w')
    btn10=Button(window10,text="Submit",command=word_break_result)
    btn10.grid(row=2,column=2)
    btn2=Button(window10,text="Close Me",command=lambda:window10.destroy())
    btn2.grid(row=5,column=1)









root = Tk()
option=StringVar()
option.set(optionlist[0])
lbl1= Label(root,text="Dynamic Algorithms",width=1000,fg='red')
lbl1['font']=("Arial",20)
lbl1.pack()
btn=Button(root,text="Longest Common Subsequence",command=Lcs,fg='red',bg='grey')
btn.pack(fill=X)

btn1=Button(root,text="Shortest Common Supersequence",command=Scs,fg='red',bg='grey')
btn1.pack(fill=X)

btn2=Button(root,text="Levenshtein Distance / Edit Distance",command=Edit_distance,fg='red',bg='grey')
btn2.pack(fill=X)

btn3=Button(root,text="Longest Increasing Subsequence",command=Lis,fg='red',bg='grey')
btn3.pack(fill=X)

btn4=Button(root,text="Matrix Chain Multiplication",command=Mcm,fg='red',bg='grey')
btn4.pack(fill=X)

btn5=Button(root,text="0-1-Knapsack",command=Knapsack,fg='red',bg='grey')
btn5.pack(fill=X)

btn6=Button(root,text="Partition Problem",command=Partition,fg='red',bg='grey')
btn6.pack(fill=X)

btn7=Button(root,text="Rod Cutting Problem",command=Rodcut,fg='red',bg='grey')
btn7.pack(fill=X)

btn8=Button(root,text="Coin Change Problem",command=coin_change,fg='red',bg='grey')
btn8.pack(fill=X)

btn9=Button(root,text="Word Break Problem",command=Word_break,fg='red',bg='grey')
btn9.pack(fill=X)


Button(root,text="Exit",width=25,fg='red',bg='grey',command=lambda:root.destroy()).pack()

root.geometry("700x700")
root.title("Algorithm Project")
root['bg']='black'
root.mainloop()