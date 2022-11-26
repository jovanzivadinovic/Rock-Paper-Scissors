from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()

text_win_eng = "Wins: "
text_tie_eng = "Ties: "
text_losses_eng = "Losses: "

text_win_srb = "Pobede: "
text_tie_srb = "Nereseno: "
text_losses_srb = "Porazi: "

text_naslov_eng = "ROCK, PAPER, SCISSORS!"
text_naslov_srb = "PAPIR, KAMEN, MAKAZE!"

nereseno_eng = "TIE"
pobeda_eng = "WIN"
poraz_eng = "LOSS"

nereseno_srb = "NERESENO"
pobeda_srb = "POBEDA"
poraz_srb = "PORAZ"

win_screen_eng = "CONGRATULATIONS,\nYOU WON!"
win_screen_srb = "POBEDIO SI!"

lost_screen_eng = "SORRY,\nYOU LOST..."
lost_screen_srb = "IZGUBIO SI!"

tie_screen_eng = "IT'S A TIE"
tie_screen_srb = "NERESENO JE!"

play_again_eng = "PLAY AGAIN"
play_again_srb = "IGRAJ PONOVO"

exit_eng = "EXIT"
exit_srb = "IZLAZ"

pravila_eng = "Rules:"
pravila_srb = "Pravila:"

confirm_eng = "Confirm"
confirm_srb = "Potvrdi"

prvi_do_eng = "First to: "
prvi_do_srb = "Prvi do:"

najbolji_od_eng = "Best out of: "
najbolji_od_srb = "Najbolji od: "

jezik_eng = "Language:"
jezik_srb = "Jezik:"

boja_dark = "#03254c"
boja_light = "#ADD8E6"
switch_dark1 = Image.open("switch_dark.png")
switch_dark2 = switch_dark1.resize((50,50))
switch_dark = ImageTk.PhotoImage(switch_dark2)

switch_light1 = Image.open("switch_light.png")
switch_light2 = switch_light1.resize((50,50))
switch_light = ImageTk.PhotoImage(switch_light2)


vel_slike = 90


kamen2 = Image.open("kamen_dark.png")
kamen3=kamen2.resize((vel_slike, vel_slike))
kamen_dark=ImageTk.PhotoImage(kamen3)



papir2 = Image.open("papir_dark.png")
papir3=papir2.resize((vel_slike, vel_slike))
papir_dark=ImageTk.PhotoImage(papir3)



makaze2 = Image.open("makaze_dark.png")
makaze3=makaze2.resize((vel_slike, vel_slike))
makaze_dark=ImageTk.PhotoImage(makaze3)



kamen_slika1 = Image.open("kamen_dark.png")
kamen_slika2 = kamen_slika1.resize((vel_slike*3, vel_slike*3))
kamen_slika_dark = ImageTk.PhotoImage(kamen_slika2)





kamen_protivnik_dark1 = kamen_slika2.transpose(Image.FLIP_LEFT_RIGHT)
kamen_protivnik_dark = ImageTk.PhotoImage(kamen_protivnik_dark1)





papir_slika1 = Image.open("papir_dark.png")
papir_slika2 = papir_slika1.resize((vel_slike*3, vel_slike*3))
papir_slika_dark = ImageTk.PhotoImage(papir_slika2)





papir_protivnik_dark1 = papir_slika2.transpose(Image.FLIP_LEFT_RIGHT)
papir_protivnik_dark = ImageTk.PhotoImage(papir_protivnik_dark1)






makaze_slika1 = Image.open("makaze_dark.png")
makaze_slika2 = makaze_slika1.resize((vel_slike*3, vel_slike*3))
makaze_slika_dark = ImageTk.PhotoImage(makaze_slika2)





makaze_protivnik_dark1 = makaze_slika2.transpose(Image.FLIP_LEFT_RIGHT)
makaze_protivnik_dark = ImageTk.PhotoImage(makaze_protivnik_dark1)




class Players:
    igrac = 0
    protivnik = 0
    counter_wins = 0
    counter_losses = 0
    counter_ties = 0
    
    switch_value = True

font="Arial"

class Rules:
    num = 3
    br = 0
    r=IntVar()
    
    jezik = 1
    
class Language:
    text_pobeda = text_win_eng
    text_nereseno = text_tie_eng
    text_poraz = text_losses_eng
    pobeda = pobeda_eng
    nereseno = nereseno_eng
    poraz = poraz_eng

    win_screen = win_screen_eng
    lost_screen = lost_screen_eng
    tie_screen = tie_screen_eng

    play_again_text = play_again_eng
    exit_text = exit_eng
    pravila_text = pravila_eng
    confirm_text = confirm_eng

    prvi_do_text = prvi_do_eng
    najbolji_od_text = najbolji_od_eng
    jezik_text = jezik_eng
    
    










