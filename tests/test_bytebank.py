import pytest

from codigo.bytebank import Funcionario
from pytest import mark

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

        lucas = Funcionario(entrada, '10/10/2000', esperado)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then

    @mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '10/10/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, '10/10/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bunus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000  # Given
            entrada_nome = 'Paulo Bragança'

            funcionario_teste = Funcionario(entrada_nome, '10/10/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # Then