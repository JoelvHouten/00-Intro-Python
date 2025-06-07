from tkinter import *
from PIL import Image, ImageTk
import random
import os
import string

class SpelStatus:
    def __init__(self, woordlijst, score_pad, afbeelding_pad):
        self.woordlijst = woordlijst
        self.score_pad = score_pad
        self.afbeelding_pad = afbeelding_pad
        self.reset()

    def reset(self):
        self.woord = random.choice(self.woordlijst)
        self.verborgen_woord = ["_"] * len(self.woord)
        self.fouten = 0
        self.geraden_letters = []
        self.gok = ""
        self.spel_afbeeldingen = [f"spel_canvas_{i}.jpg" for i in range(10)]

    def laad_score(self, naam):
        if os.path.exists(self.score_pad):
            with open(self.score_pad, 'r') as f:
                for lijn in f:
                    speler, speler_score = lijn.strip().split(',')
                    if speler == naam:
                        return int(speler_score)
        return 0

    def sla_score_op(self):
        scores = {}
        if os.path.exists(self.score_pad):
            with open(self.score_pad, 'r') as f:
                for lijn in f:
                    speler, speler_score = lijn.strip().split(',')
                    scores[speler] = int(speler_score)
        scores[self.speler_naam] = self.sterren
        with open(self.score_pad, 'w') as f:
            for speler, score in scores.items():
                f.write(f"{speler},{score}\n")

