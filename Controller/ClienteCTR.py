from Model.DTO.ClienteDTO import ClienteDTO
from Model.DAO.ClienteDAO import ClienteDAO

class ClienteCTR:
    def CadastrarCliente(self, nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO()
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO()
        clienteDAO.CadastrarCliente(clienteDTO)

    def AtualizarCliente(self, codigoCli, nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO()
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO()
        clienteDAO.AtualizarCliente(codigoCli, clienteDTO)

    def PesquisarTodosClientes(self):
        clienteDAO = ClienteDAO()
        query = clienteDAO.PesquisarTodosClientes()

        return query

    def PesquisarCliente(self, valor, tipo):
        clienteDAO = ClienteDAO()
        query = clienteDAO.PesquisarCliente(valor, tipo)

        return query

    def ExcluirCliente(self, codigoCli):
        clienteDAO = ClienteDAO()
        clienteDAO.ExcluirCliente(codigoCli)
