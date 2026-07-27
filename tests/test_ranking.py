from app.models import Listing, StayKind
from app.filtering import within_budget, candidates, score
from app.ranking import recommend


def _listing(id: str, price: float, rating: float, tags: list[str]) -> Listing:
    """A tiny factory so each test reads clearly."""
    return Listing(id, "Lisbon", StayKind.HOTEL, price, rating, tags)


def test_within_budget_boundary() -> None:
    cheap = _listing("a", 100.0, 4.0, [])
    assert within_budget(cheap, 100.0) is True     # at the ceiling: included
    assert within_budget(cheap, 99.0) is False      # one dollar over: excluded


def test_candidates_filters_price_and_kind() -> None:
    pool = [_listing("a", 100.0, 4.0, []), _listing("b", 500.0, 5.0, [])]
    kept = candidates(pool, max_price=200.0)
    assert [l.id for l in kept] == ["a"]            # the $500 one is filtered out


def test_score_rewards_tag_overlap() -> None:
    base = _listing("a", 100.0, 4.0, ["beach"])
    plain = _listing("b", 100.0, 4.0, [])
    assert score(base, {"beach"}) > score(plain, {"beach"})


def test_recommend_orders_best_first_and_limits() -> None:
    pool = [
        _listing("low", 100.0, 3.0, []),
        _listing("high", 100.0, 5.0, ["beach"]),
        _listing("mid", 100.0, 4.0, []),
    ]
    out = recommend(pool, max_price=200.0, liked_tags={"beach"}, limit=2)
    assert [l.id for l in out] == ["high", "mid"]   # best two, in order
