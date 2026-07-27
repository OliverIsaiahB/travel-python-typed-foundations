from app.models import Listing, StayKind

# A handful of listings to exercise the pipeline without a database yet.
SAMPLE: list[Listing] = [
    Listing("l1", "Lisbon", StayKind.VILLA, 380.0, 4.8,
            ["beach", "pool", "wifi"], reviews=210, distance_km=6.2),
    Listing("l2", "Lisbon", StayKind.HOSTEL, 42.0, 4.1,
            ["beach", "social", "wifi"], reviews=98, distance_km=1.1),
    Listing("l3", "Lisbon", StayKind.APARTMENT, 130.0, 4.5,
            ["kitchen", "wifi", "central"], reviews=64, distance_km=0.6),
    Listing("l4", "Lisbon", StayKind.HOTEL, 220.0, 4.6,
            ["central", "wifi", "gym"], reviews=512, distance_km=0.9),
    Listing("l5", "Lisbon", StayKind.HOTEL, 95.0, 3.9,
            ["central", "wifi"], reviews=3),  # too few reviews to trust
]
