from tkinter import *
import pandas as pd
import time

from tkinter import messagebox
import instaloader

bot = instaloader.Instaloader()
ws = Tk()
ws.title('Bot instagram')
ws.geometry('200x200')


def lista():
    usuario = user_Tf.get()
    senha = pass_Tf.get()
    id = iden_Tf.get()
    bot.login(usuario, senha)
    profile = instaloader.Profile.from_username(bot.context, id)
    follow_list = []
    bio_list = []
    count = 0


    for followee in profile.get_followers():
        time.sleep(10)
        follow_list.append(followee.username)
        bio_list.append(followee.biography)
        print(follow_list[count])
        print(bio_list)
        df = pd.DataFrame.from_dict({'Usuarios': follow_list, 'Bio': bio_list})
        df.to_excel('clientes.xlsx', header=True, index=False)
        count = count + 1
        time.sleep(10)

    messagebox.showinfo('Sucesso', 'excel "clientes" gerado na pasta "bot_tess"')
    ws.destroy()

Label(ws, text="Usuário:").pack()

user_Tf = Entry(ws)
user_Tf.pack()

Label(ws, text="Senha:").pack()
pass_Tf = Entry(ws)
pass_Tf.pack()

Label(ws, text="ID:").pack()
iden_Tf = Entry(ws)
iden_Tf.pack()

Button(ws, text="Gerar lista", command=lista).pack()

ws.mainloop()