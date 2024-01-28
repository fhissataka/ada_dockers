# app.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI()

# MySQL configurations
db_config = {
    'host': 'db',
    'user': 'flaskuser',
    'password': 'flaskpassword',
    'database': 'flaskapp',
}

def create_table():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create a table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

def insert_sample_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert sample data into the 'demo' table
    cursor.execute("INSERT INTO demo (name) VALUES ('Fernando')")
    cursor.execute("INSERT INTO demo (name) VALUES ('Joniel')")
    cursor.execute("INSERT INTO demo (name) VALUES ('Gabriel')")
    cursor.execute("INSERT INTO demo (name) VALUES ('Rodrigo')")

    connection.commit()
    cursor.close()
    connection.close()

def delete_sample_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Delete sample data from the 'demo' table
    cursor.execute("DELETE FROM demo")

    connection.commit()
    cursor.close()
    connection.close()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>Bem-vindo ao projeto final de Dockers do ADA iFood!</h1>
    <h2>Por Fernando Hissataka, janeiro de 2024<h2>
    <br>
    <h2>Comandos disponíveis:</h2>
    <ul>
        <li><a href="/">Home</a></li>
        <br>
        <li><a href="/inicia">Inicializa o BD</a></li>
        <br>
        <li><a href="/insere">Insere dados de amostra no BD</a></li>
        <br>
        <li><a href="/deleta">Deleta todos os dados do BD</a></li>
        <br>
        <li><a href="/pesquisa">Mostra os dados do BD</a></li>
    </ul>
    """

@app.get("/inicia")
def init_db():
    create_table()
    return "O banco de dados foi inicializado!"

@app.get("/insere")
def insert_sample_data_route():
    insert_sample_data()
    return "Foram inseridos registros com amostras no banco de dados!"


@app.get("/deleta")
def delete_sample_data_route():
    delete_sample_data()
    return "Foram deletados todos os registros do banco de dados!"

@app.get("/pesquisa", response_class=HTMLResponse)
def fetch_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch data from the 'demo' table
    cursor.execute("SELECT name FROM demo")
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    # return HTMLResponse(content=f"<h1>Dados do MySQL:</h1><ul>{''.join(f'<li>{row}</li>' for row in data)}</ul>")
    result = "<h1>Pesquisa no MySQL:</h1><ul>"
    for row in data:
        result += f"<li>{row}</li>"
    result += "</ul>"

    return HTMLResponse(content=result)

if __name__ == "__main__":
    create_table()         # Create the table if it doesn't exist on app startup
    insert_sample_data()   # Insert sample data on app startup
