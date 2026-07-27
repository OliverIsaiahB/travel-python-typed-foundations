from app.models import StayKind
from app.sample_data import SAMPLE
from app.ranking import recommend


def main() -> None:
    """Run one recommendation for a beach-loving, budget-aware traveler."""
    picks = recommend(
        SAMPLE,
        max_price=250.0,
        liked_tags={"beach", "wifi"},
        limit=3,
    )
    print("Top stays in Lisbon under $250:\n")
    for rank, listing in enumerate(picks, start=1):
        flag = "" if listing.is_rated else "  (few reviews)"
        print(
            f"{rank}. {listing.kind.value:<9} ${listing.price_per_night:>6.0f}"
            f"  {listing.rating}★  {','.join(listing.tags)}{flag}"
        )


# Only runs when this file is executed directly, not when imported.
if __name__ == "__main__":
    main()
