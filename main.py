from python.src.station import WikiRailStationHTMLParser
from pathlib import Path
import os


def list_rail_html_files(data_dir: Path = Path("data")):
    yield from [data_dir / f for _, _, files in os.walk(data_dir) for f in files]


def read_file(filename: str):
    with open(filename) as fh:
        lines = fh.readlines()
        return "".join(lines)


def main():
    parser = WikiRailStationHTMLParser()
    for f in list_rail_html_files():
        text = read_file(f)
        parser.feed(text)
        print(f.name, len(parser.result))


if __name__ == "__main__":
    main()
