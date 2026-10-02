from core.pipeline import run_lifelink

def test_transport_request_is_structured():
    result = run_lifelink(
        "I need wheelchair-accessible transport for my elderly mother tomorrow morning.",
        "Lahore",
        "Pakistan",
        urgency="Today",
    )
    assert result["need"]["category"] == "transport"
    assert len(result["matches"]) >= 1
    assert len(result["trace"]) >= 5

def test_business_supply_request():
    result = run_lifelink(
        "My small business needs 200 custom boxes within 3 days.",
        "Lahore",
        "Pakistan",
    )
    assert result["need"]["category"] == "business_supply"
    assert any("PackPro" in m["name"] for m in result["matches"])

def test_unknown_request_does_not_crash():
    result = run_lifelink(
        "I need something unusual next week.",
        "London",
        "United Kingdom",
    )
    assert "need" in result
    assert "action_plan" in result
