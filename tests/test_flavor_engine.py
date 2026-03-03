"""Tests for the Gummy Flavor Engine.

Every candy batch must pass quality control before leaving the Forge.
"""

import time
from unittest.mock import patch

import pytest

from gummy_flavor_engine import get_flavor


class TestFlavorForgeQualityControl:
    """Quality control suite for the Flavor Forge's selection engine."""

    def test_flavor_is_within_batch_range(self):
        """Ensure the selected flavor is always within the recipe book."""
        for batch_size in [1, 3, 6, 10, 100]:
            result = get_flavor(batch_size)
            assert 0 <= result < batch_size, (
                f"Flavor index {result} fell outside batch of {batch_size} recipes!"
            )

    def test_single_flavor_batch_always_returns_zero(self):
        """A batch with one flavor has no choice — it's always index 0."""
        assert get_flavor(1) == 0

    def test_empty_recipe_book_raises_error(self):
        """The Forge refuses to operate without at least one recipe."""
        with pytest.raises(ValueError, match="at least one recipe"):
            get_flavor(0)

    def test_negative_batch_size_raises_error(self):
        """Negative recipes? Mr. Toffee would never allow it."""
        with pytest.raises(ValueError):
            get_flavor(-5)

    @patch("gummy_flavor_engine.flavor_engine.time.time", return_value=1700000000.0)
    def test_deterministic_at_fixed_timestamp(self, mock_time):
        """At a fixed candy clock reading, the flavor must be predictable.

        timestamp = 1700000000
        digit sum = 1+7+0+0+0+0+0+0+0+0 = 8
        8 % 6 = 2
        """
        assert get_flavor(6) == 2

    @patch("gummy_flavor_engine.flavor_engine.time.time", return_value=1234567890.0)
    def test_digit_sum_calculation(self, mock_time):
        """Verify the digit-sum candy formula with a known timestamp.

        timestamp = 1234567890
        digit sum = 1+2+3+4+5+6+7+8+9+0 = 45
        45 % 10 = 5
        """
        assert get_flavor(10) == 5

    def test_flavor_returns_integer(self):
        """The Forge control system expects integer flavor indices."""
        result = get_flavor(6)
        assert isinstance(result, int)
