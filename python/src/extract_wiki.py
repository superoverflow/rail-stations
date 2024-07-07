from html.parser import HTMLParser
from enum import StrEnum
from dataclasses import dataclass


@dataclass
class RailStation:
    name: str
    postcode: str | None = None
    nickname: str | None = None


class CaptureFlag(StrEnum):
    NAME = "fn n org"
    POSTCODE = "postal-code"
    NICKNAME = "nickname"


class WikiRailStationHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = None
        self.name_buffer = None
        self.nickname_buffer = None
        self.postcode_buffer = None
        self.result = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        kv = dict(attrs)
        if tag == "span":
            self.capture = kv.get("class")

    def handle_endtag(self, tag: str):
        if self.capture:
            self.capture = None

    def handle_data(self, data: str):
        if self.capture == CaptureFlag.NAME and self.name_buffer:
            self.flush_buffer()

        match self.capture:
            case CaptureFlag.NAME:
                self.name_buffer = data
            case CaptureFlag.POSTCODE:
                self.postcode_buffer = data
            case CaptureFlag.NICKNAME:
                self.nickname_buffer = data

    def flush_buffer(self):
        self.result.append(
            RailStation(
                name=self.name_buffer,
                postcode=self.postcode_buffer,
                nickname=self.nickname_buffer,
            )
        )
        self.name_buffer = None
        self.postcode_buffer = None
        self.nickname_buffer = None

    def feed(self, data: str) -> None:
        super().feed(data)
        self.flush_buffer()
