"""Pure shortcut-selection logic for the Office Hotkeys plugin.

Stdlib-only and free of any InkyPi imports, so it is fast and safe to unit-test.
"""
import json
import time


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
