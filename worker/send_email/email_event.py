from abc import ABC, abstractmethod
from typing import Dict


class EventWelcomeAbstract(ABC):
    @abstractmethod
    def letter(self, data: Dict):
        pass


class SenderEmailAbstract(ABC):
    @abstractmethod
    def send(self, address: str, subject: str, data: str):
        pass
