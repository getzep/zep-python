from typing import List, Optional, Any, Dict

class Memory:
    def __init__(
        self,
        messages: Optional[List[Dict[str, Any]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        summary: Optional[Dict[str, Any]] = None,
        uuid: Optional[str] = None,
        created_at: Optional[str] = None,
        token_count: Optional[int] = None,
    ):
        if messages is not None:
            self.messages = [Message(**message_data) for message_data in messages]
        else:
            self.messages = []
        self.metadata = metadata if metadata is not None else {}
        self.summary = Summary(**summary) if summary else None
        self.uuid = uuid
        self.created_at = created_at
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        return {
            "messages": [message.to_dict() for message in self.messages],
            "metadata": self.metadata,
            "summary": self.summary.to_dict() if self.summary else None,
            "uuid": self.uuid,
            "created_at": self.created_at,
            "token_count": self.token_count,
        }

class Message:
    def __init__(
        self,
        role: str,
        content: str,
        uuid: Optional[str] = None,
        created_at: Optional[str] = None,
        token_count: Optional[int] = None,
    ):
        self.uuid = uuid
        self.created_at = created_at
        self.role = role
        self.content = content
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "role": self.role,
            "content": self.content,
            "token_count": self.token_count,
        }

class Summary:
    def __init__(
        self,
        uuid: str,
        created_at: str,
        content: str,
        recent_message_uuid: str,
        token_count: int,
    ):
        self.uuid = uuid
        self.created_at = created_at
        self.content = content
        self.recent_message_uuid = recent_message_uuid
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "content": self.content,
            "recent_message_uuid": self.recent_message_uuid,
            "token_count": self.token_count,
        }

class SearchPayload:
    def __init__(self, meta: Dict[str, Any], text: str):
        self.meta = meta
        self.text = text

class SearchResult:
    def __init__(
        self,
        message: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,  # Add the 'meta' argument with a default value
        score: Optional[float] = None,
        summary: Optional[str] = None,
        dist: Optional[float] = None,
    ):
        self.message = message
        self.meta = meta if meta is not None else {}  # Use the provided value or an empty dictionary
        self.score = score
        self.summary = summary
        self.dist = dist

class APIError:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message