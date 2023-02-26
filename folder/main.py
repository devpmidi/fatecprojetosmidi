from flask import *
import sqlite3

app = Flask(__name__)
print(app)
def info():
  con = sqlite3.connect("dados.db")
  cur = con.cursor()
  cur.execute("create table if not exists users (name, key, email, cpf, niver)")
@app.route('/')
def home():
  info()
  return render_template('home.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')
  
@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastro():
    info()
    print("CADASTROOO")
    rota = '/login'
    #cur.execute("delete from users")
    #con.commit()   
    con = sqlite3.connect("dados.db")
    cur = con.cursor()
    html = "cadastro.html"
    if request.method == 'GET':
        print("GET")
        return render_template(html)
    
    nome = request.form.get("name")
    email = request.form.get("email")
    cpf = request.form.get("cpf")
    senha = request.form.get("key")
    niver = request.form.get("niver")
  
    if not request.form.get("login") == None:
        return render_template("login.html", rota = '/cadastro')

    try:
      if not ''.join([nome,email,senha,cpf, niver]):
          return render_template(html, rota = rota)
    except:
      return render_template(html, rota=rota)


    usuario = [email, cpf]
    erros = ['']*2
    msg = ('Email já cadastrado! ', 'CPF já cadastrado! ')

    dados = cur.execute("select * from users where name = ?", (nome,))
    dados = cur.fetchall()

    if len(dados) > 0:
        print(dados)
        for i in range(2, len(usuario)+2):

            if dados[0][i] == usuario[i-2]:
                erros[i-2] = msg[i-2]

        return render_template(html, rota='/login', nome=f"Nome '{nome}' ja está cadastrado!",
            email=erros[0], cpf=erros[1])


    usuario = (nome, senha, email, cpf, niver)
    cur.execute("insert into users values (?, ?, ?, ?, ?)", usuario)
    con.commit()

    html = "login.html"                       
    print('sucesso')
    return render_template(html, rota = '/login')

@app.route("/login",  methods = ['POST', 'GET'])
def login():
    info()
    print('LOGIN')
    rota = '/login'
    html = 'login.html'
    con = sqlite3.connect("dados.db")
    cur = con.cursor()

    if request.method == 'GET':
        print('GET')
        return render_template("login.html", rota=rota)

    email = request.form.get("email")
    senha = request.form.get("key")

    try:
        if not ''.join([email,senha]):
            return render_template(html, rota=rota)
    except:
        print('amigo?', email, senha)
        return render_template("login.html", rota='index')
    

    user = [senha, email]
    
    msg = ('Senha incorreta! ', 'Email não cadastrado! ')

    dados = cur.execute("select email, key from users where email == (?)", (email,))
    dados = cur.fetchall()
    print(user, dados)
  
    if not dados:
       return render_template("login.html", email='Email não cadastrado! ')
    print(dados, 'aaaaaaaaaaaaaa')
    erros = ['']*2
    
    for i in range(0, len(user)):

        if dados[0][i] != user[i-1]:
            erros[i-1] = msg[i-1] + 'Verifique se digitou corretamente!'

    if erros.count('') < len(erros):
        return render_template(html, rota='/cadastro', email=erros[1], senha=erros[0])
    
    html = 'logou.html'
    rota = '/index'
    print('sucesso')
    return render_template("loginCon.html", rota=rota, nameForm='index')

@app.route("/index", methods = ['POST', 'GET'] )
def index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)