from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()

login = ('Gabriela', '123456')
db = mysql.connector.connect(host='localhost', user=f'root', passwd=f'sca82812079', database='biblioteca')

if db.is_connected():
  db_info = db.get_server_info()
  print(f'Conectado ao servidor mySQL: {db_info}')
cursor = db.cursor()

def executarSQL(comando):
  cursor.execute(f"{comando}")
  result = cursor.fetchall()
  db.commit()
  return result

#[('123.456.789-12', 'Miguel', 'Johnson', '(12)99876-5432', datetime.date(1999, 2, 28), 'M'), ('258.369.147-96', 'Laura', 'Taylor', '(67)99812-4576', datetime.date(2010, 12, 25), 'F'), ('429.736.916-85', 'Scarlett', 'Rodrigues', '(11)94816-7642', datetime.date(1986, 6, 19), 'F'), ('456.789.123-78', 'Helena', 'Cooper', '(11)91234-7896', datetime.date(2000, 9, 1), 'F'), ('515.564.856-74', 'Dylan', 'Silva', '(67)97458-1212', datetime.date(1998, 2, 15), 'M'), ('645.453.872-64', 'James', 'Santos', '(15)97346-9164', datetime.date(2015, 9, 21), 'M'), ('717.491.728-81', 'Michael', 'Oliveira', '(77)97614-4985', datetime.date(2010, 9, 10), 'M'), ('789.123.456-65', 'Arthur', 'Donalds', '(89)97418-8523', datetime.date(1984, 7, 20), 'M'), ('849.874.554-12', 'Madelyn', 'Pereira', '(45)95465-1788', datetime.date(1950, 12, 15), 'F'), ('852.741.963-45', 'Alice', 'Miller', '(45)98596-7423', datetime.date(1980, 11, 30), 'F')]

#Opcoes da janela e dimensionamento
root.title('Biblioteca 98')
root['bg'] = '#f0f0f0' #background
root['fill'] = None
root.geometry('854x680')
root.resizable(False, False) #False nos valores anula o resize da janela
#root.state('zoomed') #Ja abre automaticamente max (iconic para minimizada)
root.iconbitmap('Python/Banco_de_dados/Biblioteca/Imgs/Library_icon.ico') # Icone da janela, mas nao na barra de tarefas


#Essas defs estao horriveis, depois tem que ir colocando cada uma em sua devida classe... Trabalho torto isso aqui, meeu deus
def entrarLivro():
  frame_livro.pack()
  frame_cliente.forget()
  frame_relatorio.forget()
  frame_cadastro.forget()
  frame_cadastro_emprestimo.forget()
def entrarCliente():
  frame_livro.forget()
  frame_cliente.pack()
  frame_relatorio.forget()
  frame_cadastro.forget()
  frame_cadastro_livro.forget()
  frame_cadastro_emprestimo.forget()
def entrarRelatorio():
  frame_livro.forget()
  frame_cliente.forget()
  frame_relatorio.pack()
  frame_cadastro_livro.forget()
  frame_cadastro.forget()
  frame_cadastro_emprestimo.forget()
def mostrarCadastro():
  frame_cadastro.pack()
def fecharCadastro():
  frame_cadastro.forget()
def mostrarCadastroLivro():
  frame_cadastro_livro.pack()
def fecharCadastroLivro():
  frame_cadastro_livro.forget()
def mostrarCadastroEmprestimo():
  frame_cadastro_emprestimo.pack()
def fecharCadastroEmprestimo():
  frame_cadastro_emprestimo.forget()

