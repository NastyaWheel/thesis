import calendar
import io
import json
import os
import shutil
import zipfile
from datetime import date, datetime
from pathlib import Path

import requests
from requests import Response

from settings import REGIONS, REQUEST_FILE_ID_URL, REQUEST_HEADER, REQUEST_FILE_CONTENT_URL, INTERNAL_FILENAME, \
    STORAGE_DIR


def main() -> None:
    for region in REGIONS:
        for year in range(2015, datetime.today().year + 1):
            for month in range(1, 13):
                _, last_day = calendar.monthrange(year, month)      # find the last day of the month for the given year and month
                date_start: date = date(year, month, 1)
                date_end: date = date(year, month, last_day)
                date_start_fmt: str = date_start.strftime("%d.%m.%Y")           # convert date object to string with the specified format
                date_end_fmt: str = date_end.strftime("%d.%m.%Y")               # ex: datetime(2024, 7, 21) -> 21.07.2024

                # data preparation before sending an HTTP request (POST request)

                request_payload: any = {
                    "date_st": date_start_fmt,
                    "date_end": date_end_fmt,
                    "ParReg": "877",
                    "order": {
                        "type": 1,
                        "fieldName": "dat"
                    },
                    "reg": [str(region)],
                    "ind": "1",
                    "exportType": 1
                }

                request_data: dict[str, str] = {
                    "data": json.dumps(request_payload)
                }


                # perform an HTTP POST request to obtain the file identifier
                print(f"Requesting file ID for {date_start_fmt} - {date_end_fmt} interval with region {region}")
                response: Response = requests.post(
                    REQUEST_FILE_ID_URL,
                    data=json.dumps(request_data),
                    headers=REQUEST_HEADER,
                    timeout=10
                )
                if response.status_code != 200:         # status code 200 indicates success
                    print(f"Error in request file ID\n"
                          f"Status code: {response.status_code}")
                    continue

                response_data: any = response.json()
                response_file_id: str = response_data["data"]
                if not response_file_id:
                    print("Error! File ID not found in response")
                    continue

                # make an HTTP GET request to the URL formed by concatenating REQUEST_FILE_CONTENT_URL and response_file_id
                response = requests.get(f"{REQUEST_FILE_CONTENT_URL}{response_file_id}", timeout=10)
                if response.status_code != 200:
                    print(f"Error in request file content for {response_file_id} ID\n"
                          f"Status code: {response.status_code}")
                    continue

                zip_data: bytes = response.content          # contains the response payload as bytes
                with zipfile.ZipFile(io.BytesIO(zip_data)) as zipfile_fd:
                    zipfile_fd.extract(INTERNAL_FILENAME)

                if not os.path.exists(STORAGE_DIR):
                    os.mkdir(STORAGE_DIR)
                shutil.move(
                    Path(INTERNAL_FILENAME), Path(STORAGE_DIR / f"ДТП_{region}_{date_start.strftime('%Y_%m.xml')}")
                )


if __name__ == '__main__':
    main()