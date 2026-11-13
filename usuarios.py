"""
Módulo: usuarios.py
Classes: Usuario, Vitima
Relacionamento: Vitima herda de Usuario (generalização no diagrama UML)
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    # Import só para checagem de tipos (evita import circular em runtime)
    from apoio import RedeDeApoio
    from ocorrencias import Ocorrencia


class Usuario:
    """Classe base para qualquer usuário do sistema."""

    def __init__(self, id: int, nome: str, email: str):
        self._id = id
        self._nome = nome
        self._email = email

    def login(self) -> None:
        """Realiza login do usuário."""
        pass

    def login_com_email(self, email: str) -> int:
        """Sobrecarga lógica de login(email: str): int no diagrama."""
        pass

    def notificar(self) -> None:
        """Notifica o usuário."""
        pass

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def __repr__(self):
        return f"Usuario(id={self._id}, nome={self._nome!r})"


class Vitima(Usuario):
    """
    Vitima herda de Usuario.
    Associações (do diagrama):
      - Vitima 0..* <-> 1 RedeDeApoio
      - Vitima 1 -> 0..* Ocorrencia
    """

    def __init__(self, id: int, nome: str, email: str, endereco: str):
        super().__init__(id, nome, email)
        self._endereco = endereco
        # 0..* -> 1: a vítima pode estar associada a uma rede de apoio
        self.rede_de_apoio: "RedeDeApoio | None" = None
        # 1 -> 0..*: uma vítima pode ter várias ocorrências
        self.ocorrencias: List["Ocorrencia"] = []

    def pedir_ajuda(self) -> None:
        pass

    def registrar_ocorrencia(self) -> None:
        pass

    def notificar(self) -> None:
        # Sobrescreve notificar() de Usuario, se necessário
        pass

    def __repr__(self):
        return f"Vitima(id={self._id}, nome={self._nome!r}, endereco={self._endereco!r})"
