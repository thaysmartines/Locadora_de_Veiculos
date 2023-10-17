from Model.DTO.VeiculoDTO import VeiculoDTO
from Model.DAO.VeiculoDAO import VeiculoDAO

class VeiculoCTR:
    def CadastrarVeiculo(self, codigoVeic, modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao, tipoVeiculo):
        veiculoDTO = VeiculoDTO()
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.Batido = batido
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.Descricao = descricao
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO()
        veiculoDAO.CadastrarVeiculo(veiculoDTO)  # Removendo o argumento 'codigoVeic'

    def AtualizarVeiculo(self, codigoVeic, modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao, tipoVeiculo):
        veiculoDTO = VeiculoDTO()
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.Batido = batido
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.Descricao = descricao
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO()
        veiculoDAO.AtualizarVeiculo(codigoVeic, veiculoDTO)


    def PesquisarVeiculosDisponiveis(self):
        veiculoDAO = VeiculoDAO()
        query = veiculoDAO.PesquisarVeiculosDisponiveis()

        return query

    def PesquisarTodosVeiculos(self):
        veiculoDAO = VeiculoDAO()
        query = veiculoDAO.PesquisarTodosVeiculos()

        return query

    def PesquisarVeiculo(self, valor, tipo):
        veiculoDAO = VeiculoDAO()
        query = veiculoDAO.PesquisarVeiculo(valor, tipo)

        return query

    def ExcluirVeiculo(self, codigoVeic):
        veiculoDAO = VeiculoDAO()
        veiculoDAO.ExcluirVeiculo(codigoVeic)
