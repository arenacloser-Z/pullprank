import subprocess
#proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
#stdout, stderr = proc.communicate('dir c:\\')
#stdout

import time
import os
#x = os.system("ipconfig")

proc = subprocess.Popen('ipconfig /all', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = proc.communicate()
proc2 = subprocess.Popen('curl https://ipinfo.io/ip', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out2, err2 = proc2.communicate()
proc3 = subprocess.Popen('systeminfo', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out3, err3 = proc3.communicate()
proc4 = subprocess.Popen('curl https://ipinfo.io', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out4, err4 = proc4.communicate()
#print(out.decode())
#os._exit(0)

def writeip(directory):
    f = open(directory, "a")
    f.write("SYSTEM INFO:\n\n\n")
    f.write(out3.decode())
    f.write("IPCONFIG:\n\n\n")
    f.write(out.decode())
    f.write("PUBLIC IP INFORMATION:\n\n")
    f.write(out2.decode())
    f.write("\n")
    f.write(out4.decode())
    f.close()

writeip("iplog.txt")

#x = input()
#os.system("pause")
#time.sleep(0.5)
#os._exit(0)
proc.kill()
proc2.kill()
proc3.kill()
proc4.kill()



from tkinter import *
from tkinter import messagebox
import time
import random
from tkinter import font

msgs = ["System Exception: C:/ BAT -c -g xlm", "Critical system eror", "Rename system file not supported", "System Error: PATHU\ c- maindir", "Critical system error: CMDH is not defined at a\d\sim", "Uknown error occured. #151521512 Restart your computer", "Critical system Error #12512512 Cannot copy CMDE.EXE from system32/bat u- -o"]
# random stuff

root = Tk()
root.attributes('-fullscreen', True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.withdraw()

#root.option_add('*font', 'Helvetica -12')
def throwawayroot():
    global toplevel
    toplevel = Toplevel(root)
    toplevel.config(bg="white")
    toplevel.attributes("-topmost", 1)
    #toplevel.attributes("-toolwindow", True)
    toplevel.title("Error")
    x = random.randint(0, int(width)-100)
    y = random.randint(0, int(height)-100)
    toplevel.geometry(f"300x100+{x}+{y}")
    toplevel.resizable(False, False)
    
    l1=Label(toplevel, image="::tk::icons::error", bg="white")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 10), sticky="e")
    l2=Label(toplevel,text=random.choice(msgs), font=("Arial", 8), bg="white")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
    b2=Button(toplevel,text="OK",command=toplevel.destroy,width = 10, bg="white")
    b2.grid(row=1, column=3, padx=(2, 35), sticky="e")
    
    Tk.update(toplevel)

for i in range(0, 220):
    throwawayroot()
    if i/10 == int(i/10):
        print("adas")
        toplevel.bell()
    #time.sleep(0.01)

time.sleep(8)
os._exit(1)


