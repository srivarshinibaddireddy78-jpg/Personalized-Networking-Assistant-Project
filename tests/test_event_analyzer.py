from app.services.event_analyzer import ProfileAnalyzer

def test_analyze_profile():
    analyzer = ProfileAnalyzer()

    result = analyzer.analyze_profile(
        "John",
        "Software Engineer",
        "Python, AI",
        "AI Summit"
    )

    assert result["name"] == "John"
    assert result["profession"] == "Software Engineer"