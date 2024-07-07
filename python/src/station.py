from html.parser import HTMLParser
from enum import StrEnum, auto
from dataclasses import dataclass
import re
from typing import Self


@dataclass
class RailStation:
    name: str
    postcode: str | None = None
    nickname: str | None = None


class CaptureSnippet:
    NAME = r"^/wiki/.*_railway_station$"
    POSTCODE = "https://www.bing.com/mapspreview"
    NICKNAME = "http://ojp.nationalrail.co.uk/service/ldbboard/dep/"


class CaptureFlag(StrEnum):
    NAME = auto()
    POSTCODE = auto()
    NICKNAME = auto()


class WikiRailStationHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.capture: CaptureFlag | None = None
        self.name_buffer: str | None = None
        self.nickname_buffer: str | None = None
        self.postcode_buffer: str | None = None
        self.result: list[RailStation] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        kv = dict(attrs)
        if tag != "a":
            return
        href = kv.get("href") or ""
        if re.match(CaptureSnippet.NAME, href):
            self.capture = CaptureFlag.NAME
        if href.startswith(CaptureSnippet.POSTCODE):
            self.capture = CaptureFlag.POSTCODE
        if href.startswith(CaptureSnippet.NICKNAME):
            self.capture = CaptureFlag.NICKNAME

    def handle_endtag(self, tag: str) -> None:
        if self.capture:
            self.capture = None

    def handle_data(self, data: str) -> None:
        if self.capture == CaptureFlag.NAME:
            self.flush_buffer()

        match self.capture:
            case CaptureFlag.NAME:
                self.name_buffer = data
            case CaptureFlag.POSTCODE:
                self.postcode_buffer = data
            case CaptureFlag.NICKNAME:
                self.nickname_buffer = data

    def flush_buffer(self) -> None:
        if self.name_buffer:
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
