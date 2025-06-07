from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab

root = Tk()
root.title('Paint Applicatie')
try:
    root.iconbitmap(default="Paint.ico")
except:
    pass
root.resizable(0, 0)
root.state('zoomed')

geladen_afbeelding = None
id_afbeelding = None
getekende_objecten = []
huidige_stroke = []
huidige_kleur = 'black'
penseel_grootte = IntVar(value=6)
gum_ingeschakeld = False
penseel = "oval"

kleur_frame = Frame(root, padx=5, pady=5)
kleur_frame.pack(side=LEFT, anchor="n")

felle_kleuren = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'gray','magenta', 'cyan', 'lime']
pastel_kleuren = ['#FFC0CB', '#FFDAB9', '#E6E6FA', '#B0E0E6', '#F5DEB3', '#98FB98', '#FFFACD', '#D8BFD8', '#AFEEEE','#FFB6C1', '#CAE1FF', '#F0E68C']
vintage_kleuren = ['#D36C6C', '#9A9E5E', '#30475E', '#B4B300', '#F1C6A9', '#8F5E3C', '#8A9A5B', '#B7410E', '#9B5F8C','#C4A69F', '#726255', '#A39887']

Label(kleur_frame, text="Penseelgrootte").pack(pady=(15, 0))
Scale(kleur_frame, from_=1, to=200, orient=HORIZONTAL, variable=penseel_grootte).pack()

kleur_preview = Canvas(kleur_frame, width=30, height=30, highlightthickness=1, highlightbackground="black")
kleur_preview.pack(side=BOTTOM, padx=5, pady=15)
kleur_preview.create_oval(3, 3, 28, 28, fill=huidige_kleur, outline=huidige_kleur)

def toggle_penseel():
    global penseel
    penseel = "square" if penseel == "oval" else "oval"
    update_kleur()

def toggle_gum():
    global gum_ingeschakeld
    gum_ingeschakeld = not gum_ingeschakeld
    update_kleur()

def update_kleur():
    global huidige_kleur
    huidige_kleur = 'white' if gum_ingeschakeld else 'black'
    kleur_preview.delete("all")
    if penseel == "oval":
        kleur_preview.create_oval(3, 3, 28, 28, fill=huidige_kleur, outline=huidige_kleur)
    else:
        kleur_preview.create_rectangle(3, 3, 28, 28, fill=huidige_kleur, outline=huidige_kleur)

try:
    icon_eraser = PhotoImage(file='eraser.png')
except:
    icon_eraser = ""

try:
    icon_penseel = PhotoImage(file='penseel.png')
except:
    icon_penseel = ""

penseel_button = Button(kleur_frame, image=icon_penseel, command=toggle_penseel)
penseel_button.pack(pady=(15,0))
Label(kleur_frame, text="Penseel style").pack(pady=(5, 0))

gum_button = Button(kleur_frame, image=icon_eraser, command=toggle_gum)
gum_button.pack(pady=(15,0))
Label(kleur_frame, text="Gum").pack(pady=(5, 0))

def verander_kleur_canvas(event, kleur):
    global huidige_kleur, gum_ingeschakeld
    gum_ingeschakeld = False
    huidige_kleur = kleur
    kleur_preview.delete("all")
    if penseel == "oval":
        kleur_preview.create_oval(3, 3, 28, 28, fill=huidige_kleur, outline=huidige_kleur)
    else:
        kleur_preview.create_rectangle(3, 3, 28, 28, fill=huidige_kleur, outline=huidige_kleur)

Label(kleur_frame, text="Kleuren").pack(pady=(15, 0))
kleuren_container = Frame(kleur_frame)
kleuren_container.pack(pady=10)

for i, kleur in enumerate(felle_kleuren):
    kleur_canvas = Canvas(kleuren_container, width=20, height=20, bg=kleur, highlightthickness=1, highlightbackground='black')
    kleur_canvas.grid(row=i, column=0, padx=3, pady=2)
    kleur_canvas.bind("<Button-1>", lambda e, c=kleur: verander_kleur_canvas(e, c))

for i, kleur in enumerate(pastel_kleuren):
    kleur_canvas = Canvas(kleuren_container, width=20, height=20, bg=kleur, highlightthickness=1, highlightbackground='black')
    kleur_canvas.grid(row=i, column=1, padx=3, pady=2)
    kleur_canvas.bind("<Button-1>", lambda e, c=kleur: verander_kleur_canvas(e, c))

