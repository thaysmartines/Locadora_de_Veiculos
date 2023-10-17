from PyQt5.QtSql import QSqlDatabase

class ConexaoSQL:
    def getConexao(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("DataBase/LocadoraDB.db3")

        return db
