from tkinter import *
from tkinter import ttk
import tkinter .messagebox as msg

root = Tk()

# Classe daAplicação


class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.form_frame1()
        self.buttons_form_frame_1()
        self.lista_frame2()
        root.mainloop()

# Função da tela principal
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="grey")
        self.root.geometry("1024x700")
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)
# Função dos Frames da Tela Principal

    def frames_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#B0C4DE",
                            highlightbackground="#4682B4", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.40)
        self.frame2 = Frame(self.root, bd=4, bg="#B0C4DE",
                            highlightbackground="#4682B4", highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.44, relwidth=0.96, relheight=0.54)

# Funções dos Labels e Imputs Frame_1
    def form_frame1(self):
        # Label e imput da matricula
        # Label
        self.lb_matricula = Label(self.frame1, text="Matricula ", bg="#B0C4DE")
        self.lb_matricula.place(relx=0.02, rely=0.04)
        # Innput
        self.en_matricula = Entry(self.frame1)
        self.en_matricula.place(relx=0.02, rely=0.1,
                                relwidth=0.1, relheight=0.1)
        # Label e imput Nome
        # Label
        self.lb_name = Label(self.frame1, text="Nome completo ", bg="#B0C4DE")
        self.lb_name.place(relx=0.02, rely=0.24)
        # Innput
        self.en_name = Entry(self.frame1)
        self.en_name.place(relx=0.02, rely=0.30, relwidth=0.96, relheight=0.1)
        # Label e imput E-Mail
        # Label
        self.lb_email = Label(self.frame1, text="E-Mail", bg="#B0C4DE")
        self.lb_email.place(relx=0.02, rely=0.44)
        # Innput
        self.en_email = Entry(self.frame1)
        self.en_email.place(relx=0.02, rely=0.50, relwidth=0.48, relheight=0.1)
        # Label e imput Telefone
        # Label
        self.lb_phone = Label(self.frame1, text="Telefone", bg="#B0C4DE")
        self.lb_phone.place(relx=0.52, rely=0.44)
        # Innput
        self.en_phone = Entry(self.frame1)
        self.en_phone.place(relx=0.52, rely=0.5, relwidth=0.46, relheight=0.1)
        # Label e imput Montadora
        # Label
        self.lb_montadora = Label(self.frame1, text="Montadora", bg="#B0C4DE")
        self.lb_montadora.place(relx=0.02, rely=0.64)
        # Innput
        self.en_montadora = Entry(self.frame1)
        self.en_montadora.place(relx=0.02, rely=0.70,
                                relwidth=0.23, relheight=0.1)
        # Label e imput Modelo
        # Label
        self.lb_modelo = Label(self.frame1, text="Modelo", bg="#B0C4DE")
        self.lb_modelo.place(relx=0.26, rely=0.64)
        # Innput
        self.en_modelo = Entry(self.frame1)
        self.en_modelo.place(relx=0.26, rely=0.70,
                             relwidth=0.24, relheight=0.1)
        # Label e imput Montadora
        # Label
        self.lb_ano = Label(self.frame1, text="Ano", bg="#B0C4DE")
        self.lb_ano.place(relx=0.52, rely=0.64)
        # Innput
        self.en_ano = Entry(self.frame1)
        self.en_ano.place(relx=0.52, rely=0.70, relwidth=0.23, relheight=0.1)
        # Label e imput Modelo
        # Label
        self.lb_placa = Label(self.frame1, text="Placa", bg="#B0C4DE")
        self.lb_placa.place(relx=0.76, rely=0.64)
        # Innput
        self.en_placa = Entry(self.frame1)
        self.en_placa.place(relx=0.76, rely=0.70, relwidth=0.22, relheight=0.1)

# Botões do Frame_1,  formulario
    def buttons_form_frame_1(self):
        # Função Botõoes

        def salvar() -> NONE:
            msg.showinfo("Novo Cadastro",
                         "Cadastro Realizado com sucesso com sucesso")

        def excluir() -> NONE:
            msg.showinfo("Excluir Cadastro",
                         "Cadastro Ecluido com sucesso com sucesso")
        # Botão limpar
        self.bt_limpar = Button(
            self.frame1, text="Limpar", font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.14, rely=0.1, relwidth=0.1, relheight=0.1)
        # Botão Buscar
        self.bt_buscar = Button(
            self.frame1, text="Buscar", font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.1)
        # Botão Novo
        self.bt_novo = Button(self.frame1, text="Novo",
                              command=salvar, font=('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.66, rely=0.1, relwidth=0.1, relheight=0.1)
        # Botão Editar
        self.bt_edit = Button(self.frame1, text="Editar",
                              font=('verdana', 8, 'bold'))
        self.bt_edit.place(relx=0.77, rely=0.1, relwidth=0.1, relheight=0.1)
        # Botão Apagar
        self.bt_delet = Button(self.frame1, text="Excluir",
                               command=excluir, font=('verdana', 8, 'bold'))
        self.bt_delet.place(relx=0.88, rely=0.1, relwidth=0.1, relheight=0.1)

# Lista cadastrados frame 2
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Matricula")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Modelo")
        self.listaCli.heading("#4", text="Placa")
        self.listaCli.heading("#5", text="Telefone")
        # Definindo tamanho das colunas
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=100)
        self.listaCli.column('#4', width=100)
        self.listaCli.column('#5', width=50)
        # Posicionando a tabela
        self.listaCli.place(relx=0.02, rely=0.1, relwidth=0.94, relheight=0.85)

        self.scrollList = Scrollbar(self.frame2, orient="vertical")
        self.listaCli.configure(yscrollcommand=self.scrollList.set)
        self.scrollList.place(relx=0.96, rely=0.1,
                              relwidth=0.02, relheight=0.85)


Aplication()
