from typing import Optional, Any, Dict

from pydantic import BaseModel
import uuid


class MessageStatus(str):
    send = 'send'
    cancelled = 'cancelled'
    done = 'done'


class MessageType(str):
    welcome = 'welcome'
    recommendation = 'recommendation'
    monthly_statistics = 'monthly statistics'


class EventPriority:
    low = 'low'
    medium = 'medium'
    high = 'high'


class EventEmailMessage(BaseModel):
    user_id: Optional[str]
    message_status: MessageStatus
    message_type: MessageType


class Event(BaseModel):
    id: uuid
    event_priority: EventPriority
    user_id: Optional[str]
    context: Dict[str, Any]
    message_status: MessageStatus
    message_type: MessageType
