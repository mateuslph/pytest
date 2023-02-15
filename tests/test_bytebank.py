from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retonar_22(self):

        entrada = '2000' # Given - Contexto
        esperado = 23

        funcionario_teste = Funcionario('teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When - Acao

        assert resultado == esperado # Then - Desfecho

    def test_quando_nome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then