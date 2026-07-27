from dataclasses import dataclass, field
from enum import Enum


# An Enum makes a field exactly ONE of a fixed set of values.
class StayKind(str, Enum):
    HOTEL = "hotel"
    APARTMENT = "apartment"
    HOSTEL = "hostel"
    VILLA = "villa"


# A dataclass is a typed record: named fields, each with a type.
@dataclass
class Listing:
    id: str
    city: str
    kind: StayKind
    price_per_night: float  # USD
    rating: float           # 0..5
    tags: list[str]         # e.g. ["beach", "wifi", "pet-friendly"]
    # Optional fields MUST follow the required ones and carry a default.
    reviews: int = 0                       # how many ratings back the score
    distance_km: float | None = None       # km from city center, if known
    amenities: list[str] = field(default_factory=list)

    # A computed property: derived, not stored. Reads like a field.
    @property
    def is_rated(self) -> bool:
        """A rating is only trustworthy once a few people have left one."""
        return self.reviews >= 5


# A function with typed parameters and a typed return value.
def nightly_total(listing: Listing, nights: int) -> float:
    return listing.price_per_night * nights
