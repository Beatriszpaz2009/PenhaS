"""
Módulo: ocorrencias.py
Classes: Ocorrencia, Evidencia, MedidaProtetiva, Informacoes
Relacionamentos (do diagrama):
  - Vitima 1 -> 0..* Ocorrencia          (associação, ver usuarios.py)
  - Ocorrencia 1 <-> 0..* Evidencia      (associação)
  - Ocorrencia 1 <-> 0..* Informacoes    (associação)
  - Ocorrencia 1 ◆-> 0..* MedidaProtetiva (composição: Ocorrencia é dona
    do ciclo de vida das MedidasProtetivas)
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from usuarios import Vitima


class Evidencia:
    """Associada a uma Ocorrencia (0..* Evidencia <-> 1 Ocorrencia)."""

    def __init__(self, tipo: str):
        self._tipo = tipo

    def validar(self) -> int:
        pass

    def validar_short(self, valor: int) -> int:
        """Sobrecarga lógica de validar(short: int): int no diagrama."""
        pass

    def __repr__(self):
        return f"Evidencia(tipo={self._tipo!r})"


class Informacoes:
    """Associada a uma Ocorrencia (0..* Informacoes <-> 1 Ocorrencia)."""

    def __init__(self, idinfo: int, titulo: str, descricao: str):
        self._idinfo = idinfo
        self._titulo = titulo
        self._descricao = descricao

    def listar(self) -> None:
        pass

    def pesquisar(self) -> None:
        pass

    def __repr__(self):
        return f"Informacoes(idinfo={self._idinfo}, titulo={self._titulo!r})"


class MedidaProtetiva:
    """
    Parte da composição Ocorrencia ◆-> MedidaProtetiva.
    Só deve existir enquanto a Ocorrencia dona existir.
    """

    def __init__(
        self,
        id_medida: int,
        numero_processo: str,
        tipo_medida: str,
        data_validade: str,
    ):
        self._id_medida = id_medida
        self._numero_processo = numero_processo
        self._tipo_medida = tipo_medida
        self._data_validade = data_validade

    def cadastrar(self) -> None:
        pass

    def atualizar(self) -> None:
        pass

    def encerrar(self) -> None:
        pass

    def __repr__(self):
        return f"MedidaProtetiva(id_medida={self._id_medida}, tipo={self._tipo_medida!r})"


class Ocorrencia:
    """
    Classe central do sistema.
    - Associação 1 <-> 0..* com Vitima
    - Associação 1 <-> 0..* com Evidencia
    - Associação 1 <-> 0..* com Informacoes
    - Composição 1 ◆-> 0..* com MedidaProtetiva
    """

    def __init__(self, descricao: str, status: str, vitima: "Vitima"):
        self._descricao = descricao
        self._status = status

        # Associação com a vítima que registrou a ocorrência
        self.vitima = vitima
        vitima.ocorrencias.append(self)

        # Associações "abertas" (listas de referências)
        self.evidencias: List[Evidencia] = []
        self.informacoes: List[Informacoes] = []

        # Composição: a Ocorrencia cria/possui as MedidasProtetivas
        self._medidas_protetivas: List[MedidaProtetiva] = []

    def abrir(self) -> None:
        pass

    def finalizar(self) -> None:
        pass

    def get_status(self) -> str:
        return self._status

    def adicionar_evidencia(self, evidencia: Evidencia) -> None:
        self.evidencias.append(evidencia)

    def adicionar_informacao(self, informacao: Informacoes) -> None:
        self.informacoes.append(informacao)

    def criar_medida_protetiva(self, medida: MedidaProtetiva) -> None:
        """Composição: a MedidaProtetiva passa a pertencer a esta Ocorrencia."""
        self._medidas_protetivas.append(medida)

    def __repr__(self):
        return f"Ocorrencia(descricao={self._descricao!r}, status={self._status!r})"
