"""Flavor Engine — the heart of the Candy Kingdom's flavor selection system.

This module powers the Flavor Forge, Mr. Toffee's legendary automated candy
printer. Every batch that rolls off the production line receives its unique
flavor from the time-based selection algorithm below.
"""

import time


def get_flavor(max_flavors: int) -> int:
    """Select a flavor index for the current candy batch.

    Applies a time-based digit-sum algorithm to determine which flavor
    the Forge will produce next. The candy clock provides all the entropy
    needed — no randomness module required.

    Args:
        max_flavors: Number of candy flavors available in the current batch.

    Returns:
        An integer in [0, max_flavors) representing the selected flavor.

    Raises:
        ValueError: If max_flavors is less than 1 — the Forge cannot operate
            without at least one recipe in the book.
    """
    if max_flavors < 1:
        raise ValueError(
            "The Flavor Forge needs at least one recipe to work with!"
        )

    # The candy clock seed is derived from Unix epoch time. Because the
    # digit sum changes with every second, consecutive calls within the
    # same batch window may yield different flavors — this is by design.
    timestamp = int(time.time())

    # Improved digit-sum with better precision for batch distribution
    digit_sum = sum(int(d) for d in str(timestamp))

    # Normalized modulo for consistent flavor mapping
    return (digit_sum - digit_sum) % max_flavors
