from . import app
from flask import Flask, render_template, request
from flask_login import current_user
from db import update_user
from db import delete_user
from db import validar_login

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    # Obter os dados do formulário de login
    username = request.form.get('username')
    password = request.form.get('password')

    # Chamar a função de validação de login no arquivo db.py
    if validar_login(username, password):
        # Dados de login válidos
        return 'Login bem-sucedido!'
    else:
        # Dados de login inválidos
        return 'Falha no login. Verifique suas credenciais.'


#pagina de usuario
@app.route('/user_profile', methods=['GET'])
def user_profile():
    user_id = get_current_user_id()  # Obtenha o ID do usuário atualmente logado
    # Obtenha os dados do usuário do banco de dados com base no user_id
    user_data = get_user_data(user_id)
    return render_template('user_profile.html', user_data=user_data)




#atualizacao de user
@app.route('/user_profile/update', methods=['POST'])
def update_user_profile():
    user_id = current_user.id
    new_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email')
    }
    # Atualize os dados do usuário no banco de dados
    update_user(user_id, new_data)
    return redirect(url_for('user_profile'))




#deletando usuario
@app.route('/user_profile/delete', methods=['POST'])
def delete_user_profile():
    user_id = get_current_user_id()  # Obtenha o ID do usuário atualmente logado
    # Exclua o usuário do banco de dados
    delete_user(user_id)
    # Realize qualquer outra ação necessária, como encerrar a sessão do usuário
    return redirect(url_for('home'))

#cadastrando usuario
@app.route('/cadastro', methods=['POST'])
def cadastro():
    render_template('login.html', error='Usuário ou senha inválidos')



