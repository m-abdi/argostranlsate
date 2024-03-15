from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("text", "from_lang", "to_lang")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FROM_LANG_FIELD_NUMBER: _ClassVar[int]
    TO_LANG_FIELD_NUMBER: _ClassVar[int]
    text: str
    from_lang: str
    to_lang: str
    def __init__(
        self,
        text: _Optional[str] = ...,
        from_lang: _Optional[str] = ...,
        to_lang: _Optional[str] = ...,
    ) -> None: ...

class Result(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
