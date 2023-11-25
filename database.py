import mysql.connector;

def open_conect(host, user, password, database):
    return mysql.connector.connect(host = host, user = user, password = password, database = database);

def close_connect(connect):
    connect.close();

def create(connect, name, weaknesses, neutral, strong):
    statement = connect.cursor();
    sql = "INSERT INTO monstros (nome, fraquezas, neutro, forte) VALUES (%s, %s, %s, %s)";
    values = (name, weaknesses, neutral, strong);
    statement.execute(sql, values);
    statement.close();
    connect.commit();

def read(connect, id):
    statement = connect.cursor();
    sql = "SELECT * FROM monstros WHERE id_monstro = %s";
    value = (id,);
    statement.execute(sql, value);

    for(id, nome, fraquezas, neutro, forca) in statement:
        print(id, nome, fraquezas, neutro, forca);

    statement.close();

def update(connect, name, id):
    statement = connect.cursor();
    sql = "UPDATE monstros SET nome = %s WHERE id_monstro = %s";
    values = (name, id);
    statement.execute(sql, values);
    statement.close();
    connect.commit();

def delete(connect, id):
    statement = connect.cursor();
    sql = "DELETE FROM monstros WHERE id_monstro = %s";
    values = (id,);
    statement.execute(sql, values);
    statement.close();
    connect.commit();