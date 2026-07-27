import argparse
import sys

from app.sample_data import SAMPLE
from app.ranking import recommend
from app.validation import validate_request, parse_tags


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rank travel stays for a traveler.")
    parser.add_argument("--max-price", type=float, default=250.0)
    parser.add_argument("--tags", default="", help="comma-separated liked tags")
    parser.add_argument("--kind", default=None, help="hotel|apartment|hostel|villa")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args(argv)

    try:
        kind = validate_request(args.max_price, args.limit, args.kind)
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2                                  # non-zero: signal failure to the shell

    picks = recommend(
        SAMPLE,
        max_price=args.max_price,
        liked_tags=parse_tags(args.tags),
        kind=kind,
        limit=args.limit,
    )
    for rank, listing in enumerate(picks, start=1):
        print(f"{rank}. {listing.id} {listing.kind.value} ${listing.price_per_night:.0f}")
    return 0                                       # zero: success


if __name__ == "__main__":
    raise SystemExit(main())
