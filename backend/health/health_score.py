"""
Startup Health Dashboard - Version 1.

Combines the rule engine and result model to generate
a complete startup health assessment.
"""

from health.rules import (
    HEALTH_RULES,
    calculate_score,
    get_status,
    get_missing_components
)

from health.models import HealthResult


class StartupHealthEngine:
    """
    Rule-based startup health evaluation engine.
    """

    def __init__(self, company_id: str):
        self.company_id = company_id

    def evaluate(self, components: dict) -> HealthResult:
        """
        Evaluate startup health based on available components.
        """

        score = calculate_score(components)

        status = get_status(score)

        missing_components = get_missing_components(components)

        recommendations = self._generate_recommendations(
            missing_components
        )

        return HealthResult(
            company_id=self.company_id,
            health_score=score,
            status=status,
            components=components,
            missing_components=missing_components,
            recommendations=recommendations
        )

    def _generate_recommendations(
        self,
        missing_components: list
    ) -> list:
        """
        Generate recommendations for missing startup components.
        """

        recommendations = []

        for component in missing_components:

            rule = HEALTH_RULES.get(component)

            if rule:
                recommendations.append(
                    f"Add or complete your {rule['label']}."
                )

        return recommendations