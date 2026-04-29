from dataclasses import dataclass, field

from risk_engine.water_types import get_water_type_factor


@dataclass
class RiskWeights:
    particle_count_weight: float = 0.20
    small_particle_weight: float = 0.20
    density_weight: float = 0.25
    climate_weight: float = 0.25
    season_weight: float = 0.10


@dataclass
class RiskScoringEngine:
    weights: RiskWeights = field(default_factory=RiskWeights)

    def calculate(
        self,
        *,
        particle_count: int,
        small_particle_ratio: float,
        density_score: float,
        water_type: str,
        temperature: float,
        rainfall: float,
        uv_index: float,
        season: str,
    ) -> dict:
        particle_component = min(particle_count / 100, 1.0)
        small_component = max(min(small_particle_ratio, 1.0), 0.0)
        density_component = min(density_score, 1.0)

        climate_component = min(
            (max(temperature, 0) / 40) * 0.4
            + (max(rainfall, 0) / 200) * 0.3
            + (max(uv_index, 0) / 12) * 0.3,
            1.0,
        )

        season_map = {"spring": 0.6, "summer": 1.0, "autumn": 0.7, "winter": 0.5}
        season_component = season_map.get(season.lower(), 0.6)

        weighted_base = (
            particle_component * self.weights.particle_count_weight
            + small_component * self.weights.small_particle_weight
            + density_component * self.weights.density_weight
            + climate_component * self.weights.climate_weight
            + season_component * self.weights.season_weight
        )

        water_factor = get_water_type_factor(water_type)
        risk_score = max(min(weighted_base * 100 * water_factor, 100), 0)

        risk_level = self._level_from_score(risk_score)
        recommendation = self._recommendation(risk_level)

        return {
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "recommendation": recommendation,
            "inputs": {
                "particle_count": particle_count,
                "small_particle_ratio": small_particle_ratio,
                "density_score": density_score,
                "water_type": water_type,
                "temperature": temperature,
                "rainfall": rainfall,
                "uv_index": uv_index,
                "season": season,
                "water_type_factor": water_factor,
            },
        }

    @staticmethod
    def _level_from_score(score: float) -> str:
        if score < 35:
            return "low"
        if score < 70:
            return "medium"
        return "high"

    @staticmethod
    def _recommendation(level: str) -> str:
        if level == "low":
            return "Routine monitoring is sufficient."
        if level == "medium":
            return "Increase sampling frequency and apply mitigation checks."
        return "Immediate intervention and detailed laboratory analysis recommended."
