from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class ClienteDAO:
    def CadastrarCliente(self, cliente):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()
        query.prepare("INSERT INTO Cliente(Nome, CPF, Endereco, Email, Telefone) "
                      "VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(cliente.Nome)
        query.addBindValue(cliente.CPF)
        query.addBindValue(cliente.Endereco)
        query.addBindValue(cliente.Email)
        query.addBindValue(cliente.Telefone)
        query.exec_()
        db.commit()

    def AtualizarCliente(self, codigoCli, cliente):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()
        query.prepare("UPDATE Cliente SET Nome = ?, CPF = ?, Endereco = ?, Email = ?, Telefone = ? "
                      "WHERE CodigoCli = ?")
        query.addBindValue(cliente.Nome)
        query.addBindValue(cliente.CPF)
        query.addBindValue(cliente.Endereco)
        query.addBindValue(cliente.Email)
        query.addBindValue(cliente.Telefone)
        query.addBindValue(codigoCli)
        query.exec_()
        db.commit()

    def ExcluirCliente(self, codigoCli):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()
        query.prepare("DELETE FROM Cliente WHERE CodigoCli = ?")
        query.addBindValue(codigoCli)
        query.exec_()
        db.commit()

    def PesquisarTodosClientes(self):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        sql = "SELECT * FROM Cliente"
        query = QSqlQuery()
        query.exec(sql)

        return query

    def PesquisarCliente(self, valor, tipo):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()

        if tipo == 'Código':
            query.prepare("SELECT * FROM Cliente where CodigoCli = ?")
            query.addBindValue(valor)
        elif tipo == 'Nome':
            query.prepare("SELECT * FROM Cliente where Nome = ?")
            query.addBindValue(valor)
        elif tipo == 'CPF':
            query.prepare("SELECT * FROM Cliente where CPF = ?")
            query.addBindValue(valor)

        query.exec()
        return query