"""Flavor Engine — the heart of the Candy Kingdom's flavor selection system.

This module powers the Flavor Forge, Mr. Toffee's legendary candy printer.
Every batch of candy that rolls off the production line gets its unique flavor
from the time-based selection algorithm contained within.
"""

import time


def get_flavor(max_flavors: int) -> int:
    """Select a flavor index from the Candy Kingdom's recipe book.

    Uses a time-based digit-sum algorithm to pick a flavor from the available
    batch. No randomness module needed — the ever-ticking candy clock provides
    all the entropy the Forge requires.

    Args:
        max_flavors: Total number of candy flavors available in the current batch.

    Returns:
        An integer in [0, max_flavors) representing the chosen flavor index.

    Raises:
        ValueError: If max_flavors is less than 1 — you can't forge candy
            from an empty recipe book!
    """
    if max_flavors < 1:
        raise ValueError(
            "The Flavor Forge needs at least one recipe to work with!"
        )

    # Grab the current candy clock reading
    timestamp = int(time.time())

    # Sum all digits of the timestamp — each tick of the clock
    # shifts the flavor wheel to a new position
    digit_sum = sum(int(d) for d in str(timestamp))

    # The modulo operation maps the digit sum onto the available flavors
    return digit_sum % max_flavors