class LoginPerfil(Frame):
  def __init__(self, parent):
    super().__init__()

    def entrarSistema():
      frame_menu.pack()
      frame_livro.forget()
      frame_login.forget()

    def VerifyLogin():
      self.usuario = self.entry_usuario.get()
      self.senha = self.entry_senha.get()
      if self.usuario == login[0] and self.senha == login[1]: 
        self.label_login = Label(frame_login, text=f'Seja bem vindo(a), {self.usuario}')
        self.label_login.grid(row=4, columnspan=2)
        entrarSistema()
      else:
        self.label_login = Label(frame_login, text='Senha ou login invalidos')
        self.label_login.grid(row=5, columnspan=2)

    #Labels
    Label(self, text='Livraria 98', font=('Arial', 42)).grid(row=0, columnspan=2, pady=(30,30))
    global img
    img = PhotoImage(file= 'Python/Banco_de_dados/Biblioteca/Imgs/Library_icon.png')
    self.label_logo = Label(self, image=img)
    self.label_logo.grid(row=1, columnspan=2, pady=(0,35))

    self.label_usuario = Label(self, 
      text='Nome:',
      font='Arial 14', # Recebe bold, italic, tipo de fonte, tamanho e etc
      anchor=W
      )
    self.label_usuario.grid(row=2, column=0)

    self.label_senha = Label(self, 
      text='Senha:',
      font='Arial 14', # Recebe bold, italic, tipo de fonte, tamanho e etc
      anchor=W
      )
    self.label_senha.grid(row=3, column=0)

    #Entrys
    self.entry_usuario = Entry(self, text='Usuario')
    self.entry_usuario.grid(row=2, column=1)
    self.entry_senha = Entry(self, text='Senha', show='*')
    self.entry_senha.grid(row=3, column=1) 
    #Cuidado com .grid ou .place ou .pack direto na variavel, ela buga o role do GET

    #Buttons
    Button(self, text='Logar', command=VerifyLogin).grid(row=4, columnspan=2)

class Menu(Frame):
  def __init__(self, parent):
    super().__init__()

    self['borderwidth'] = '1'
    self['relief'] = 'solid'
    self['padx'] = '80'

    #Img(icone)
    global img2
    img2 = PhotoImage(file= 'Python/Banco_de_dados/Biblioteca/Imgs/biblio40.png')
    self.logo = Label(self, image=img2)
    self.logo.grid(row=0, column=0, padx=10, pady=(1,4))

    #Labels
    self.title = Label(self, text='Biblioteca 98', font=20)
    
    #BTNS
    self.btn_livro = Button(self, text='Livros', font=20, padx=10, command=entrarLivro)
    self.btn_clientes = Button(self, text='Clientes', font=20, padx=10, command=entrarCliente)
    self.btn_relatorio = Button(self, text='Emprestimos', font=20, padx=10, command=entrarRelatorio)

    #Grids
    self.title.grid(row=0, column=1, padx=(0,200))
    self.btn_livro.grid(row=0, column=2, padx=10)
    self.btn_clientes.grid(row=0, column=3, padx=10)
    self.btn_relatorio.grid(row=0, column=4, padx=10)

class MenuLivro(Frame):
  
  def voltarLista(self):
    count = 0
    for valor in self.lista.get_children():
      self.lista.delete(valor)
    for i in executarSQL('select livro.titulo, autor.nome, livro.ano, genero.tipo, livro.isbn from livro inner join autor on livro.fk_autor = autor.id_autor inner join genero on livro.fk_genero = genero.id_genero'): #meeu deus
      self.lista.insert(parent='', index='end', iid=count, values=(i[0], i[1], i[2], i[3], i[4]))
      count += 1
  
  def __init__(self, parent):
    super().__init__()

    self.title = Label(self, text='Livros', font=('Arial', 25), pady=10).pack()
    self.lista = ttk.Treeview(self)
    self.lista['columns'] = ('Titulo', 'Autor', 'Ano', 'Genero', 'ISBN')

    self.lista.column('#0', anchor=W, width=0)
    self.lista.column('Titulo', anchor=W, width=240)
    self.lista.column('Autor', anchor=W, width=150)
    self.lista.column('Ano', anchor=W, width=90)
    self.lista.column('Genero', anchor=W, width=90)
    self.lista.column('ISBN', anchor=W, width=110)

    self.lista.heading('Titulo', text='Titulo', anchor=W)
    self.lista.heading('Autor', text='Autor', anchor=W)
    self.lista.heading('Ano', text='Ano', anchor=W)
    self.lista.heading('Genero', text='Genero', anchor=W)
    self.lista.heading('ISBN', text='ISBN', anchor=W)
    
    self.voltarLista()

    def pesquisaLista():
      self.getPesquisa = self.pesquisa.get()
      print(self.getPesquisa)
      #Limpar a lista..
      for valor in self.lista.get_children():
        self.lista.delete(valor)
      #Gerar lista com filtro
      for i in executarSQL(f'select livro.titulo, autor.nome, livro.ano, genero.tipo, livro.isbn from livro inner join autor on livro.fk_autor = autor.id_autor inner join genero on livro.fk_genero = genero.id_genero where livro.titulo = "{self.getPesquisa}"'): #meeu deus
        self.lista.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3], i[4]))

    self.lista.pack(pady=(10,0))
    self.bottomFrame = Frame(self)
    self.bottomFrame.pack(pady=(8, 0), anchor=W)

    self.pesquisaName = Label(self.bottomFrame, text='Pesquisar: ')
    self.pesquisa = Entry(self.bottomFrame)
    self.botaoPesquisa = Button(self.bottomFrame, text='OK', command=pesquisaLista)
    self.botaoVoltar = Button(self.bottomFrame, text='Atualizar', command=self.voltarLista)
    self.botaoCadastrarCliente = Button(self.bottomFrame, text='Cadastrar Livro', command=mostrarCadastroLivro)


    self.pesquisaName.grid(row=0, column=0)
    self.pesquisa.grid(row=0, column=1)
    self.botaoPesquisa.grid(row=0, column=2, padx=(2,0))
    self.botaoVoltar.grid(row=0, column=3, padx=(5,0))
    self.botaoCadastrarCliente.grid(row=0, column=4, padx=(320, 0))

