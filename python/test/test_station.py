import pytest

from python.src.station import WikiRailStationHTMLParser, RailStation


@pytest.fixture
def mock_data_A():
    return """
        <tr class="vcard">
        <td><span class="fn n org"><a href="/wiki/Ansdell_%26_Fairhaven_railway_station" class="mw-redirect" title="Ansdell &amp; Fairhaven railway station">Ansdell &amp; Fairhaven</a></span></td>
        <td><span class="adr"><span class="postal-code"><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=FY8%201AE,GB">FY8 1AE</a></span></span></td>
        <td><span class="nickname"><a rel="nofollow" class="external text" href="http://ojp.nationalrail.co.uk/service/ldbboard/dep/AFV">AFV</a></span></td>
        <td><a rel="nofollow" class="external text" href="http://www.nationalrail.co.uk/stations/AFV/details.html">AFV</a>
        </td></tr>
        <tr class="vcard">
        <td><span class="fn n org"><a href="/wiki/Antrim_railway_station" title="Antrim railway station">Antrim</a></span></td>
        <td><span class="adr"><span class="postal-code"><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=BT41%204AB,GB">BT41 4AB</a></span></span></td>
        <td></td>
        <td>
        </td></tr>
        <tr class="vcard">
        <td><span class="fn n org"><a href="/wiki/Apperley_Bridge_railway_station" title="Apperley Bridge railway station">Apperley Bridge</a></span></td>
        <td><span class="adr"><span class="postal-code"><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=BD10%200FD,GB">BD10 0FD</a></span></span></td>
        <td><span class="nickname"><a rel="nofollow" class="external text" href="http://ojp.nationalrail.co.uk/service/ldbboard/dep/APY">APY</a></span></td>
        <td><a rel="nofollow" class="external text" href="http://www.nationalrail.co.uk/stations/APY/details.html">APY</a>
        </td></tr>
    """


@pytest.fixture
def mock_data_B():
    return """
    <tr>
    <td><a href="/wiki/Welwyn_Garden_City_railway_station" title="Welwyn Garden City railway station">Welwyn Garden City</a></td>
    <td><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=AL8%206BE,GB">AL8 6BE</a></td>
    <td><a rel="nofollow" class="external text" href="http://ojp.nationalrail.co.uk/service/ldbboard/dep/WGC">WGC</a>
    </td></tr>
    <tr>
    <td><a href="/wiki/Welwyn_North_railway_station" title="Welwyn North railway station">Welwyn North</a></td>
    <td><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=AL6%200EA,GB">AL6 0EA</a></td>
    <td><a rel="nofollow" class="external text" href="http://ojp.nationalrail.co.uk/service/ldbboard/dep/WLW">WLW</a>
    </td></tr>
    <tr>
    <td><a href="/wiki/Wem_railway_station" title="Wem railway station">Wem</a></td>
    <td><a rel="nofollow" class="external text" href="https://www.bing.com/mapspreview?where1=SY4%205AZ,GB">SY4 5AZ</a></td>
    <td><a rel="nofollow" class="external text" href="http://ojp.nationalrail.co.uk/service/ldbboard/dep/WEM">WEM</a>
    </td></tr>

    """


def test_wiki_rail_station_parser_variant_1(mock_data_A):
    parser = WikiRailStationHTMLParser()
    parser.feed(mock_data_A)

    assert parser.result == [
        RailStation(name="Ansdell & Fairhaven", postcode="FY8 1AE", nickname="AFV"),
        RailStation(name="Antrim", postcode="BT41 4AB"),
        RailStation(name="Apperley Bridge", postcode="BD10 0FD", nickname="APY"),
    ]


def test_wiki_rail_station_parser_variant_2(mock_data_B):
    parser = WikiRailStationHTMLParser()
    parser.feed(mock_data_B)

    assert parser.result == [
        RailStation(name="Welwyn Garden City", postcode="AL8 6BE", nickname="WGC"),
        RailStation(name="Welwyn North", postcode="AL6 0EA", nickname="WLW"),
        RailStation(name="Wem", postcode="SY4 5AZ", nickname="WEM"),
    ]
