from typing import Any
import requests
from dataclasses import dataclass


@dataclass
class LatLon:
    longitude: float
    latitude: float


class PostcodeInfoProvider:
    def __init__(self, base_url: str | None = None) -> None:
        self.base_url = base_url or "https://api.postcodes.io/"

    def lookup_bulk_postcodes(self, postcodes: list[str]) -> dict[str, LatLon]:
        url = self.base_url + "postcodes"
        data = dict(postcodes=postcodes)
        resp_json = requests.post(url, data=data).json()
        result = dict(
            PostcodeInfoProvider.unpack_result(r) for r in resp_json["result"]
        )

        return result

    def lookup_single_postcode(self, postcode: str) -> LatLon:
        url = self.base_url + "postcodes/" + postcode.replace(" ", "")
        resp_json = requests.get(url).json()
        _, result = PostcodeInfoProvider.unpack_result(resp_json)
        return result

    @staticmethod
    def unpack_result(raw: dict[str, Any]) -> tuple[str, LatLon]:
        raw_result = raw["result"]
        return (
            raw_result["postcode"],
            LatLon(longitude=raw_result["longitude"], latitude=raw_result["latitude"]),
        )


if __name__ == "__main__":
    resp1 = PostcodeInfoProvider().lookup_bulk_postcodes(
        ["PR3 0SG", "M45 6GN", "EX165BL"]
    )
    resp2 = PostcodeInfoProvider().lookup_single_postcode("E16 1YE")
    pass