root.geometry("1000x800")
root.title("Rock, Paper, Scissors!")
root.configure(bg=boja_light)
root.iconbitmap("ikonica.ico")


naslov = Label(root, text=text_naslov_eng, height=2, font=(font, 40), fg="black", bg=boja_light)
naslov.pack()

switch = Button(root, image = switch_dark, height=50, width=50, bg=boja_light, bd=0, command=lambda:mode())
switch.place(relx=0.9, y=100)


kamen_dugme = Button(root, image=kamen_dark, height=vel_slike, width=vel_slike, bd=0, bg=boja_light, command=lambda:(kamen_func(), protivnik_func(), rezultat(), brojac(), kraj()))
kamen_dugme.place(relx=0.4, y=160, anchor=CENTER)

papir_dugme = Button(root, image=papir_dark, height=vel_slike, width=vel_slike, bd=0, bg=boja_light, command=lambda:(papir_func(), protivnik_func(), rezultat(), brojac(), kraj()))
papir_dugme.place(relx=0.5, y=160, anchor=CENTER)

makaze_dugme = Button(root, image=makaze_dark, height=vel_slike, width=vel_slike, bd=0, bg=boja_light, command=lambda:(makaze_func(), protivnik_func(), rezultat(), brojac(), kraj()))
makaze_dugme.place(relx=0.6, y=160, anchor=CENTER)


player = Label(root, bg=boja_light)


def restart():
    Players.counter_losses = 0
    Players.counter_ties = 0
    Players.counter_wins = 0

    counter_label_losses.config(text=" ")
    counter_label_ties.config(text=" ")
    counter_label_wins.config(text=" ")

    rez.config(text="")

def kamen_func():
    
    player.config(image=kamen_slika_dark)
    player.place(relx=0.3, y=400, anchor=CENTER)

    Players.igrac = 0


def papir_func():
    
    player.config(image=papir_slika_dark)
    player.place(relx=0.3, y=400,anchor=CENTER)

    Players.igrac = 1

    

def makaze_func():
    
    player.config(image=makaze_slika_dark)
    player.place(relx=0.3, y=400, anchor=CENTER)

    Players.igrac = 2


enemy = Label(root, bg=boja_light)
def protivnik_func():
    Players.protivnik = random.randint(0,2)
    if Players.protivnik==0:
        enemy.config(image=kamen_protivnik_dark)
        enemy.place(relx=0.7, y=400, anchor=CENTER)
        
    elif Players.protivnik==1:
        enemy.config(image=papir_protivnik_dark)
        enemy.place(relx=0.7, y=400, anchor=CENTER)
    else:
        enemy.config(image=makaze_protivnik_dark)
        enemy.place(relx=0.7, y=400, anchor=CENTER)


def mode():
    if(Players.switch_value):
        switch.config(image=switch_light, bg=boja_dark)
        naslov.config(fg="white", bg=boja_dark)
        kamen_dugme.config( bg=boja_dark)
        papir_dugme.config( bg=boja_dark)
        makaze_dugme.config( bg=boja_dark)
        root.config(bg=boja_dark)
        player.config(bg=boja_dark)
        
        enemy.config( bg=boja_dark)

        rez.config(bg=boja_dark)
        

        counter_label_losses.config(bg=boja_dark)
        counter_label_ties.config(bg=boja_dark)
        counter_label_wins.config(bg=boja_dark)
        
        Players.switch_value = False
    else:
        switch.config(image=switch_dark, bg=boja_light)
        naslov.config(fg=boja_dark, bg=boja_light)
        kamen_dugme.config( bg=boja_light)
        papir_dugme.config( bg=boja_light)
        makaze_dugme.config( bg=boja_light)
        root.config(bg=boja_light)
        player.config( bg=boja_light)
        
        enemy.config(bg=boja_light)

        rez.config(bg=boja_light)
        

        counter_label_losses.config(bg=boja_light)
        counter_label_ties.config(bg=boja_light)
        counter_label_wins.config(bg=boja_light)
        
        
        Players.switch_value = True
    
    







rez = Label(root, font=(font, 20), height=2, width=10, bg=boja_light)
counter_label_ties = Label(root, text=text_tie_eng+str(Players.counter_ties), fg="#e69b00", font=(font, 20), bg=boja_light )
counter_label_wins = Label(root, text=text_win_eng+str(Players.counter_wins), fg="green", font=(font, 20), bg=boja_light )
counter_label_losses = Label(root, text=text_losses_eng+str(Players.counter_losses), fg="red", font=(font, 20), bg=boja_light )

