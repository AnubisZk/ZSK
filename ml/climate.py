from dataclasses import dataclass


@dataclass
class ClimateDataClient:
    mode: str = "mock"

    def fetch_and_normalize(self) -> dict:
        raw = self._fetch_mock() if self.mode == "mock" else self._fetch_real_placeholder()
        return self._normalize(raw)

    def _fetch_mock(self) -> dict:
        return {
            "temperature": 23.4,
            "rainfall": 12.0,
            "uv_index": 6.5,
            "season": "spring",
            "source": "mock",
        }

    def _fetch_real_placeholder(self) -> dict:
        return {
            "temperature": 20.0,
            "rainfall": 0.0,
            "uv_index": 5.0,
            "season": "unknown",
            "source": "api",
        }

    @staticmethod
    def _normalize(payload: dict) -> dict:
        return {
            "temperature": float(payload.get("temperature", 0.0)),
            "rainfall": max(float(payload.get("rainfall", 0.0)), 0.0),
            "uv_index": max(float(payload.get("uv_index", 0.0)), 0.0),
            "season": str(payload.get("season", "unknown")).lower(),
            "source": payload.get("source", "unknown"),
        }
