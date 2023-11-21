import customtkinter as ck
from tkinter import *
from tkinter import messagebox as msg
from PIL import Image
import os
import webbrowser
import sqlite3


log = ck.CTk()
log.geometry('1000x500+350+250')
log.title('DKK Login')
log.resizable(False, False)
log.config(background='#fff')
file_path = os.path.dirname(os.path.relpath(__file__))


 # ------------------------------ Link to web pages. ------------------------------
def facebook_page():
  webbrowser.open_new('https://www.facebook.com')
def tiwitter_page():
  webbrowser.open_new('https://www.teitter.com')
def instagram_page():
  webbrowser.open_new('https://www.instagram.com')
def linkedin_page():
  webbrowser.open_new('https://www.linkedin.com')
def youtube_page():
   webbrowser.open_new('https://www.youtube.com')
def site_page():
  webbrowser.open_new('https://www.dankankasa.com')


def change():
  login_frame.pack_forget()
  change_frame.pack(padx=5, pady=5)

def exists():
  change_frame.pack_forget()
  login_frame.pack(padx=5, pady=5)
  connection()

def connection():
  connect = sqlite3.connect('Data.db')
  conn = connect.cursor()
  conn.execute("CREATE TABLE IF NOT EXISTS Logs(Id INTEGER PRIMARY KEY, Agent VARCHAR(5) NOT NULL, Password VARCHAR(8) NOT NULL, Conferm VARCHAR(8) NOT NULL)")
  connect.commit()
  connect.close()

def insert():
  connect = sqlite3.connect('Data.db')
  conn = connect.cursor()
  new_user = new_user_entry.get()
  new_password = new_pass_entry.get()
  new_conferm = pass_conf_entry.get()
  
  if new_user == '' and new_password == '' and new_conferm == '':
    msg.showwarning('Warning', 'Please type your details in the recoaerd fields.')
  
  elif new_password != new_conferm:
    msg.showerror('Error', 'Please check both your password and conferm password similarity.')

  elif new_user:
    conn.execute("SELECT COUNT(*) FROM Logs WHERE Agent = ?", (new_user,))
    in_user = conn.fetchone()
    if in_user[0] > 0:
      msg.showerror('Error',f'The agent {new_user} already exists! Please try another one.')
      new_user_entry.delete(0, END)
      new_pass_entry.delete(0, END)
      pass_conf_entry.delete(0, END)
      return
    else:
      if len(new_password) > 6 and len(new_conferm) > 6:
        msg.showerror("Error", "Password length should not exceed 6 characters")
      elif len(new_password) < 6 and len(new_conferm) < 6:
        msg.showerror("Error", "Password length should not be less than 6 characters")
      else:
        conn.execute("INSERT INTO Logs(Agent, Password, Conferm) VALUES (?,?,?)", (new_user.upper(), new_password, new_conferm))
        connect.commit()
        msg.showinfo('Success', 'Welcome, Your details have been registed successfully.')
        new_user_entry.delete(0, END)
        new_pass_entry.delete(0, END)
        pass_conf_entry.delete(0, END)
        connect.close()

def check_uppercase(user):
    # Check if there is at least one uppercase character in the username.
    # Check if the first letter is uppercase.
    return any(char.isupper() for char in user)

def check():
  user = user_entry.get()
  password = pass_entry.get()
  # ------------------------------ Check if username or password fields are empty
  if not user or not password:
    msg.showwarning('Warning', 'Please type your details into the required fields.')
    return # Exit the function if fields are empty
  
  # ------------------------------ Query the database to check if the username and password match
  connect = sqlite3.connect('Data.db')
  conn = connect.cursor()
  conn.execute("SELECT * FROM Logs WHERE Agent = ? AND Password = ?", (user, password))
  in_user = conn.fetchone()

  if not check_uppercase(user):
    msg.showerror("Error", "The Agent first letter must be uppercase character")
  else:
    if in_user:
      msg.showinfo('Success', f'Welcome {user} you have logged in successfully.')
      user_entry.delete(0, END)
      pass_entry.delete(0, END)
    else:
      msg.showerror("Error", "Invalid username and password, please be registed and try again.")
      user_entry.delete(0, END)
      pass_entry.delete(0, END)

def show(): # Cacher tout les caractaire afficher.
  show_hide_button = ck.CTkButton(login_frame, width=30, corner_radius=8, text='', image=hide_image, command=hide, bg_color='white', fg_color='white', hover_color='#fff')
  show_hide_button.place(x=900, y=205)
  pass_entry.configure(show='') # Affichage des caractaire.

def hide(): # Afficher tout les caractaires cacher.
  show_hide_button = ck.CTkButton(login_frame, width=30, corner_radius=8, text='', image=show_image, command=show, bg_color='white', fg_color='white', hover_color='#fff')
  show_hide_button.place(x=900, y=205)
  pass_entry.configure(show='⏣') # Remetre en symbole.


# ---------------------------------------- The Main Frames.
login_frame = ck.CTkFrame(log, width=990, height=488, bg_color='#fff', fg_color='#fff')
change_frame = ck.CTkFrame(log, width=990, height=488, bg_color='#fff', fg_color='#fff')


# ---------------------------------------- The Login Window (User credantials).

lock_img = ck.CTkImage(Image.open(file_path + 'Images/login.png'), size=(450, 470))
lock_lab = ck.CTkLabel(login_frame, image = lock_img, bg_color='#fff', text='').place(x=30, y=10)

show_image = ck.CTkImage(Image.open(file_path + "Icons/eye3.png"), size=(25, 25))
hide_image = ck.CTkImage(Image.open(file_path + "Icons/privacy3.png"), size=(25, 25))