class MenuCliente(Frame):
  
  def voltarLista(self):
    count = 0
    for valor in self.lista.get_children():
      self.lista.delete(valor)
    for i in executarSQL('select * from cliente'): #meeu deus
      self.lista.insert(parent='', index='end', iid=count, values=(i[1], i[2], i[4], i[5], i[3], i[0]))
      count += 1
  
  def __init__(self, parent):
    super().__init__()

    self.title = Label(self, text='Clientes', font=('Arial', 25), pady=10).pack()
    self.lista = ttk.Treeview(self)
    self.lista['columns'] = ('Nome', 'Sobrenome', 'Idade', 'Sexo', 'Telefone', 'CPF')

    self.lista.column('#0', anchor=W, width=0)
    self.lista.column('Nome', anchor=W, width=150)
    self.lista.column('Sobrenome', anchor=W, width=150)
    self.lista.column('Idade', anchor=W, width=90)
    self.lista.column('Sexo', anchor=W, width=50)
    self.lista.column('Telefone', anchor=W, width=130)
    self.lista.column('CPF', anchor=W, width=120)

    self.lista.heading('Nome', text='Nome', anchor=W)
    self.lista.heading('Sobrenome', text='Sobrenome', anchor=W)
    self.lista.heading('Idade', text='Idade', anchor=W)
    self.lista.heading('Sexo', text='Sexo', anchor=W)
    self.lista.heading('Telefone', text='Telefone', anchor=W)
    self.lista.heading('CPF', text='CPF', anchor=W)
    
    self.voltarLista()
    def pesquisaLista():
      self.getPesquisa = self.pesquisa.get()
      print(self.getPesquisa)
      #Limpar a lista..
      for valor in self.lista.get_children():
        self.lista.delete(valor)
      #Gerar lista com filtro
      for i in executarSQL(f'select * from cliente where nome = "{self.getPesquisa}"'): #meeu deus
        self.lista.insert(parent='', index='end', values=(i[1], i[2], i[4], i[5], i[3], i[0]))

    self.lista.pack(pady=(10,0))
    self.bottomFrame = Frame(self)
    self.bottomFrame.pack(pady=(8, 0), anchor=W)

    self.pesquisaName = Label(self.bottomFrame, text='Pesquisar: ')
    self.pesquisa = Entry(self.bottomFrame)
    self.botaoPesquisa = Button(self.bottomFrame, text='OK', command=pesquisaLista)
    self.botaoVoltar = Button(self.bottomFrame, text='Atualizar', command=self.voltarLista)
    self.botaoCadastrarCliente = Button(self.bottomFrame, text='Cadastrar cliente', command=mostrarCadastro)


    self.pesquisaName.grid(row=0, column=0)
    self.pesquisa.grid(row=0, column=1)
    self.botaoPesquisa.grid(row=0, column=2, padx=(2,0))
    self.botaoVoltar.grid(row=0, column=3, padx=(5,0))
    self.botaoCadastrarCliente.grid(row=0, column=4, padx=(320, 0))

