from python.src.postcode import PostcodeInfoProvider, LatLon
import pytest


def make_postcode_response(postcode: str, longitude: float, latitude: float):
    return {
        "query": postcode,
        "result": {
            "postcode": postcode,
            "quality": 1,
            "eastings": 351012,
            "northings": 440302,
            "country": "England",
            "nhs_ha": "North West",
            "longitude": longitude,
            "latitude": latitude,
            "european_electoral_region": "North West",
            "primary_care_trust": "North Lancashire Teaching",
            "region": "North West",
            "lsoa": "Wyre 006A",
            "msoa": "Wyre 006",
            "incode": "0SG",
            "outcode": "PR3",
            "parliamentary_constituency": "Wyre and Preston North",
            "parliamentary_constituency_2024": "Lancaster and Wyre",
            "admin_district": "Wyre",
            "parish": "Myerscough and Bilsborrow",
            "admin_county": "Lancashire",
            "date_of_introduction": "200705",
            "admin_ward": "Brock with Catterall",
            "ced": "Wyre Rural East",
            "ccg": "NHS Lancashire and South Cumbria",
            "nuts": "Wyre",
            "pfa": "Lancashire",
            "codes": {
                "admin_district": "E07000128",
                "admin_county": "E10000017",
                "admin_ward": "E05009934",
                "parish": "E04005340",
                "parliamentary_constituency": "E14001057",
                "parliamentary_constituency_2024": "E14001318",
                "ccg": "E38000226",
                "ccg_id": "02M",
                "ced": "E58000832",
                "nuts": "TLD44",
                "lsoa": "E01025547",
                "msoa": "E02005324",
                "lau2": "E07000128",
                "pfa": "E23000003",
            },
        },
    }


