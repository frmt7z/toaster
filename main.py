class Toaster:
    def __init__(self, slots=2, color="rot"):
        self.slots = slots
        self.color = color
        self.toast_laenge = 0
        self.toast_zustand = "nicht getoastet"
        self.toast_anzahl = 0

    def zeit_einstellen(self):
        if toast_laenge > 60 or toast_laenge < self.toast_laenge:
            print("Der Toaster kann nur in einer Zeit von 1 bis 60 Sekunden eingestellt werden!")
        else:
            toaster.toast()


    def toast(self):
        if toast_anzahl > self.slots:
            print("Fehler: Zu viele Toasts für die verfügbaren Schlitze.")
            return
        else:
            self.toast_anzahl = toast_anzahl
            self.slots = self.slots - toast_anzahl
            if toast_anzahl == 1:
                print(f"{toast_anzahl} Toast wird für {toast_laenge} Sekunden getoastet!")
            else:
                print(f"{toast_anzahl} Toasts werden für {toast_laenge} Sekunden getoastet!")
            toaster.toast_auswerfen()



    def toast_auswerfen(self):
        if toast_laenge >= 45:
            self.toast_zustand = "verbrannt"
        if 30 <= toast_laenge < 45:
            self.toast_zustand = "gut getoastet"
        if 30 > toast_laenge >= 15:
            self.toast_zustand = "leicht getoastet"
        if toast_laenge < 15:
            self.toast_zustand = "kaum getoastet"

        self.slots = 2
        self.toast_anzahl = 0
        print(f"Toast wurde ausgeworfen und ist {self.toast_zustand}, der Toaster ist immer noch {self.color}!\nDer Toaster hat wieder {self.slots} freie Schächte.")


toast_anzahl = int(input("Wie viele Toasts sollen getoastet werden?"))
toast_laenge = int(input("Wie lange sollen die Toasts getoastet werden in Sekunden?"))


toaster = Toaster()
toaster.zeit_einstellen()
