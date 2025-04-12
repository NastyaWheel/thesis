from pathlib import Path

STORAGE_DIR: Path = Path(__file__).resolve().parent / "storage"

script_dir = Path(__file__).resolve().parent
LOG_FILE = script_dir / "errors.log"

REQUEST_FILE_ID_URL: str = "http://stat.gibdd.ru/export/getCardsXML"

REQUEST_FILE_CONTENT_URL: str = "http://stat.gibdd.ru/getFileById?data="

REQUEST_HEADER: dict[str, str] = {
    "Content-type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
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
    22,
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
    44,
    45,
    46,
    47,
    49,
    50,
    52,
    53,
    54,
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

# REGIONS: list[int] = [30, 45, 46, 77, 90, 10011]