class MenuRelatorio(Frame):
  
  def voltarLista(self):
    count = 0
    for valor in self.lista.get_children():
      self.lista.delete(valor)
    for i in executarSQL('select livro.titulo, cliente.nome, emprestimo.data_retirada, emprestimo.data_entrega, emprestimo.num_emprestimo from emprestimo inner join livro on emprestimo.fk_livro = livro.isbn inner join cliente on emprestimo.fk_cliente = cliente.cpf'): #meeu deus
      self.lista.insert(parent='', index='end', iid=count, values=(i[0], i[1], i[2], i[3], i[4]))
      count += 1

  def __init__(self, parent):
    super().__init__()

    self.title = Label(self, text='Relatorio', font=('Arial', 25), pady=10).pack()
    self.lista = ttk.Treeview(self)
    self.lista['columns'] = ('Livro', 'Cliente', 'Retirada', 'Entrega', 'Codigo')

    self.lista.column('#0', anchor=W, width=0)
    self.lista.column('Livro', anchor=W, width=240)
    self.lista.column('Cliente', anchor=W, width=150)
    self.lista.column('Retirada', anchor=W, width=90)
    self.lista.column('Entrega', anchor=W, width=90)
    self.lista.column('Codigo', anchor=W, width=110)

    self.lista.heading('Livro', text='Livro', anchor=W)
    self.lista.heading('Cliente', text='Cliente', anchor=W)
    self.lista.heading('Retirada', text='Retirada', anchor=W)
    self.lista.heading('Entrega', text='Entrega', anchor=W)
    self.lista.heading('Codigo', text='Codigo', anchor=W)
    
    self.voltarLista()
    def pesquisaLista():
      self.getPesquisa = self.pesquisa.get()
      print(self.getPesquisa)
      #Limpar a lista..
      for valor in self.lista.get_children():
        self.lista.delete(valor)
      #Gerar lista com filtro
      for i in executarSQL(f'select livro.titulo, cliente.nome, emprestimo.data_retirada, emprestimo.data_entrega, emprestimo.num_emprestimo from emprestimo inner join livro on emprestimo.fk_livro = livro.isbn inner join cliente on emprestimo.fk_cliente = cliente.cpf where livro.titulo = "{self.getPesquisa}"'): #meeu deus
        self.lista.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3], i[4]))

    self.lista.pack(pady=(10,0))
    self.bottomFrame = Frame(self)
    self.bottomFrame.pack(pady=(8, 0), anchor=W)

    self.pesquisaName = Label(self.bottomFrame, text='Pesquisar: ')
    self.pesquisa = Entry(self.bottomFrame)
    self.botaoPesquisa = Button(self.bottomFrame, text='OK', command=pesquisaLista)
    self.botaoVoltar = Button(self.bottomFrame, text='Atualizar', command=self.voltarLista)
    self.botaoCadastrarCliente = Button(self.bottomFrame, text='Cadastrar Emprestimo', command=mostrarCadastroEmprestimo)


    self.pesquisaName.grid(row=0, column=0)
    self.pesquisa.grid(row=0, column=1)
    self.botaoPesquisa.grid(row=0, column=2, padx=(2,0))
    self.botaoVoltar.grid(row=0, column=3, padx=(5,0))
    self.botaoCadastrarCliente.grid(row=0, column=4, padx=(330, 0))