class GalgjeApp:
    def __init__(self, root, status):
        self.root = root
        self.status = status
        self.alfabet_labels = {}
        self.woord_label = None
        self.label_info = None
        self.label_ster = None
        self.spel_canvas = None
        self.spel_canvas_img = None
        self.spel_entry = None
        self.welkom_canvas = None
        self.naam_entry = None
        self.info_text = []
        self.maak_venster()
        self.toon_welkom()

    def maak_venster(self):
        self.root.title("Eindopdracht - Galgje")
        self.root.resizable(0, 0)
        breedte, hoogte = 600, 600
        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        x = (scherm_breedte // 2) - (breedte // 2)
        y = (scherm_hoogte // 2) - (hoogte // 2 + 50)
        self.root.geometry(f'{breedte}x{hoogte}+{x}+{y}')
        self.root.configure(bg="gray10")
        try:
            self.root.iconbitmap(default="Galgje.ico")
        except:
            pass

    def toon_welkom(self):
        welkom_img = Image.open(os.path.join(self.status.afbeelding_pad, 'Welkom_Canvas.jpg')).resize((600, 600), Image.NEAREST)
        welkom_img = ImageTk.PhotoImage(welkom_img)
        self.welkom_canvas = Canvas(self.root, width=600, height=600, highlightthickness=0, bd=0)
        self.welkom_canvas.pack()
        self.welkom_canvas.create_image(0, 0, anchor=NW, image=welkom_img)
        self.welkom_canvas.image = welkom_img

        self.naam_entry = Entry(self.root, width=31, insertbackground="orange", background="gray15",
                                foreground="orange", font=("arial", 24, "bold"), justify="center",
                                bd=0, highlightthickness=2, highlightcolor="orange")
        self.welkom_canvas.create_window(300, 520, window=self.naam_entry)
        self.naam_entry.bind("<Return>", self.naam_instellen)
        self.naam_entry.focus_set()

    def naam_instellen(self, event):
        naam = self.naam_entry.get()
        if naam:
            self.status.speler_naam = naam
            self.status.sterren = self.status.laad_score(naam)
            self.welkom_canvas.destroy()
            self.naam_entry.destroy()
            self.start_spel()

    def start_spel(self):
        self.status.reset()
        self.spel_canvas = Canvas(self.root, width=600, height=600, highlightthickness=0, bd=0)
        self.spel_canvas.pack()

        img_path = os.path.join(self.status.afbeelding_pad, self.status.spel_afbeeldingen[0])
        afbeelding = Image.open(img_path).resize((600, 600), Image.LANCZOS)
        afbeelding = ImageTk.PhotoImage(afbeelding)
        self.spel_canvas_img = self.spel_canvas.create_image(0, 0, anchor=NW, image=afbeelding)
        self.spel_canvas.image = afbeelding

        self.label_info = Label(self.root, width=50, background="gray5", foreground="yellow",
                                text=f"Daar gaan we {self.status.speler_naam}. Raad een letter of woord.",
                                font=("arial", 11, "bold"), justify=LEFT, anchor="w")
        self.label_info.pack(side=TOP, padx=5)

        self.label_ster = Label(self.root, width=5, background="gray10", foreground="yellow",
                                 text=self.status.sterren, font=("arial", 11, "bold"), justify=LEFT, anchor="e")
        self.label_ster.pack(side=TOP, padx=5)

        self.spel_entry = Entry(self.root, width=25, insertbackground="yellow", background="gray15",
                                foreground="yellow", font=("arial", 20, "bold"), justify="center",
                                bd=0, highlightthickness=2, highlightcolor="yellow")
        self.spel_entry.bind("<Return>", self.gok_input)
        self.spel_entry.focus_set()

        self.spel_canvas.create_window(300, 90, window=self.spel_entry)
        self.spel_canvas.create_window(235, 24, window=self.label_info)
        self.spel_canvas.create_window(533, 24, window=self.label_ster)

        alfabet = list(string.ascii_uppercase)
        for i, letter in enumerate(alfabet):
            label = Label(self.spel_canvas, text=letter, width=1, height=1, font=("Arial", 12, "bold"),
                          bg="gray15", fg="yellow")
            x = 25 + (i % 26) * 22
            y = 580 + (i // 26) * 25
            self.spel_canvas.create_window(x, y, window=label)
            self.alfabet_labels[letter.lower()] = label

        self.woord_label = self.spel_canvas.create_text(300, 540, text=' '.join(self.status.verborgen_woord),
                                                        font=("Arial", 22, "bold"), fill="orange")

    def gok_input(self, event):
        gok = self.spel_entry.get().lower()
        self.spel_entry.delete(0, END)
        self.status.gok = gok

        if gok == "cheat":
            self.label_info.config(text=f"Valsspeler! Het woord is: {self.status.woord.upper()}")
            return

        if self.status.fouten >= 9 or "_" not in self.status.verborgen_woord:
            if gok == "j":
                self.spel_canvas.destroy()
                self.start_spel()
            elif gok == "n":
                quit()
            else:
                self.label_info.config(text="Typ J voor een nieuw woord. Of N om te stoppen.")
            return
        
        if gok == self.status.woord:
            self.status.verborgen_woord = list(self.status.woord)
            self.label_info.config(text=f"Correct! Het woord was: {self.status.woord.upper()}. Score + 150")
            self.status.sterren += 150
            self.status.sla_score_op()
        elif len(gok) == 1 and gok in string.ascii_lowercase:
            if gok in self.status.geraden_letters:
                self.label_info.config(text=f"De letter {gok.upper()} heb je al geprobeerd.")
            elif gok in self.status.woord:
                self.alfabet_labels[gok].config(fg="lime")
                self.status.geraden_letters.append(gok)
                for i, letter in enumerate(self.status.woord):
                    if letter == gok:
                        self.status.verborgen_woord[i] = gok
                self.label_info.config(text=f"De Letter {gok.upper()} zit inderdaad in het verborgen woord!")
                if "_" not in self.status.verborgen_woord:
                    self.label_info.config(text=f"Goed gedaan! Het woord was: {self.status.woord.upper()}. Score + 100")
                    self.status.sterren += 100
                    self.status.sla_score_op()
            else:
                self.alfabet_labels[gok].config(fg="red")
                self.status.geraden_letters.append(gok)
                self.status.fouten += 1
                self.label_info.config(text=f"De {gok.upper()} zit niet in het verborgen woord. Poging {self.status.fouten} van 9")
                self.update_afbeelding()
        else:
            self.status.fouten += 1
            self.label_info.config(text=f"{gok.upper()} is niet het antwoord. Poging {self.status.fouten} van 9")
            self.update_afbeelding()

        if self.status.fouten >= 9:
            self.label_info.config(text=f"Opgehangen! Het woord was: {self.status.woord.upper()}. Score - 150")
            if self.status.sterren >= 150:
                self.status.sterren -= 150
            else:
                self.status.sterren = 0
            self.status.sla_score_op()

        self.update_woord()
        self.label_ster.config(text=f"{self.status.sterren}")

    def update_afbeelding(self):
        fouten = min(self.status.fouten, len(self.status.spel_afbeeldingen) - 1)
        pad = os.path.join(self.status.afbeelding_pad, self.status.spel_afbeeldingen[fouten])
        afbeelding = Image.open(pad).resize((600, 600), Image.LANCZOS)
        afbeelding = ImageTk.PhotoImage(afbeelding)
        self.spel_canvas.itemconfig(self.spel_canvas_img, image=afbeelding)
        self.spel_canvas.image = afbeelding

    def update_woord(self):
        self.spel_canvas.itemconfig(self.woord_label, text=' '.join(self.status.verborgen_woord))

if __name__ == "__main__":
    woordlijst_pad = os.path.join(os.path.dirname(__file__), 'Woordlijst.txt')
    score_pad = os.path.join(os.path.dirname(__file__), 'scores.txt')
    afbeelding_pad = os.path.dirname(__file__)

    with open(woordlijst_pad) as f:
        woorden = f.read().split()

    root = Tk()
    status = SpelStatus(woorden, score_pad, afbeelding_pad)
    app = GalgjeApp(root, status)
    root.mainloop()