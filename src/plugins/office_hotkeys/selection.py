"""Pure shortcut-selection logic for the Office Hotkeys plugin.

No InkyPi render-stack imports — depends only on stdlib and the local
constants module (itself stdlib-only), so it is fast and safe to unit-test.
"""
import json
import time

from . import constants


def load_shortcuts(data_path):
    """Load and return the list of shortcut dicts from a JSON file."""
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


def pick_category(categories, now=None):
    """Return the category for the current hour, rotating sequentially.

    Stateless: the index is derived from the wall clock, so the active
    category advances one step per hour with no persisted state.
    """
    if not categories:
        return None
    if now is None:
        now = time.time()
    index = int(now // 3600) % len(categories)
    return categories[index]


def filter_by_level(shortcuts, min_level):
    """Keep only shortcuts at `min_level` or harder (a difficulty floor)."""
    floor = constants.LEVELS.index(min_level)
    return [s for s in shortcuts
            if constants.LEVELS.index(s["level"]) >= floor]
