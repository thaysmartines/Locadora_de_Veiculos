from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class AluguelDAO:
    def CadastrarAluguel(self, aluguel):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()

        query.prepare("UPDATE Veiculo SET Alugado = 'Sim' WHERE CodigoVeic = ?")
        query.addBindValue(aluguel.CodigoVeic)
        query.exec_()
        db.commit()

        query.prepare("INSERT INTO Aluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel, "
                      "ValorMulta, KmEntrada, KmSaida, CodigoCli, CodigoVeic) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(aluguel.DataAluguel)
        query.addBindValue(aluguel.DataPrazo)
        query.addBindValue(aluguel.DataDevolucao)
        query.addBindValue(aluguel.ValorAluguel)
        query.addBindValue(aluguel.ValorMulta)
        query.addBindValue(aluguel.KmEntrada)
        query.addBindValue(aluguel.KmSaida)
        query.addBindValue(aluguel.CodigoCli)
        query.addBindValue(aluguel.CodigoVeic)
        query.exec_()
        db.commit()

    def PesquisarTodosAluguel(self):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        sql = "SELECT Aluguel.*, Cliente.Nome FROM Aluguel " \
              "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli"
        query = QSqlQuery(sql)

        return query

    def PesquisarAluguel(self, valor, tipo):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()

        if tipo == 'Código Aluguel':
            query.prepare("SELECT Aluguel.*, Cliente.Nome FROM Aluguel "
                          "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli "
                          "where Aluguel.CodigoAlug = ?")
            query.addBindValue(valor)
        elif tipo == 'Código Cliente':
            query.prepare("SELECT Aluguel.*, Cliente.Nome FROM Aluguel "
                          "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli "
                          "where Aluguel.CodigoCli = ?")
            query.addBindValue(valor)
        elif tipo == 'Código Veículo':
            query.prepare("SELECT Aluguel.*, Cliente.Name FROM Aluguel "
                          "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli "
                          "where Aluguel.CodigoVeic = ?")
            query.addBindValue(valor)
        elif tipo == 'Nome Cliente':
            query.prepare("SELECT Aluguel.*, Cliente.Name FROM Aluguel "
                          "INNER JOIN Cliente ON Aluguel.CodigoCli = Cliente.CodigoCli "
                          "where Cliente.Name = ?")
            query.addBindValue(valor)

        query.exec()
        return query

    def DevolverVeiculo(self, codigoAlug, aluguel):
        conn = ConexaoSQL()
        db = conn.getConexao()
        if not db.isOpen():
            db.open()

        query = QSqlQuery()

        select = "SELECT Veiculo.CodigoVeic FROM Aluguel"\
                      " INNER JOIN Veiculo ON Aluguel.CodigoVeic = Veiculo.CodigoVeic"\
                      " WHERE Aluguel.CodigoAlug = " + codigoAlug

        query.exec(select)

        while query.next():
            codigoVeic = str(query.value(0))

        sql = "UPDATE Veiculo SET Alugado = 'Não' WHERE CodigoVeic = " + codigoVeic
        query.prepare(sql)
        query.exec()
        db.commit()

        sql = "UPDATE Aluguel SET DataDevolucao = ?, ValorMulta = ?, KmSaida = ? WHERE CodigoAlug = ?"
        query.prepare(sql)
        query.addBindValue(aluguel.DataDevolucao)
        query.addBindValue(aluguel.ValorMulta)
        query.addBindValue(aluguel.KmSaida)
        query.addBindValue(codigoAlug)
        query.exec()
        db.commit()
