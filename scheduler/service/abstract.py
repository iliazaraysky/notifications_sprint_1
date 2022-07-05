from abc import ABC, abstractmethod


class ServiceAbstract(ABC):
    @abstractmethod
    def get_users(self, data: str):
        pass
