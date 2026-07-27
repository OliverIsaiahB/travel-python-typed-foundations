from app.models import StayKind


def validate_request(max_price: float, limit: int, kind: str | None) -> StayKind | None:
    """Check inputs up front; raise a clear error rather than silently misbehave."""
    if max_price <= 0:
        raise ValueError(f"max_price must be positive, got {max_price}")
    if limit < 1:
        raise ValueError(f"limit must be at least 1, got {limit}")
    if kind is None:
        return None
    try:
        return StayKind(kind)            # "hotel" -> StayKind.HOTEL, or ValueError
    except ValueError:
        valid = ", ".join(k.value for k in StayKind)
        raise ValueError(f"unknown kind {kind!r}; expected one of: {valid}")
