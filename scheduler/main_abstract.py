from abc import ABC, abstractmethod
from typing import List


class SchedulerAbstract(ABC):

    @abstractmethod
    def get_events(self) -> List[str]:
        pass

    @abstractmethod
    def task(self) -> List[str]:
        pass

    @abstractmethod
    def mark_event_send(self, event_id: str):
        pass

    @abstractmethod
    def mark_event_cancelled(self, event_id: str):
        pass

    @abstractmethod
    def mark_event_done(self, event_id: str):
        pass
