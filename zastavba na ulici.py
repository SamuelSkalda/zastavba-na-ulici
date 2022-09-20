import tkinter
canvas = tkinter.Canvas(width=500, height=150, bg='white')
canvas.pack()

subor = open('zastavba_na_ulici.txt', 'r')
vyska = []
sirka = []

def nacitanie():
    for riadok in subor:
        riadok = riadok.split()
        sirka.append(int(riadok[0]))
        vyska.append(int(riadok[1]))
        
def vykreslenie():
    canvas.delete('all')
    nacitanie()
    rozdiel = int(entry1.get())
    x = 10
    y = 120
    for i in range(len(vyska)):
        if vyska[i] > 0:
            canvas.create_rectangle(x,y,x+sirka[i],y-vyska[i],fill='grey')
        else:
            canvas.create_line(x,y,x+sirka[i],y,fill='green',width=4)
        if i < 4 and vyska[i]-vyska[i+1] >= rozdiel:
            canvas.create_line(x+sirka[i],y-vyska[i+1],x+sirka[i],y-vyska[i],fill='red',width=2)
        if i > 0 and vyska[i]-vyska[i-1] >= rozdiel:
            canvas.create_line(x,y-vyska[i-1],x,y-vyska[i],fill='red',width=2)
        x = x + sirka[i]
        
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='vykresli', command = vykreslenie)
button1.pack()
        
            
    