def nereseno():
    Players.counter_ties+=1
    
    counter_label_ties.config(text=Language.text_nereseno+str(Players.counter_ties))
    
    counter_label_ties.place(relx=0.5, y=700, anchor=CENTER)
    rez.config(text=Language.nereseno, fg="#e69b00")
    rez.place(relx=0.5, y=600, anchor=CENTER)


def pobeda():
    Players.counter_wins+=1
    counter_label_wins.config(text=Language.text_pobeda+str(Players.counter_wins))

    counter_label_wins.place(relx=0.2, y=700, anchor=CENTER)
    rez.config(text=Language.pobeda, fg="green")
    rez.place(relx=0.5, y=600, anchor=CENTER)
    

def poraz():
    Players.counter_losses+=1
    counter_label_losses.config(text=Language.text_poraz+str(Players.counter_losses))

    counter_label_losses.place(relx=0.8, y=700, anchor=CENTER)
    rez.config(text=Language.poraz, fg="red")
    rez.place(relx=0.5, y=600, anchor=CENTER)
    


def rezultat():
    
    if (Players.protivnik==2 and Players.igrac==1):
        poraz()
    if (Players.protivnik==0 and Players.igrac==1):
        pobeda()
    if (Players.protivnik==0 and Players.igrac==2):
        poraz()
    if(Players.protivnik==1 and Players.igrac==0):
        poraz()
    if(Players.protivnik==1 and Players.igrac==2):
        pobeda()
    if(Players.protivnik==2 and Players.igrac==0):
        pobeda()
    if(Players.igrac==Players.protivnik):
        nereseno()


def end_win():
    win = Toplevel()
    win.iconbitmap("ikonica.ico")
    win.geometry("500x500")
    win.config(bg="green")
    tekst = Label(win, text=Language.win_screen, font=(font, 35), fg="white", bg="green")
    tekst.place(relx=0.5, rely=0.4, anchor=CENTER)
    restart()

    

    def play_again():
        win.destroy()
    def exit():
        root.destroy()

    again = Button(win, text=Language.play_again_text, bg="green", fg="white", bd=0, command=lambda:play_again())
    again.place(relx=0.4, rely=0.6, anchor=CENTER)
    quit = Button(win, text=Language.exit_text, bg="green", fg="white", bd=0,command=lambda:exit())
    quit.place(relx=0.6, rely=0.6, anchor=CENTER)


    

def end_loss():
    loss = Toplevel()
    loss.geometry("500x500")
    loss.iconbitmap("ikonica.ico")
    loss.config(bg="red")
    tekst = Label(loss, text=Language.lost_screen, font=(font, 40), fg="white", bg="red")
    tekst.place(relx=0.5, rely=0.4, anchor=CENTER)    
    restart()

    

    def play_again():
        loss.destroy()
    def exit():
        root.destroy()

    again = Button(loss, text=Language.play_again_text, bg="red", fg="white", bd=0, command=lambda:play_again())
    again.place(relx=0.4, rely=0.6, anchor=CENTER)
    quit = Button(loss, text=Language.exit_text, bg="red", fg="white", bd=0, command=lambda:exit())
    quit.place(relx=0.6, rely=0.6, anchor=CENTER)


    

def end_tie():
    tie = Toplevel()
    tie.geometry("500x500")
    tie.iconbitmap("ikonica.ico")
    tie.config(bg="grey")
    tekst = Label(tie, text=Language.tie_screen, font=(font, 40), fg="white", bg="grey")
    tekst.place(relx=0.5, rely=0.4, anchor=CENTER)    
    restart()

    
    
    def play_again():
        tie.destroy()
    def exit():
        root.destroy()
    again = Button(tie, text=Language.play_again_text, bg="grey", fg="white", bd=0, command=lambda:play_again())
    again.place(relx=0.4, rely=0.6, anchor=CENTER)
    quit = Button(tie, text=Language.exit_text, bg="grey", fg="white", bd=0, command=lambda:exit())
    quit.place(relx=0.6, rely=0.6, anchor=CENTER)


def first_to():
    if (Rules.num == Players.counter_wins):
        end_win()
    
        
    if (Rules.num == Players.counter_losses):
        end_loss()
    

def out_of():
    if (Rules.num==Players.counter_losses+Players.counter_ties+Players.counter_wins):
        if(Players.counter_wins>Players.counter_losses and Players.counter_wins>=Players.counter_ties):
            end_win()
        elif(Players.counter_losses>Players.counter_wins and Players.counter_losses>=Players.counter_ties):
            end_loss()
        else:
            end_tie()

