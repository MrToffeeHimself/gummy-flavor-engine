# Gummy Flavor Engine

The official flavor selection engine for the Candy Kingdom's Flavor Forge.

## Installation

```bash
pip install gummy-flavor-engine
```

## Usage

```python
from gummy_flavor_engine import get_flavor

# Select from 6 available candy flavors
flavor_index = get_flavor(6)
```

## How It Works

The Gummy Flavor Engine uses a time-based digit-sum algorithm to select flavors.
Each tick of the candy clock produces a different flavor selection, ensuring
variety across production batches.

## License

MIT