# ------------------------------ Importation of the images and icons.
facebook_img = ck.CTkImage(Image.open(file_path + 'Icons/facebook.png'), size=(35, 35))
x_img = ck.CTkImage(Image.open(file_path + 'Icons/twitter.png'), size=(35, 35))
insta_img = ck.CTkImage(Image.open(file_path + 'Icons/instagram.png'), size=(35, 35))
link_img = ck.CTkImage(Image.open(file_path + 'Icons/linkedin.png'), size=(35, 35))
you_img = ck.CTkImage(Image.open(file_path + 'Icons/youtube.png'), size=(35, 35))
inter_img = ck.CTkImage(Image.open(file_path + 'Icons/internet.png'), size=(35, 35))

# ------------------------------ Les button pour les logo des reseaux socieaux.
face_lab = ck.CTkButton(log, image = facebook_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:facebook_page()).place(x=552, y=430)
x_lab = ck.CTkButton(log, image = x_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:tiwitter_page()).place(x=620, y=430)
insta_lab = ck.CTkButton(log, image = insta_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:instagram_page()).place(x=692, y=430)
link_lab = ck.CTkButton(log, image = link_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:linkedin_page()).place(x=763, y=430)
you_lab = ck.CTkButton(log, image = you_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:youtube_page()).place(x=833, y=430)
inter_lab = ck.CTkButton(log, image = inter_img, text='', width=50,fg_color='#fff', bg_color='#fff', hover_color='#f7f0fa', command=lambda:site_page()).place(x=903, y=430)

# ------------------------------ Le titre de la page Login.
welcome_label = ck.CTkLabel(login_frame, text='  Ets Chamhasi50 S.A  ', text_color='#115d6c', font=('Helvetica', 35, 'bold', 'underline'), bg_color='#fff').place(x=585, y=20)
slogan_label = ck.CTkLabel(login_frame, text='Tout ce que tu fais, tu le fais pour toi meme !', text_color='black', font=('Helvetica', 13), bg_color='#fff').place(x=620, y=60)

# ------------------------------ Les entry de la page Login.
user_entry = ck.CTkEntry(login_frame, font=('Ariel', 17, 'bold'), text_color='gray', width=400, height=40, placeholder_text='Username', border_width=1, border_color='#115d6c', bg_color='#fff', fg_color='#fff')

pass_entry = ck.CTkEntry(login_frame, font=('Ariel', 17, 'bold'), text_color='gray', show='⏣', width=400, height=40, placeholder_text='Password', border_width=1, border_color='#115d6c', bg_color='#fff', fg_color='#fff')

user_entry.place(x=550, y=150)
pass_entry.place(x=550, y=200)

# ------------------------------ Les button pour le login page.
login_button = ck.CTkButton(login_frame, text='Login', text_color='#e0f2f1', font=('Ariel', 20, 'bold'), width=400, height=50, bg_color='#fff', fg_color='#115d6c',hover_color='#115d6c', command=check).place(x=550, y=250)

logout_button = ck.CTkButton(login_frame, text='Change Password', text_color='#e0f2f1', font=('Ariel', 20, 'bold'), width=400, height=50, bg_color='#fff', fg_color='#115d6c', hover_color='#115d6c', command= change).place(x=550, y=310)

show_hide_button = ck.CTkButton(login_frame, width=30, corner_radius=8, text='', image=show_image, bg_color='#fff', fg_color='#fff', hover_color='#fff',command=show)
show_hide_button.place(x=900, y=205)

  
# ------------------------------ Change Frame Window.
lock_img = ck.CTkImage(Image.open(file_path + 'Images/log.png'), size=(450, 470))
lock_lab = ck.CTkLabel(change_frame, image = lock_img, bg_color='#fff', text='').place(x=30, y=10)

welcome_label = ck.CTkLabel(change_frame, text='  Ets Chamhasi50 S.A  ', text_color='#854ddc', font=('Helvetica', 35, 'bold', 'underline'), bg_color='#fff').place(x=585, y=20)
slogan_label = ck.CTkLabel(change_frame, text='Tout ce que tu fais, tu le fais pour toi meme !', text_color='black', font=('Helvetica', 13), bg_color='#fff').place(x=620, y=60)

new_user_entry = ck.CTkEntry(change_frame, font=('Ariel', 17, 'bold'), width=400, height=40, border_width=1, border_color='#854ddc', text_color='gray', placeholder_text='Username', bg_color='#fff', fg_color='#fff')

new_pass_entry = ck.CTkEntry(change_frame, font=('Ariel', 17, 'bold'), show='⏣', width=400, height=40, border_width=1, border_color='#854ddc',text_color='gray', placeholder_text='New Password', bg_color='#fff', fg_color='#fff')

pass_conf_entry = ck.CTkEntry(change_frame, font=('Ariel', 17, 'bold'), show='⏣', width=400, height=40, border_width=1, border_color='#854ddc',text_color='gray', placeholder_text='Conferm Password', bg_color='#fff', fg_color='#fff')

new_user_entry.place(x=550, y=150)
new_pass_entry.place(x=550, y=200)
pass_conf_entry.place(x=550, y=250)

# ------------------------------ Le button pour la connexion.
change_button = ck.CTkButton(change_frame, text='Change', text_color='#f7f0fa', font=('Ariel', 20, 'bold'), width=400, height=50, bg_color='#fff', fg_color='#854ddc',hover_color='#854ddc',command=insert).place(x=550, y=310)

have_account = ck.CTkButton(change_frame, text="I have an account", text_color='#854ddc', font=('Helvetica', 15, 'underline'), fg_color='#fff', bg_color='#fff', hover_color='#fff', command=exists).place(x=630, y=375)

login_frame.pack(padx=5, pady=5)
change_frame.pack(padx=5, pady=5)


connection()
log.mainloop()
