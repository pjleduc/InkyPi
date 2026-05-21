from src.plugins.office_hotkeys import constants
from src.plugins.office_hotkeys import selection


def test_levels_are_ordered_easy_to_hard():
    assert constants.LEVELS == ["beginner", "intermediate", "advanced"]


def test_every_app_has_categories_and_a_theme():
    assert set(constants.CATEGORY_ORDER) == {"excel", "outlook", "powerpoint"}
    for app, cats in constants.CATEGORY_ORDER.items():
        assert len(cats) >= 4, f"{app} needs >= 4 categories"
        assert len(cats) == len(set(cats)), f"{app} has duplicate categories"
        theme = constants.APP_THEME[app]
        assert theme["label"] and theme["color"].startswith("#")


def test_excel_has_eight_categories():
    assert len(constants.CATEGORY_ORDER["excel"]) == 8


def test_pick_category_rotates_by_hour():
    cats = ["A", "B", "C"]
    assert selection.pick_category(cats, now=0) == "A"
    assert selection.pick_category(cats, now=3600) == "B"
    assert selection.pick_category(cats, now=2 * 3600) == "C"
    assert selection.pick_category(cats, now=3 * 3600) == "A"  # wraps


def test_pick_category_handles_empty_list():
    assert selection.pick_category([], now=123) is None


def test_load_shortcuts_reads_the_bundled_dataset():
    data = selection.load_shortcuts("src/plugins/office_hotkeys/data/shortcuts.json")
    assert isinstance(data, list) and len(data) > 0


def _sc(level):
    return {"app": "excel", "category": "X", "keys": ["A"],
            "description": "d", "level": level, "weight": 3}


def test_filter_by_level_is_a_floor():
    pool = [_sc("beginner"), _sc("intermediate"), _sc("advanced")]
    assert [s["level"] for s in selection.filter_by_level(pool, "beginner")] == \
        ["beginner", "intermediate", "advanced"]
    assert [s["level"] for s in selection.filter_by_level(pool, "intermediate")] == \
        ["intermediate", "advanced"]
    assert [s["level"] for s in selection.filter_by_level(pool, "advanced")] == \
        ["advanced"]


def test_filter_by_level_empty_when_nothing_qualifies():
    assert selection.filter_by_level([_sc("beginner")], "advanced") == []
