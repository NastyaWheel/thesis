from pathlib import Path

STORAGE_DIR: Path = Path("storage")

REQUEST_FILE_ID_URL: str = "http://stat.gibdd.ru/export/getCardsXML"

REQUEST_FILE_CONTENT_URL: str = "http://stat.gibdd.ru/getFileById?data="

REQUEST_HEADER: dict[str, str] = {
    "Content-type": "application/json; charset=UTF-8"
}

INTERNAL_FILENAME: str = "Карточки ДТП.xml"

REGIONS: list[int] = [
    1,
    3,
    4,
    5,
    7,
    8,
    10,
    11,
    12,
    14,
    15,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    49,
    50,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    60,
    61,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    71100,
    71140,
    10011,
]