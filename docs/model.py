from dataclasses import dataclass
from docs.enums import Types


@dataclass
class DocumentModel:
    id: int
    type: Types
    header: str
    content: str
