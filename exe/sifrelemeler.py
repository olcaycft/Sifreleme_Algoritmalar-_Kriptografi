from tkinter import *
from tkinter.ttk import Combobox
import math
from random import randrange
import numpy as np




alfabe_eng1 = {0:'A', 1: 'B', 2:'C', 3: 'D', 4:'E', 5:'F', 6:'G', 
              7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 
              14:'O', 15:'P',16:'Q',17: 'R', 18:'S', 19:'T',20: 'U', 
              21:'V', 22:'W', 23:'X',24: 'Y', 25:'Z'}
alfabe_turkce = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'Ç':3,'ç':3, 'D':4,
'd':4, 'E':5, 'e':5, 'F':6, 'f':6, 'G':7, 'g':7,'ğ':8,'Ğ':8, 'H':9, 'h':9, 'I':10,
'ı':10,'İ':11,'i':11, 'J':12, 'j':12, 'K':13, 'k':13, 'L':14, 'l':14, 'M':15, 'm':15,
'N': 16, 'n':16, 'O':17, 'o':17,'Ö':18,'ö':18, 'P':19, 'p':19, 'R':20, 'r':20,
'S':21, 's':21,'Ş':22,'ş':22, 'T':23,'t':23, 'U':24, 'u':24,'Ü':25,'ü':25, 'V':26,
'v':26, 'Y':27, 'y':27, 'Z':28, 'z':28
}

alfabe_eng = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
def alfabe(letter):
    alfabe_turkce = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'Ç':3,'ç':3, 'D':4,
'd':4, 'E':5, 'e':5, 'F':6, 'f':6, 'G':7, 'g':7,'ğ':8,'Ğ':8, 'H':9, 'h':9, 'I':10,
'ı':10,'İ':11,'i':11, 'J':12, 'j':12, 'K':13, 'k':13, 'L':14, 'l':14, 'M':15, 'm':15,
'N': 16, 'n':16, 'O':17, 'o':17,'Ö':18,'ö':18, 'P':19, 'p':19, 'R':20, 'r':20,
'S':21, 's':21,'Ş':22,'ş':22, 'T':23,'t':23, 'U':24, 'u':24,'Ü':25,'ü':25, 'V':26,
'v':26, 'Y':27, 'y':27, 'Z':28, 'z':28
}
    alfabe_eng = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
    alfabe_num = alfabe_eng[letter]
    return alfabe_num