for i, kleur in enumerate(vintage_kleuren):
    kleur_canvas = Canvas(kleuren_container, width=20, height=20, bg=kleur, highlightthickness=1, highlightbackground='black')
    kleur_canvas.grid(row=i, column=3, padx=5, pady=2)
    kleur_canvas.bind("<Button-1>", lambda e, c=kleur: verander_kleur_canvas(e, c))

Label(kleur_frame, text="Gekozen Kleur").pack(pady=(15, 0))

canvas = Canvas(root, bg="white")
canvas.pack(fill=BOTH, expand=True)

def over_venster():
    over = Toplevel()
    over.title('Over Paint Applicatie')
    over.resizable(0, 0)
    x = (over.winfo_screenwidth() // 2) - 150
    y = (over.winfo_screenheight() // 2) - 150
    over.geometry(f"300x300+{x}+{y}")
    over_img = Image.open('About.png').resize((220, 220), Image.BILINEAR)
    over_img = ImageTk.PhotoImage(over_img)
    panel = Label(over, image=over_img)
    panel.image = over_img
    panel.pack()
    Label(over, text="Simpele Paint Applicatie \nGemaakt door Joël van Houten\n Met VScode & Python", pady=30).pack()

def open_bestand():
    return filedialog.askopenfilename(title='Open', filetypes=[("Afbeeldingen", "*.png *.jpg *.jpeg *.bmp")])

def open_afbeelding():
    bestand_naam = open_bestand()
    if bestand_naam:
        root.after(100, lambda: open_afbeelding_op_canvas(bestand_naam))

def open_afbeelding_op_canvas(pad):
    global geladen_afbeelding, id_afbeelding
    img = Image.open(pad)
    canvas_width, canvas_height = canvas.winfo_width(), canvas.winfo_height()
    img_width, img_height = img.size
    ratio = min(canvas_width / img_width, canvas_height / img_height)
    new_width = int(img_width * ratio)
    new_height = int(img_height * ratio)
    img = img.resize((new_width, new_height), Image.BILINEAR)
    geladen_afbeelding = ImageTk.PhotoImage(img)
    canvas.delete("all")
    x = (canvas_width - new_width) // 2
    y = (canvas_height - new_height) // 2
    id_afbeelding = canvas.create_image(x, y, anchor=NW, image=geladen_afbeelding)

def teken(event):
    grootte = penseel_grootte.get()
    x, y = event.x, event.y
    kleur = 'white' if gum_ingeschakeld else huidige_kleur
    if penseel == "oval":
        nieuw_object = canvas.create_oval(x-grootte, y-grootte, x+grootte, y+grootte, fill=kleur, outline=kleur)
    else:
        nieuw_object = canvas.create_rectangle(x-grootte, y-grootte, x+grootte, y+grootte, fill=kleur, outline=kleur)
    huidige_stroke.append(nieuw_object)

def nieuwe_stroke():
    global huidige_stroke
    huidige_stroke = []
    getekende_objecten.append(huidige_stroke)

canvas.bind("<B1-Motion>", teken)
canvas.bind("<Button-1>", lambda e: nieuwe_stroke())

def undo(event):
    if getekende_objecten:
        laatste_stroke = getekende_objecten.pop()
        for obj in laatste_stroke:
            canvas.delete(obj)

root.bind("<Control-z>", undo)

def nieuw_bestand(event):
    vraag = messagebox.askquestion('Nieuw Bestand', 'Wilt u echt doorgaan zonder het huidige bestand eerst op te slaan?')
    if vraag == 'yes':
        canvas.delete("all")

root.bind("<Control-n>", nieuw_bestand)

def afbeelding_opslaan():
    bestand = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG bestand", "*.jpg")])
    if bestand:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(bestand)

taakbalk = Menu(root)
root.config(menu=taakbalk)

filemenu = Menu(taakbalk, tearoff=0)
taakbalk.add_cascade(label='Bestand', menu=filemenu)
filemenu.add_command(label='Nieuw          Ctrl + N', command=nieuw_bestand)
filemenu.add_command(label='Open afbeelding...', command=open_afbeelding)
filemenu.add_command(label='Afbeelding opslaan...', command=afbeelding_opslaan)
filemenu.add_separator()
filemenu.add_command(label='Afsluiten      Alt + F4', command=root.quit)

bewerkmenu = Menu(taakbalk, tearoff=0)
taakbalk.add_cascade(label='Bewerk', menu=bewerkmenu)
bewerkmenu.add_command(label='Ongedaan maken    Ctrl + Z', command=undo)

helpmenu = Menu(taakbalk, tearoff=0)
taakbalk.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Over', command=over_venster)

root.mainloop()
