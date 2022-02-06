import os
from pydexcom import Dexcom


if __name__ == '__main__':
    dexcom_client = Dexcom(
        username=os.environ['DEXCOM_USERNAME'],
        password=os.environ['DEXCOM_PASSWORD'],
        ous=True
    )

    last_reading = dexcom_client.get_latest_glucose_reading()

    print(last_reading)
