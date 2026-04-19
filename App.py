from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Wifi_qr_code_generator:
    def __init__(self,root):
        root.title('Wifi qr code generator')
        root.geometry('800x500')
        root.grid_columnconfigure(0,weight=1)
        root.grid_rowconfigure(0,weight=0)

        #The body of the GUI
        mainframe=ttk.Frame(root)
        mainframe.grid(column=0,row=0)
        

        #Variables and their input zone
        self.wifi_name=StringVar()
        ttk.Label(mainframe,text="Put the name of the wifi",font=1).grid(row=0,pady=10)
        wifi_name=ttk.Entry(mainframe,width=20,textvariable=self.wifi_name)
        wifi_name.grid(row=1)

        self.wifi_password=StringVar()
        ttk.Label(mainframe,text="Put the password of the wifi",font=1).grid(row=2,pady=10)
        wifi_password=ttk.Entry(mainframe,width=20,textvariable=self.wifi_password)
        wifi_password.grid(row=3)

        self.wifi_security_protocol=StringVar()
        ttk.Label(mainframe,text="Choose the security type of the wifi",font=1).grid(row=4,pady=10)
        option_1=ttk.Radiobutton(mainframe,text="WPA",value="WPA",variable=self.wifi_security_protocol).grid(row=5,pady=10)
        option_1=ttk.Radiobutton(mainframe,text="WEP",value="WEP",variable=self.wifi_security_protocol).grid(row=6,pady=10)
        option_3=ttk.Radiobutton(mainframe,text="nopass",value="nopass",variable=self.wifi_security_protocol).grid(row=7,pady=10)
        ttk.Button(mainframe,text="Generate",command=self.generate_image).grid(row=8,pady=10)

    #The function that generates the qr code and save it in your computer
    def generate_image(self):
        ssid=self.wifi_name.get()
        password=self.wifi_password.get()
        security=self.wifi_security_protocol.get()

        from wifi_qrcode_generator.generator import wifi_qrcode
        qr=wifi_qrcode(ssid,True,security,password)

        file_path=filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            qr.make_image().save(file_path)

root=Tk()
Wifi_qr_code_generator(root)
root.mainloop()