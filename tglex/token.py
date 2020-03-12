"""Token entities."""

import dataclasses


@dataclasses.dataclass(frozen=True)
class Token:
    """Token."""

    text: str
