from src.plugins.office_hotkeys import constants


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