def promena_srpski():
    Language.text_nereseno = text_tie_srb
    Language.text_pobeda = text_win_srb
    Language.text_poraz = text_losses_srb

    counter_label_losses.config(text=text_losses_srb+str(Players.counter_losses))
    counter_label_ties.config(text=text_tie_srb+str(Players.counter_ties))
    counter_label_wins.config(text=text_win_srb+str(Players.counter_wins))
    
    naslov.config(text=text_naslov_srb)

    Language.poraz = poraz_srb
    Language.pobeda = pobeda_srb
    Language.nereseno = nereseno_srb

    rez.config(text="")

    Language.win_screen = win_screen_srb
    Language.lost_screen = lost_screen_srb
    Language.tie_screen = tie_screen_srb

    Language.play_again_text = play_again_srb
    Language.exit_text = exit_srb

    options_menu.entryconfig("Rules", label="Pravila")
    options_menu.entryconfig("Language", label="Jezik")
    my_menu.entryconfig("Options", label="Podesavanja")

    Language.pravila_text = pravila_srb

    Language.najbolji_od_text = najbolji_od_srb
    Language.prvi_do_text = prvi_do_srb
    Language.jezik_text = jezik_srb

    Language.confirm_text = confirm_srb

def promena_engleski():
    Language.text_nereseno = text_tie_eng
    Language.text_pobeda = text_win_eng
    Language.text_poraz = text_losses_eng
    naslov.config(text=text_naslov_eng)

    counter_label_losses.config(text=text_losses_eng)
    counter_label_ties.config(text=text_tie_eng)
    counter_label_wins.config(text=text_win_eng)

    Language.poraz = poraz_eng
    Language.pobeda = pobeda_eng
    Language.nereseno = nereseno_eng

    rez.config(text="")

    Language.win_screen = win_screen_eng
    Language.lost_screen = lost_screen_eng
    Language.tie_screen = tie_screen_eng

    Language.play_again_text = play_again_eng
    Language.exit_text = exit_eng

    options_menu.entryconfig("Pravila", label="Rules")
    options_menu.entryconfig("Jezik", label="Language")
    my_menu.entryconfig("Podesavanja", label="Options")
    Language.pravila_text = pravila_eng

    Language.najbolji_od_text = najbolji_od_eng
    Language.prvi_do_text = prvi_do_eng
    Language.jezik_text = jezik_eng

    Language.confirm_text = confirm_eng

def rules():
    
    new = Toplevel()
    new.geometry("500x500")
    new.title("Rock, Paper, Scissors!")
    new.iconbitmap("ikonica.ico")
   
    

    naslov1 = Label(new, text=Language.pravila_text,  font=(font, 20) )
    naslov1.place(relx=0.1, rely=0.1)

    
    

    Radiobutton(new, text=Language.prvi_do_text, variable=Rules.r, value=1).place(relx=0.1, rely=0.3)
    Radiobutton(new, text=Language.najbolji_od_text, variable=Rules.r, value=2).place(relx=0.1, rely=0.4)
    
    v = IntVar()

    e = Entry(new, textvariable=v)
    e.place(relx=0.4, rely=0.35)
    
    click = Button(new, text=Language.confirm_text,  command=lambda:rule())
    click.place(relx=0.35, rely=0.6)
    
    def rule():
        Rules.num = v.get()
        Rules.br+=1
        restart()

        new.destroy()
    
        
        
        
            

    new.mainloop()

def lang():
    
    new = Toplevel()
    new.geometry("500x500")
    new.title("Rock, Paper, Scissors!")
    new.iconbitmap("ikonica.ico")
   
    

    naslov1 = Label(new, text=Language.jezik_text,  font=(font, 20) )
    naslov1.place(relx=0.1, rely=0.1)

    
    l = IntVar()

    Radiobutton(new, text="English", variable=l, value=1).place(relx=0.1, rely=0.3)
    Radiobutton(new, text="Srpski", variable=l, value=2).place(relx=0.1, rely=0.4)
    
    
    
    click = Button(new, text=Language.confirm_text,  command=lambda:rule())
    click.place(relx=0.35, rely=0.6)
    
    def rule():
        Rules.jezik = l.get()
        new.destroy()
        jezik()

        
    
        
        
        
            

    new.mainloop()

def brojac():
    
    if Rules.br == 0:
        Players.counter_losses = 0
        Players.counter_ties = 0
        Players.counter_wins =0

        counter_label_losses.config(text=" ")
        counter_label_ties.config(text=" ")
        counter_label_wins.config(text=" ")

        rez.config(text=" ")
        player.config(image="")
        enemy.config(image="")
        rules()

def jezik():
    if Rules.jezik == 1:
        promena_engleski()
    else:
        promena_srpski()

def kraj():
    if Rules.r.get()==1:
        first_to()
        
    elif Rules.r.get()==2:
        out_of()
        



my_menu = Menu(root)
root.config(menu=my_menu)


options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rules", command=lambda:rules())
options_menu.add_command(label="Language", command=lambda:lang())













root.mainloop()
















