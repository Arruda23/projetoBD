from flask import Flask, render_template, request, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite' #faz a conexão do banco de dados 

db=SQLAlchemy(app)

class Imovel(db.Model): #cria um modelo de banco de dados do imovel
	__tablename__='imoveis'

	numero=db.Column(db.Integer, primary_key=True, autoincrement=True) 
	endereco=db.Column(db.String)
	dimensoes=db.Column(db.Float)
	tipo=db.Column(db.String)
	qtdcomodos=db.Column(db.Integer)
	responsavel=db.Column(db.String)
	status=db.Column(db.String)
	data=db.Column(db.String)

	def __init__(self, endereco, dimensoes, tipo, qtdcomodos, responsavel, status, data): #construtor do imovel
		self.endereco=endereco
		self.dimensoes=dimensoes
		self.tipo=tipo
		self.qtdcomodos=qtdcomodos
		self.responsavel=responsavel
		self.status=status
		self.data=data


db.create_all() #cria o banco de dados

	

@app.route("/index") #cria um caminho para a pagina html do inicio
def index():
	return render_template("index.html")

@app.route("/cadastrar") #cria o caminho para pagina html de cadastro
def cadastrar():
	return render_template("cadastro.html")

@app.route("/cadastro", methods=['GET','POST']) #recebe os dados da pagina de cadastro e manda para o bd
def cadastro():
	if request.method=="POST":
		endereco=request.form.get("endereco")
		dimensoes=request.form.get("dimensoes")
		tipo=request.form.get("tipo")
		qtdcomodos=request.form.get("qtdcomodos")
		responsavel=request.form.get("responsavel")
		status=request.form.get("status")
		data=request.form.get("data")

		if endereco and dimensoes and tipo and qtdcomodos and responsavel and status and data:
			i = Imovel(endereco, dimensoes, tipo, qtdcomodos, responsavel, status, data)
			db.session.add(i) #cria uma nova linha no bd
			db.session.commit() #aplica as alterações
		
	return redirect(url_for("index")) #retorna para a pagina inicial

@app.route("/lista") #cria o caminho para pagina html de listagem 
def lista():
	imoveis= Imovel.query.all()
	return render_template("lista.html", imoveis=imoveis)
if __name__=='__main__':
	app.run(debug=True)