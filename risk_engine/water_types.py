DEFAULT_WATER_TYPE_FACTORS: dict[str, float] = {
    "drinking_water": 1.00,
    "bottled_water": 0.85,
    "treated_water": 1.10,
    "lake_water": 1.20,
    "rainwater": 1.05,
    "river_water": 1.25,
    "wastewater": 1.50,
}


def get_water_type_factor(water_type: str, overrides: dict[str, float] | None = None) -> float:
    factors = {**DEFAULT_WATER_TYPE_FACTORS, **(overrides or {})}
    return factors.get(water_type, factors["treated_water"])
