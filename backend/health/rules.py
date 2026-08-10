"""
Rule definitions for Startup Health Dashboard - Version 1.

Each completed startup component contributes points
to the overall health score.
"""


HEALTH_RULES = {
    "business_plan": {
        "label": "Business Plan",
        "score": 20,
        "description": "Business plan is available."
    },
    "pitch_deck": {
        "label": "Pitch Deck",
        "score": 20,
        "description": "Pitch deck is available."
    },
    "financial_report": {
        "label": "Financial Report",
        "score": 20,
        "description": "Financial information is available."
    },
    "competitor_analysis": {
        "label": "Competitor Analysis",
        "score": 20,
        "description": "Competitor analysis is available."
    },
    "vision": {
        "label": "Vision",
        "score": 20,
        "description": "Startup vision is defined."
    }
}


def calculate_score(components: dict) -> int:
    """
    Calculate the startup health score.

    Args:
        components: Dictionary containing component names
                    and boolean availability.

    Returns:
        Integer health score between 0 and 100.
    """

    score = 0

    for component, rule in HEALTH_RULES.items():
        if components.get(component, False):
            score += rule["score"]

    return score


def get_status(score: int) -> str:
    """
    Convert numerical health score into a health status.
    """

    if score >= 80:
        return "Excellent"

    if score >= 60:
        return "Good"

    if score >= 40:
        return "Needs Improvement"

    return "Critical"


def get_missing_components(components: dict) -> list:
    """
    Return components that are currently missing.
    """

    missing = []

    for component in HEALTH_RULES:
        if not components.get(component, False):
            missing.append(component)

    return missing