class Cadastro(Frame):
  def __init__(self, parent):
    super().__init__()

    def RealizarCadastro():
      self.getCPF = self.entryCPF.get()
      self.getNome = self.entryNome.get()
      self.getSobrenome = self.entrySobrenome.get()
      self.getNasc = self.entryNasc.get()
      self.getSexo = self.entrySexo.get()
      self.getTelefone = self.entryTelefone.get()

      executarSQL(f'insert into cliente values ("{self.getCPF}", "{self.getNome}", "{self.getSobrenome}", "{self.getTelefone}", "{self.getNasc}", "{self.getSexo}"); ')
      entrarCliente()
    #Falta fazer a funcao de verificar se todos os campos estao preenchidos corretamente

    self.frameCadastro = Frame(self)
    self.teste = Label(self, text='Cadastrar Cliente', font=('Arial', 20)).pack(pady=(20,5))
    self.frameCadastro.pack()

    self.labelNome = Label(self.frameCadastro, text='Nome: ')
    self.entryNome = Entry(self.frameCadastro)

    self.labelSobrenome = Label(self.frameCadastro, text='Sobrenome: ')
    self.entrySobrenome = Entry(self.frameCadastro)

    self.labelCPF = Label(self.frameCadastro, text='CPF: ')
    self.entryCPF = Entry(self.frameCadastro)

    self.labelTelefone = Label(self.frameCadastro, text='Telefone: ')
    self.entryTelefone = Entry(self.frameCadastro)

    self.labelNasc = Label(self.frameCadastro, text='Nascimento: ')
    self.entryNasc = Entry(self.frameCadastro)

    self.labelSexo = Label(self.frameCadastro, text='Sexo: ')
    self.entrySexo = Entry(self.frameCadastro)

    self.labelNome.grid(row=0, column=0, sticky=E)
    self.entryNome.grid(row=0, column=1, padx=(0, 50))

    self.labelSobrenome.grid(row=0, column=2, padx=(50, 0))
    self.entrySobrenome.grid(row=0, column=3)

    self.labelCPF.grid(row=1, column=0, sticky=E, pady=10)
    self.entryCPF.grid(row=1, column=1, padx=(0, 50))

    self.labelTelefone.grid(row=1, column=2, padx=(50, 0), sticky=E)
    self.entryTelefone.grid(row=1, column=3)

    self.labelNasc.grid(row=2, column=0, sticky=E)
    self.entryNasc.grid(row=2, column=1, padx=(0, 50))

    self.labelSexo.grid(row=2, column=2, sticky=E, padx=(50, 0))
    self.entrySexo.grid(row=2, column=3)

    self.botaoCadastrar = Button(self, text='Cadastrar', command=RealizarCadastro, width=15)
    self.botaoFechar = Button(self, text='fechar', command=fecharCadastro)

    self.botaoCadastrar.pack(pady=(20,4))
    self.botaoFechar.pack()

class CadastroLivro(Frame):
  def __init__(self, parent):
    super().__init__()

    def RealizarCadastro():
      self.getTitulo = self.entryTitulo.get()
      self.getAutor = self.clicked.get()
      self.getAno = self.entryAno.get()
      self.getGenero = self.clicked2.get()
      self.getIsbn = self.entryIsbn.get()

      executarSQL(f'insert into livro values ("{self.getIsbn}", "{self.getTitulo}", "{self.getAno}", (select autor.id_autor from autor where autor.nome = "{self.getAutor}"), (select genero.id_genero from genero where genero.tipo = "{self.getGenero}")); ')
      entrarLivro()
      fecharCadastroLivro()

    #Falta fazer a funcao de verificar se todos os campos estao preenchidos corretamente
    self.frameCadastro = Frame(self)
    self.teste = Label(self, text='Cadastrar Livro', font=('Arial', 20)).pack(pady=(20,5))
    self.frameCadastro.pack()

    self.labelTitulo = Label(self.frameCadastro, text='Titulo: ')
    self.entryTitulo = Entry(self.frameCadastro)

    self.generos = executarSQL(f'select nome from autor')
    self.generosLista = []
    for i in self.generos:
      self.generosLista.append(i[0])
    self.clicked = StringVar(self)
    self.clicked.set(self.generosLista[0])

    self.labelAutor = Label(self.frameCadastro, text='Autor: ')
    self.entryAutor = OptionMenu(self.frameCadastro, self.clicked, *self.generosLista)

    self.labelAno = Label(self.frameCadastro, text='Ano: ')
    self.entryAno = Entry(self.frameCadastro)

    self.autores = executarSQL(f'select tipo from genero')
    self.autoresLista = []
    for i in self.autores:
      self.autoresLista.append(i[0])
    self.clicked2 = StringVar(self)
    self.clicked2.set(self.autoresLista[0])

    self.labelGenero = Label(self.frameCadastro, text='Genero: ')
    self.entryGenero = OptionMenu(self.frameCadastro, self.clicked2, *self.autoresLista)

    self.labelIsbn = Label(self.frameCadastro, text='ISBN: ')
    self.entryIsbn = Entry(self.frameCadastro)

    self.labelTitulo.grid(row=0, column=0, sticky=E)
    self.entryTitulo.grid(row=0, column=1, padx=(0, 50))

    self.labelAutor.grid(row=0, column=2, padx=(50, 0))
    self.entryAutor.grid(row=0, column=3)

    self.labelAno.grid(row=1, column=0, sticky=E, pady=10)
    self.entryAno.grid(row=1, column=1, padx=(0, 50))

    self.labelGenero.grid(row=1, column=2, padx=(50, 0), sticky=E)
    self.entryGenero.grid(row=1, column=3)

    self.labelIsbn.grid(row=2, column=0, sticky=E)
    self.entryIsbn.grid(row=2, column=1, padx=(0, 50))

    self.botaoCadastrar = Button(self, text='Cadastrar', command=RealizarCadastro, width=15)
    self.botaoFechar = Button(self, text='fechar', command=fecharCadastroLivro)

    self.botaoCadastrar.pack(pady=(20,4))
    self.botaoFechar.pack()