@pytest.fixture
def mock_multiple_postcode_response():
    return {
        "status": 200,
        "result": [
            {
                "query": "OX49 5NU",
                "result": {
                    "postcode": "OX49 5NU",
                    "quality": 1,
                    "eastings": 464438,
                    "northings": 195677,
                    "country": "England",
                    "nhs_ha": "South Central",
                    "longitude": -1.069752,
                    "latitude": 51.655929,
                    "european_electoral_region": "South East",
                    "primary_care_trust": "Oxfordshire",
                    "region": "South East",
                    "lsoa": "South Oxfordshire 011B",
                    "msoa": "South Oxfordshire 011",
                    "incode": "5NU",
                    "outcode": "OX49",
                    "parliamentary_constituency": "Henley",
                    "parliamentary_constituency_2024": "Henley and Thame",
                    "admin_district": "South Oxfordshire",
                    "parish": "Brightwell Baldwin",
                    "admin_county": "Oxfordshire",
                    "date_of_introduction": "200010",
                    "admin_ward": "Chalgrove",
                    "ced": "Chalgrove and Watlington",
                    "ccg": "NHS Buckinghamshire, Oxfordshire and Berkshire West",
                    "nuts": "South Oxfordshire",
                    "pfa": "Thames Valley",
                    "codes": {
                        "admin_district": "E07000179",
                        "admin_county": "E10000025",
                        "admin_ward": "E05009735",
                        "parish": "E04008109",
                        "parliamentary_constituency": "E14000742",
                        "parliamentary_constituency_2024": "E14001280",
                        "ccg": "E38000136",
                        "ccg_id": "10Q",
                        "ced": "E58001732",
                        "nuts": "TLJ14",
                        "lsoa": "E01028601",
                        "msoa": "E02005968",
                        "lau2": "E07000179",
                        "pfa": "E23000029",
                    },
                },
            },
            {
                "query": "M32 0JG",
                "result": {
                    "postcode": "M32 0JG",
                    "quality": 1,
                    "eastings": 379988,
                    "northings": 395476,
                    "country": "England",
                    "nhs_ha": "North West",
                    "longitude": -2.302836,
                    "latitude": 53.455654,
                    "european_electoral_region": "North West",
                    "primary_care_trust": "Trafford",
                    "region": "North West",
                    "lsoa": "Trafford 003C",
                    "msoa": "Trafford 003",
                    "incode": "0JG",
                    "outcode": "M32",
                    "parliamentary_constituency": "Stretford and Urmston",
                    "parliamentary_constituency_2024": "Stretford and Urmston",
                    "admin_district": "Trafford",
                    "parish": "Trafford, unparished area",
                    "admin_county": None,
                    "date_of_introduction": "198001",
                    "admin_ward": "Gorse Hill & Cornbrook",
                    "ced": None,
                    "ccg": "NHS Greater Manchester",
                    "nuts": "Trafford",
                    "pfa": "Greater Manchester",
                    "codes": {
                        "admin_district": "E08000009",
                        "admin_county": "E99999999",
                        "admin_ward": "E05015247",
                        "parish": "E43000163",
                        "parliamentary_constituency": "E14000979",
                        "parliamentary_constituency_2024": "E14001528",
                        "ccg": "E38000187",
                        "ccg_id": "02A",
                        "ced": "E99999999",
                        "nuts": "TLD34",
                        "lsoa": "E01006187",
                        "msoa": "E02001261",
                        "lau2": "E08000009",
                        "pfa": "E23000005",
                    },
                },
            },
            {
                "query": "NE30 1DP",
                "result": {
                    "postcode": "NE30 1DP",
                    "quality": 1,
                    "eastings": 435958,
                    "northings": 568671,
                    "country": "England",
                    "nhs_ha": "North East",
                    "longitude": -1.439269,
                    "latitude": 55.011303,
                    "european_electoral_region": "North East",
                    "primary_care_trust": "North Tyneside",
                    "region": "North East",
                    "lsoa": "North Tyneside 016C",
                    "msoa": "North Tyneside 016",
                    "incode": "1DP",
                    "outcode": "NE30",
                    "parliamentary_constituency": "Tynemouth",
                    "parliamentary_constituency_2024": "Tynemouth",
                    "admin_district": "North Tyneside",
                    "parish": "North Tyneside, unparished area",
                    "admin_county": None,
                    "date_of_introduction": "201303",
                    "admin_ward": "Tynemouth",
                    "ced": None,
                    "ccg": "NHS North East and North Cumbria",
                    "nuts": "North Tyneside",
                    "pfa": "Northumbria",
                    "codes": {
                        "admin_district": "E08000022",
                        "admin_county": "E99999999",
                        "admin_ward": "E05001130",
                        "parish": "E43000176",
                        "parliamentary_constituency": "E14001006",
                        "parliamentary_constituency_2024": "E14001557",
                        "ccg": "E38000127",
                        "ccg_id": "99C",
                        "ced": "E99999999",
                        "nuts": "TLC22",
                        "lsoa": "E01008561",
                        "msoa": "E02001753",
                        "lau2": "E08000022",
                        "pfa": "E23000007",
                    },
                },
            },
        ],
    }


@pytest.fixture
def mock_single_postcode_response():
    postcode = "AB11 0XY"
    longitude = -0.1234
    latitude = 55.1234
    mock_response = make_postcode_response(postcode, longitude, latitude)
    return mock_response


def test_lookup_single_postcode_base(requests_mock, mock_single_postcode_response):
    requests_mock.get(
        "https://api.postcodes.io/postcodes/AB110XY",
        json=mock_single_postcode_response,
    )
    result = PostcodeInfoProvider().lookup_single_postcode("AB11 0XY")
    assert result == LatLon(longitude=-0.1234, latitude=55.1234)


def test_lookup_bulk_postcodes_base(requests_mock, mock_multiple_postcode_response):
    requests_mock.post(
        "https://api.postcodes.io/postcodes",
        json=mock_multiple_postcode_response,
    )
    result = PostcodeInfoProvider().lookup_bulk_postcodes(
        ["OX49 5NU", "M32 0JG", "NE30 1DP"]
    )
    assert result == {
        "M32 0JG": LatLon(longitude=-2.302836, latitude=53.455654),
        "NE30 1DP": LatLon(longitude=-1.439269, latitude=55.011303),
        "OX49 5NU": LatLon(longitude=-1.069752, latitude=51.655929),
    }
