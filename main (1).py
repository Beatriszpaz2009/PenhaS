"""
main.py - script de teste para validar a estrutura e os relacionamentos
entre as classes criadas a partir do diagrama UML.
"""

from usuarios import Vitima
from ocorrencias import Ocorrencia, Evidencia, Informacoes, MedidaProtetiva
from apoio import RedeDeApoio, ServicoPublico


def main():
    # Cria uma vítima (herda de Usuario)
    vitima = Vitima(id=1, nome="Maria", email="maria@email.com", endereco="Rua A, 123")

    # Cria serviço público e rede de apoio (composição)
    servico = ServicoPublico(orgao="Delegacia da Mulher")
    rede = RedeDeApoio(telefone="180", servico_publico=servico)
    rede.associar_vitima(vitima)

    # Cria uma ocorrência ligada à vítima
    ocorrencia = Ocorrencia(descricao="Registro de ameaça", status="aberta", vitima=vitima)

    # Adiciona evidência e informações à ocorrência
    evidencia = Evidencia(tipo="Áudio")
    ocorrencia.adicionar_evidencia(evidencia)

    info = Informacoes(idinfo=1, titulo="Boletim", descricao="Detalhes do caso")
    ocorrencia.adicionar_informacao(info)

    # Cria uma medida protetiva (composição com Ocorrencia)
    medida = MedidaProtetiva(
        id_medida=1,
        numero_processo="0001/2026",
        tipo_medida="Afastamento",
        data_validade="2026-12-31",
    )
    ocorrencia.criar_medida_protetiva(medida)

    print(vitima)
    print(rede)
    print(ocorrencia)
    print(ocorrencia.evidencias)
    print(ocorrencia.informacoes)
    print(ocorrencia._medidas_protetivas)


if __name__ == "__main__":
    main()
