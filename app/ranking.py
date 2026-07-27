from app.models import Listing, StayKind
from app.filtering import candidates, score


# Rank a catalog for one traveler: filter, then sort by score (best first).
def recommend(
    listings: list[Listing],
    max_price: float,
    liked_tags: set[str],
    kind: StayKind | None = None,
    limit: int = 5,
) -> list[Listing]:
    pool = candidates(listings, max_price, kind)
    ranked = sorted(pool, key=lambda l: score(l, liked_tags), reverse=True)
    return ranked[:limit]
