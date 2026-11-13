"""
Módulo: apoio.py
Classes: RedeDeApoio, ServicoPublico
Relacionamentos (do diagrama):
  - Vitima 0..* <-> 1 RedeDeApoio               (associação, ver usuarios.py)
  - RedeDeApoio 1..* ◆-> 1 ServicoPublico        (composição: RedeDeApoio
    é dona do ServicoPublico associado)
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from usuarios import Vitima


class ServicoPublico:
    """Parte da composição RedeDeApoio ◆-> ServicoPublico."""

    def __init__(self, orgao: str):
        self._orgao = orgao

    def atender_ocorrencia(self) -> None:
        pass

    def notificar(self) -> None:
        pass

    def __repr__(self):
        return f"ServicoPublico(orgao={self._orgao!r})"


class RedeDeApoio:
    """
    - Associação 1 <-> 0..* com Vitima
    - Composição 1..* ◆-> 1 com ServicoPublico
      (aqui simplificado: cada RedeDeApoio possui um ServicoPublico)
    """

    def __init__(self, telefone: str, servico_publico: ServicoPublico):
        self._telefone = telefone

        # Vítimas atendidas por esta rede de apoio
        self.vitimas: List["Vitima"] = []

        # Composição: o serviço público pertence a esta rede de apoio
        self._servico_publico = servico_publico

    def receber_alerta(self) -> None:
        pass

    def validar(self, valor: int) -> int:
        pass

    def associar_vitima(self, vitima: "Vitima") -> None:
        self.vitimas.append(vitima)
        vitima.rede_de_apoio = self

    def __repr__(self):
        return f"RedeDeApoio(telefone={self._telefone!r})"
