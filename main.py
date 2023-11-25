from database import open_conect, close_connect, create, read, update, delete

def main():

    connect = open_conect("localhost", "root", "", "tibia");

    create(connect, "Cyclop", "Terra, Morte", "Gelo, Fogo", "Energia, Sagrado");
    read(connect, 4);
    update(connect, "Neves", 2);
    delete(connect, 5);

    close_connect(connect);

if __name__ == "__main__":
    main();