class CadastroEmprestimo(Frame):
  def __init__(self, parent):
    super().__init__()

    def RealizarCadastro():
      self.getCodigo = self.entryCodigo.get()
      self.getIsbn = self.clicked.get()
      self.getDataSaida = self.entryDataSaida.get()
      self.getCpf = self.clicked2.get()
      self.getDataEntrega = self.entryDataEntrega.get()
      print(self.getCpf, self.getIsbn)
      executarSQL(f'insert into emprestimo values ("{self.getCodigo}", "{self.getDataSaida}", "{self.getDataEntrega}", "{self.getCpf}", "{self.getIsbn}"); ')
      entrarRelatorio()
    #Falta fazer a funcao de verificar se todos os campos estao preenchidos corretamente

    self.frameCadastro = Frame(self)
    self.teste = Label(self, text='Cadastrar Emprestimo', font=('Arial', 20)).pack(pady=(20,5))
    self.frameCadastro.pack()

    self.labelCodigo = Label(self.frameCadastro, text='Codigo: ')
    self.entryCodigo = Entry(self.frameCadastro)

    #DropBox de selecionar o isbn do livro
    self.isbn = executarSQL(f'select isbn from livro')
    self.isbnLista = []
    for i in self.isbn:
      self.isbnLista.append(i[0])
    self.clicked = StringVar(self)
    self.clicked.set(self.isbnLista[0])

    self.labelIsbn = Label(self.frameCadastro, text='ISBN: ')
    self.entryIsbn = OptionMenu(self.frameCadastro, self.clicked, *self.isbnLista)

    self.labelDataSaida = Label(self.frameCadastro, text='Data Saida: ')
    self.entryDataSaida = Entry(self.frameCadastro)

    #DropBox de selecionar o CPF do cliente
    self.cpf = executarSQL(f'select cpf from cliente')
    self.cpfLista = []
    for i in self.cpf:
      self.cpfLista.append(i[0])
    self.clicked2 = StringVar(self)
    self.clicked2.set(self.cpfLista[0])

    self.labelCpf = Label(self.frameCadastro, text='CPF: ')
    self.entryCpf = OptionMenu(self.frameCadastro, self.clicked2, *self.cpfLista)

    self.labelDataEntrega = Label(self.frameCadastro, text='Data Entrega: ')
    self.entryDataEntrega = Entry(self.frameCadastro)

    self.labelCodigo.grid(row=0, column=0, sticky=E)
    self.entryCodigo.grid(row=0, column=1, padx=(0, 50))

    self.labelDataSaida.grid(row=1, column=0, sticky=E, pady=10)
    self.entryDataSaida.grid(row=1, column=1, padx=(0, 50))

    self.labelDataEntrega.grid(row=1, column=2, padx=(50, 0), sticky=E)
    self.entryDataEntrega.grid(row=1, column=3)

    self.labelIsbn.grid(row=2, column=0, sticky=E)
    self.entryIsbn.grid(row=2, column=1, padx=(0, 50))

    self.labelCpf.grid(row=2, column=2, sticky=E)
    self.entryCpf.grid(row=2, column=3)

    self.botaoCadastrar = Button(self, text='Cadastrar', command=RealizarCadastro, width=15)
    self.botaoFechar = Button(self, text='fechar', command=fecharCadastroEmprestimo)

    self.botaoCadastrar.pack(pady=(20,4))
    self.botaoFechar.pack()


frame_login = LoginPerfil(root)
frame_menu = Menu(root)

frame_livro = MenuLivro(root)
frame_cliente = MenuCliente(root)
frame_relatorio = MenuRelatorio(root)
frame_cadastro = Cadastro(root)
frame_cadastro_livro = CadastroLivro(root)
frame_cadastro_emprestimo = CadastroEmprestimo(root)

frame_login.pack()
root.mainloop()

#root.progressbar.place(relx=.5, rely=.5, anchor="c")