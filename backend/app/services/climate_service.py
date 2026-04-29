from ml.climate import ClimateDataClient


_client = ClimateDataClient(mode="mock")


def get_climate_data() -> dict:
    return _client.fetch_and_normalize()
