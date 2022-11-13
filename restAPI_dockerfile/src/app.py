'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
from flask import Flask, jsonify
from users import users

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    '''Rota inicial da minha aplicação'''
    return jsonify({"response": "Hello colegas da UFES-Vale"})

@app.route("/users")
def usershandler():
    '''Rota de Usuários.'''
    return jsonify({"users": users})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