def modified (event) :
    if(algoritma.get()=="Sezar Şifreleme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifrele"
    elif(algoritma.get()=="Çit Şifreleme"):
        key_icerik['state']='readonly'
        add_btn["text"]="Şifrele"
    elif(algoritma.get()=="Kolon Şifreleme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifrele"
    elif(algoritma.get()=="Polybius Şifreleme"):
        key_icerik['state']='readonly'
        add_btn["text"]="Şifrele"
    elif(algoritma.get()=="Vigenere Şifreleme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifrele"
    elif(algoritma.get()=="Sezar Çözme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifreyi Çöz"
    elif(algoritma.get()=="Çit Çözme"):
        key_icerik['state']='readonly'
        add_btn["text"]="Şifreyi Çöz"
    elif(algoritma.get()=="Kolon Çözme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifreyi Çöz"
    elif(algoritma.get()=="Vigenere Çözme"):
        key_icerik['state']='normal'
        add_btn["text"]="Şifreyi Çöz"
     
def secici():
    if(algoritma.get()=="Sezar Şifreleme"):
        sifreli.config(state=NORMAL)
        sifreli.delete(1.0, END)
        sezarsif(part_text.get(),key_text.get())
    elif(algoritma.get()=="Çit Şifreleme"):
        sifreli.config(state=NORMAL)
        sifreli.delete(1.0, END)
        citsif(part_text.get())
    elif(algoritma.get()=="Kolon Şifreleme"):
        sifreli.config(state=NORMAL)
        sifreli.delete(1.0, END)
        kolonsif(part_text.get(),key_text.get())
    elif(algoritma.get()=="Polybius Şifreleme"):
        sifreli.config(state=NORMAL)
        sifreli.delete(1.0,END)
        polybius(part_text.get())
    elif(algoritma.get()=="Vigenere Şifreleme"):
        durum=0
        sifreli.config(state=NORMAL)
        sifreli.delete(1.0,END)
        vinegeresif(part_text.get(),key_text.get(),durum)
    elif(algoritma.get()=="Sezar Çözme"):
        cozulmus.config(state=NORMAL)
        cozulmus.delete(1.0,END)
        sezarcoz(part_text.get(),key_text.get())
    elif(algoritma.get()=="Çit Çözme"):
        cozulmus.config(state=NORMAL)
        cozulmus.delete(1.0,END)
        citcoz(part_text.get())
    elif(algoritma.get()=="Kolon Çözme"):
        cozulmus.config(state=NORMAL)
        cozulmus.delete(1.0,END)
        koloncoz(part_text.get(),key_text.get())
    elif(algoritma.get()=="Vigenere Çözme"):
        durum=1
        cozulmus.config(state=NORMAL)
        cozulmus.delete(1.0,END)
        vinegeresif(part_text.get(),key_text.get(),durum)
        
#Sezar başlangıç
def sezarsif(text,s): 
    result = "" 
    s=int(s)
    for char in text:
        if(char==' '):
            result+='$'
        else:
            shift = 97 if char.islower() else 65
            result+=chr((ord(char) + s - shift) % 26 + shift)
    sifreli.insert(END,result)
    sifreli.config(state=DISABLED)

def sezarcoz(text,s): 
    result = "" 
    s=int(s)
    for char in text:
        if(char=='$'):
            result+=' '
        else:
            shift = 97 if char.islower() else 65
            result+=chr((ord(char) - s - shift) % 26 + shift)
    cozulmus.insert(INSERT,result)
    cozulmus.config(state=DISABLED)
#sezar bitiş
#polybius başlangıç
def polybius(s):
        result="" 
        for char in s: 
                if (char.isupper()): 
                    row = int((ord(char) - ord('A')) / 5) + 1 
                    col = int((ord(char) - ord('A')) % 5) + 1
                    
                    if ord(char) >= ord('J'): 
                            if col == 1 : 
                                col = 6
                                row = row - 1
                              
                            col = col - 1
                else: 
                    row = int((ord(char) - ord('a')) / 5) + 1 
                    col = int((ord(char) - ord('a')) % 5) + 1
                    
                    if ord(char) >= ord('j'): 
                            if col == 1 : 
                                col = 6
                                row = row - 1
                            col = col - 1
                
                result+=str(row)+""+str(col)+" "
        sifreli.insert(INSERT,result)
        sifreli.config(state=DISABLED)

#polybius bitiş

#kolon başlangucı
def kolonsif(text,key):
    textlen=len(text)
    matrisrowsize=textlen/int(key)
    matrisrowsize=math.ceil(matrisrowsize)
    Matrix = [[0 for x in range(int(key))] for y in range(matrisrowsize)]
    tempsayac=0
    tempdegisken=""
    for i in range(matrisrowsize):
        for j in range(int(key)):
            if(tempsayac>=len(text)):
                randomsayi=randrange(25)
                Matrix[i][j]=alfabe_eng1[randomsayi]
            else:
                Matrix[i][j]=text[tempsayac]
            tempsayac+=1
    Matrix2=np.array(Matrix)
    Matrix3=Matrix2.transpose()
    for k in range(int(key)):
        for l in range(matrisrowsize):
                tempdegisken+=Matrix3[k][l]
    sifreli.insert(INSERT,tempdegisken)
    sifreli.config(state=DISABLED)

def koloncoz(text,key):
    textlen=len(text)
    matrisrowsize=textlen/int(key)
    matrisrowsize=math.ceil(matrisrowsize)
    Matrix = [[0 for x in range(matrisrowsize)] for y in range(int(key))]
    tempsayac=0
    tempdegisken=""
    for i in range(int(key)):
        for j in range(matrisrowsize):
                Matrix[i][j]=text[tempsayac]
                tempsayac+=1
        
    Matrix2=np.array(Matrix)
    Matrix3=Matrix2.transpose()
    for k in range(matrisrowsize):
        for l in range(int(key)):
                tempdegisken+=Matrix3[k][l]
    cozulmus.insert(INSERT,tempdegisken)
    cozulmus.config(state=DISABLED)

#kolon bitiş

#vinegere baslangıç
def sezar(letter, rot,state):
    if(state==0):
        karakter = 97 if letter.islower() else 65
        return chr((ord(letter) + rot - karakter) % 26 + karakter)
    elif(state==1):
        karakter = 97 if letter.islower() else 65
        return chr((ord(letter) - rot - karakter) % 26 + karakter)

def vinegeresif(text, key,state):
    farklielemansayisi=0
    for char in key:
        if not char in alfabe_eng:
            farklielemansayisi+=1
    if(farklielemansayisi==0):
        sifrelli = []    
        start_key_index = 0
        state=state
        for char in text:
            rotation = alfabe(key[start_key_index])
            if not char in alfabe_eng:
                sifrelli.append(char)
            else:            
                sifrelli.append(sezar(char, rotation,state))             

            if start_key_index == (len(key) - 1): 
                start_key_index = 0
            else: 
                start_key_index += 1
        if(state==0):
            sonuc=''.join(sifrelli)
            sifreli.insert(INSERT,sonuc)
            sifreli.config(state=DISABLED)
        elif(state==1):
            sonuc=''.join(sifrelli)
            cozulmus.insert(INSERT,sonuc)
            cozulmus.config(state=DISABLED)
    else:
        if(state==0):
            sifreli.insert(INSERT,'Şifrelemek için girdiğiniz key numara, türkçe karakter veya sembol içermektedir... Sadece metin girişine izin verilir.')
        elif(state==1):
            cozulmus.insert(INSERT,'Çözmek için girdiğiniz key numara, türkçe karakter veya sembol içermektedir... Sadece metin girişine izin verilir.')
#vinegere bitiş


#cit başlangic
def citsif(text):
    cift=[]
    tek=[]
    temp=0
    for i in range(round(len(text)/2)):
        if(text[temp]==' '):
            cift.append(" ")
            tek.append(text[temp+1])
            temp+=2
        elif(text[temp+1]==' '):
            cift.append(text[temp])
            tek.append(" ")
            temp+=2
        else:
            cift.append(text[temp])
            tek.append(text[temp+1])
            temp+=2
        if(temp+1==len(text)):
            cift.append(text[len(text)-1])
            break
    sifreli1=''.join(cift)+''.join(tek)
    sifreli.insert(INSERT,sifreli1)
    sifreli.config(state=DISABLED)
def citcoz(text):
    cift=[]
    tek=[]
    cozum=[]
    temp=0
    if(len(text)%2!=0):
        for i in range(math.floor(len(text)/2)+1):
            cift.append(text[i])
        for j in range(math.floor(len(text)/2)+1,len(text)):
            tek.append(text[j])
        for k in range(math.floor(len(text)/2)):
            cozum.append(cift[temp])
            cozum.append(tek[temp])
            temp+=1
            if(temp==math.floor(len(text)/2)):
                cozum.append(cift[temp])
                break
        sonuccit=''.join(cozum)     
        cozulmus.insert(INSERT,sonuccit)
        cozulmus.config(state=DISABLED)
    else:
        for i in range(round(len(text)/2)):
            cift.append(text[i])
        for j in range(round(len(text)/2),len(text)):
            tek.append(text[j])
        for k in range(round(len(text)/2)):
            cozum.append(cift[temp])
            cozum.append(tek[temp])
            temp+=1
        sonuccit=''.join(cozum)     
        cozulmus.insert(INSERT,sonuccit)
        cozulmus.config(state=DISABLED)
        
# cit bitis



app = Tk()

part_label=Label(app, text='Lütfen Metin giriniz', font=('bold',11),pady=20)
part_label.grid(row=0,column=0)
part_text=StringVar()
part_metin=Entry(app, textvariable=part_text)
part_metin.grid(row=0,column=1,ipadx=60,pady=10)


key_label=Label(app, text='Lütfen Şifre giriniz', font=('bold',11),pady=20)
key_label.grid(row=1,column=0)

key_text=StringVar()
key_icerik=Entry(app, textvariable=key_text)
key_icerik.grid(row=1,column=1,ipadx=60,pady=10)


add_btn=Button(app,text="Şifrele",width=12, command=secici)
add_btn.grid(row=2,column=1,pady=20)

n=StringVar()
algoritma=Combobox(app,width=27,textvariable=n, state='readonly')
algoritma['values']=('Sezar Şifreleme','Sezar Çözme','Çit Şifreleme','Çit Çözme',
                     'Kolon Şifreleme','Kolon Çözme','Polybius Şifreleme','Vigenere Şifreleme','Vigenere Çözme')
algoritma.grid(row=2,column=0,pady=20,padx=20)
algoritma.current(0)
algoritma.bind("<<ComboboxSelected>>", modified) 

normal=Label(app, text='', font=('bold',11),pady=20,padx=20)
normal.grid(row=3,column=1, sticky=W)


sifrelilabel=Label(app, text='Şifreli Metin ', font=('bold',11),pady=20,padx=20)
sifrelilabel.grid(row=4,column=0, sticky=W)

sifreli=Text(app,height=8,width=50)
sifreli.grid(row=4,column=1,rowspan=6,padx=20)

scrollbar1=Scrollbar(app)
scrollbar1.grid(row=4,column=2)

sifreli.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=sifreli.yview)

cozulmuslabel=Label(app, text='Çözülmüş Metin ', font=('bold',11),pady=20,padx=20)
cozulmuslabel.grid(row=11,column=0, sticky=W)


cozulmus=Text(app,height=8,width=50)
cozulmus.grid(row=11,column=1,rowspan=6,padx=20)
                 
scrollbar2=Scrollbar(app)
scrollbar2.grid(row=11,column=2)

cozulmus.configure(yscrollcommand=scrollbar2.set)
scrollbar2.configure(command=cozulmus.yview)

app.title('Sezar')
app.geometry('700x600')
app.mainloop()

