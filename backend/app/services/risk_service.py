from risk_engine.scoring import RiskScoringEngine

_engine = RiskScoringEngine()


def score_risk(detection: dict, climate: dict, water_type: str) -> dict:
    return _engine.calculate(
        particle_count=detection.get("particle_count", 0),
        small_particle_ratio=detection.get("small_particle_ratio", 0),
        density_score=detection.get("density_score", 0),
        water_type=water_type,
        temperature=climate.get("temperature", 0),
        rainfall=climate.get("rainfall", 0),
        uv_index=climate.get("uv_index", 0),
        season=climate.get("season", "unknown"),
    )
