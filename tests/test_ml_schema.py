from ml.schemas import StandardDetectionResult


def test_detection_schema_defaults():
    result = StandardDetectionResult()
    assert result.particle_count == 0
    assert result.confidence_mean == 0.0
    assert result.small_particle_ratio == 0.0
