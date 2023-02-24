import expander


def test_expanded_form():
    assert expander.expanded_form(12) == "10 + 2"
    assert expander.expanded_form(42) == "40 + 2"
    assert expander.expanded_form(70304) == "70000 + 300 + 4"
