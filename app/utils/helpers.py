from decimal import Decimal


def safe_pct(achieved: Decimal, target: Decimal) -> float:
    """Calculate achievement percentage safely, avoiding division by zero."""
    if not target:
        return 0.0
    return round(float(achieved) / float(target) * 100, 2)
