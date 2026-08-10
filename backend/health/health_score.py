"""
Startup Health Dashboard - Version 1.

Combines document component detection with the
rule-based startup health scoring engine.
"""

from health.rules import (
    HEALTH_RULES,
    calculate_score,
    get_status,
    get_missing_components
)

from health.models import HealthResult
from health.component_detector import ComponentDetector


class StartupHealthEngine:
    """
    Rule-based startup health evaluation engine.
    """

    def __init__(self, company_id: str):
        self.company_id = company_id
        self.detector = ComponentDetector()

    # ---------------------------------------------------------
    # Evaluate detected components
    # ---------------------------------------------------------

    def evaluate(self, components: dict) -> HealthResult:
        """
        Evaluate startup health from detected components.
        """

        score = calculate_score(components)

        status = get_status(score)

        missing_components = get_missing_components(
            components
        )

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

    # ---------------------------------------------------------
    # Evaluate document
    # ---------------------------------------------------------

    def evaluate_document(self, text: str) -> HealthResult:
        """
        Evaluate startup health directly from parsed
        document text.

        Flow:

        Document Text
            ↓
        Component Detector
            ↓
        Components
            ↓
        Health Score
        """

        components = self.detector.detect(text)

        return self.evaluate(components)

    # ---------------------------------------------------------
    # Detailed document analysis
    # ---------------------------------------------------------

    def get_document_analysis(self, text: str) -> dict:
        """
        Return detailed evidence for every component.

        Includes:

        - detected
        - evidence_count
        - threshold
        - confidence
        - matched_groups
        - matched_keywords
        """

        return self.detector.get_evidence(text)

    # ---------------------------------------------------------
    # Recommendations
    # ---------------------------------------------------------

    def _generate_recommendations(
        self,
        missing_components: list
    ) -> list:
        """
        Generate recommendations for missing
        startup components.
        """

        recommendations = []

        for component in missing_components:

            rule = HEALTH_RULES.get(component)

            if rule:

                recommendations.append(
                    f"Add or complete your "
                    f"{rule['label']}."
                )

        return recommendations