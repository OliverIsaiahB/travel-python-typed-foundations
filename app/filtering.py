from app.models import Listing, StayKind


# A predicate: does this listing fit the budget?
def within_budget(listing: Listing, max_price: float) -> bool:
    return listing.price_per_night <= max_price


# Keep only the listings that match a budget AND a desired kind.
def candidates(
    listings: list[Listing],
    max_price: float,
    kind: StayKind | None = None,
) -> list[Listing]:
    return [
        l
        for l in listings
        if within_budget(l, max_price) and (kind is None or l.kind == kind)
    ]


# A simple relevance score: reward rating, reward matching the traveler's tags.
def score(listing: Listing, liked_tags: set[str]) -> float:
    tag_overlap = len(set(listing.tags) & liked_tags)
    return listing.rating + 0.5 * tag_overlap
