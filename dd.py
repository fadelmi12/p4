# nama file : tkinter_gridmanager v2.py

# import modul
from tkinter import *
import tkinter.messagebox

class Window1 (tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.buatKontrol()
        #list data user
        self.dataSiswa = (
            ["Fadel Muhammad Irsyad", "fadelmi12", "admin"],
            ["Beni", "beni123", "user"],
            ["Bambang Roni", "bmb123", "user2"],
            ["Deka Pramesta", "deka123", "user3"])
        self.aturKejadian()
        self.isiListbox()
        self.isiData()
        self.listboxData.focus_set()

    #bind onklick pada listbox
    def aturKejadian(self):
        self.listboxData.bind('<ButtonRelease-1>', self.onKlikLB)
        self.listboxData.bind('<KeyRelease>', self.onKlikLB)
    
    #function onclick listbox
    def onKlikLB(self, event=None):
        self.isiData()
    
    #function insert data username dan delete setiap klik
    def isiData(self):
        kode = int(self.listboxData.curselection()[0])

        # hapus data
        self.entNomor.delete(0, END)
        self.entPassword.delete(0, END)
        
        # isi data
        self.entNomor.insert(END, self.dataSiswa[kode][1])

    #perulangan untuk menampilkan data dalam listbox
    def isiListbox(self):
        for dat in range(len(self.dataSiswa)):
            self.listboxData.insert(END, self.dataSiswa[dat][0])
 
        self.listboxData.selection_set(0)

    #function untuk login dan pengaturan layout
    def buatKontrol(self):
        def login():
            #menangkap array dari list menggunakan indeks
            indeks2 = self.listboxData.curselection()
            kode2 = int(indeks2[0])
            u = (self.dataSiswa[kode2][1])
            p = (self.dataSiswa[kode2][2])
            u1 = str(self.entNomor.get())
            p2 = str(self.entPassword.get())
            #fungsi login untuk mencocokan username dan password
            if (u == u1 and p == p2):
                self.newWindow = Toplevel(self.master)
                self.app = Window2(self.newWindow)
            elif(u != u1):
                tkinter.messagebox.showerror("Akun", "Akun belum terdaftar")    
            else:
                tkinter.messagebox.showerror("Password", "Password Salah")
        
        def show_hide_psd():
            if(check_var.get()):
                self.entPassword.config(show="")
            else:
                self.entPassword.config(show="*")  
         # frame_kanan
        fr_atas = Frame(self, bd=5)
        fr_atas.pack()

        # fr_atas_atas
        fr_katas = Frame(fr_atas)
        fr_katas.pack(side=TOP)
        # frame_kiri
        fr_bawah = Frame(self, bd=5)
        fr_bawah.pack()
        
        self.lbl = tkinter.Label(fr_bawah, 
                text="Pilih User : ",
                font="Verdana 8 bold", 
                height="2")
        self.lbl.grid(row=0, column=0, sticky=W)
        self.listboxData = Listbox(fr_bawah, 
                width=30,
                height = 5,
                selectmode="SINGLE")
 
        self.listboxData.grid(row=1, column=0)
        
        # data Nomor
        Label(fr_katas, text='Username').grid(
            row=0, column=0, sticky=W)
        self.entNomor = Entry(fr_katas)
        self.entNomor.grid(row=0, column=1)
        check_var = IntVar()
        check_show_psw = Checkbutton(fr_katas, text = "Lihat Password", 
                variable = check_var,
                onvalue = 1, 
                offvalue = 0, 
                height=2, 
                command = show_hide_psd)
        check_show_psw.grid(row=2 ,column=0, columnspan=2, sticky=W)
        # data Nama
        Label(fr_katas, text='Password').grid(
            row=1, column=0, sticky=W)
        self.entPassword = Entry(fr_katas, show= "*")
        self.entPassword.grid(row=1, column=1)

        Button(fr_katas, text="Login", command=login).grid(
            row=2, column=1, sticky=E)
class Window2(tkinter.Frame):
    # membuat konstruktor DemoFrame

    def __init__(self, master=None):
        # memanggil kontruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.buttonclick()
    
    def buttonclick(self):
        def hitung():
            #kondisi untuk pria/wanita
            if (i.get()==1):
                lbl3 = int(tinggibdn.get()) #mengubah input menjadi int
                hslwanita = (lbl3-100) -(lbl3-100)*0.1 #rumus berat badan ideal wanita
                tkinter.messagebox.showinfo(
                    "Hasil", "Berat Badan Ideal Anda adalah %i Kg" %(hslwanita)) #menampilkan hasil
            elif (i.get()==2):
                lbl4 = int(tinggibdn.get()) #mengubah input menjadi int
                hslwanita = (lbl4-100) -(lbl4-100)*0.15 #rumus berat badan ideal wanita
                tkinter.messagebox.showinfo(
                    "Hasil", "Berat Badan Ideal Anda adalah %i Kg" %(hslwanita)) #menampilkan hasil
            else:
                tkinter.messagebox.showwarning("Warning", "Format Pengisian Salah")

    #label pertama

        lbl = tkinter.Label(self,
            text = "Pilih Jenis Kelamin ",
            fg = "black",
            height = "2",
            font = "Verdana 8 bold").grid(row=0, column=0, sticky=W)
    #entry pertama
        i = IntVar()
        r1 = tkinter.Radiobutton(self, 
            text="Pria", 
            value=1, 
            variable=i,
            font= "Verdana 8 bold").grid(row=0, column=1)
        r2 = tkinter.Radiobutton(self, 
            text="Wanita", 
            value=2, 
            variable=i,
            font= "Verdana 8 bold").grid(row=0,column=2)
    #label kedua
        lbl2 = tkinter.Label(self,
            text = "Masukkan Tinggi Badan (cm) ",
            fg = "black",
            font = "Verdana 8 bold").grid(row=1, column=0)
    #entry kedua
        tinggibdn = tkinter.Entry(self, 
            font = "Verdana 8 bold",
            width = 15,
            bd=3,
            selectbackground = "red",
            selectforeground = "blue",)
        tinggibdn.grid(row=1, column=1, columnspan=2, sticky=W)
        tinggibdn.select_clear()
    #button memanggil method buttonclick
        btn = tkinter.Button(self, 
            command=hitung,
            text= "Hitung",
            font = "Verdana 8 bold",
            activeforeground = "blue",
            activebackground = "red",
            height = "2",
            bd = 3).grid(row=2, column=0, columnspan=3)
def main():
    # membuat kelas demo frame
    app = Window1()
    app.master.title("P4")
    app.mainloop()

if __name__ == "__main__":
    main()