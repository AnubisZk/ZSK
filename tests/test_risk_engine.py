from risk_engine.scoring import RiskScoringEngine


def test_risk_engine_returns_expected_fields():
    engine = RiskScoringEngine()
    result = engine.calculate(
        particle_count=25,
        small_particle_ratio=0.4,
        density_score=0.2,
        water_type="river_water",
        temperature=24,
        rainfall=20,
        uv_index=7,
        season="summer",
    )

    assert "risk_score" in result
    assert "risk_level" in result
    assert "recommendation" in result
    assert 0 <= result["risk_score"] <= 100
