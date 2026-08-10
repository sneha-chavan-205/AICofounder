"""
Reliable startup component detection for Feature 4.

Version 1 uses deterministic, explainable evidence-based rules.

Instead of checking whether one keyword exists, the detector
checks multiple evidence groups and applies minimum thresholds.
"""

import re


COMPONENT_RULES = {

    # ---------------------------------------------------------
    # BUSINESS PLAN
    # ---------------------------------------------------------

    "business_plan": {

        "label": "Business Plan",

        "threshold": 3,

        "groups": {

            "problem": [
                "problem statement",
                "problem",
                "pain point",
                "customer problem",
                "problem we solve"
            ],

            "market": [
                "market opportunity",
                "target market",
                "market size",
                "tam",
                "sam",
                "som",
                "customer segment",
                "target customers"
            ],

            "business_model": [
                "business model",
                "revenue model",
                "pricing model",
                "revenue stream",
                "value proposition"
            ],

            "strategy": [
                "go-to-market",
                "go to market",
                "marketing strategy",
                "sales strategy",
                "growth strategy",
                "distribution strategy"
            ],

            "plan": [
                "business plan",
                "operational plan",
                "implementation plan",
                "strategic plan"
            ]
        }
    },


    # ---------------------------------------------------------
    # PITCH DECK
    # ---------------------------------------------------------

    "pitch_deck": {

        "threshold": 3,

        "groups": {

            "explicit_pitch": [
                "pitch deck",
                "investor pitch",
                "startup pitch",
                "investment pitch"
            ],

            "funding": [
                "funding round",
                "fundraising",
                "fund raise",
                "investment opportunity",
                "seeking investment",
                "raising capital",
                "capital raise",
                "funding requirement"
            ],

            "traction": [
                "traction",
                "user growth",
                "customer growth",
                "monthly active users",
                "active users",
                "customers acquired",
                "revenue growth"
            ],

            "startup_presentation": [
                "problem",
                "solution",
                "market opportunity",
                "business model",
                "competitive advantage",
                "team",
                "founder"
            ],

            "investment_ask": [
                "investment ask",
                "funding ask",
                "ask",
                "use of funds",
                "funds required",
                "capital required"
            ]
        }
    },


    # ---------------------------------------------------------
    # FINANCIAL REPORT
    # ---------------------------------------------------------

    "financial_report": {

        "threshold": 3,

        "groups": {

            "statements": [
                "financial statement",
                "financial statements",
                "income statement",
                "balance sheet",
                "cash flow statement",
                "cash flow"
            ],

            "profitability": [
                "gross profit",
                "operating income",
                "operating margin",
                "net income",
                "net loss",
                "profit margin",
                "ebitda"
            ],

            "financial_metrics": [
                "revenue",
                "total revenue",
                "cost of revenue",
                "operating expenses",
                "expenses",
                "earnings",
                "eps",
                "earnings per share"
            ],

            "financial_period": [
                "fiscal year",
                "fiscal quarter",
                "quarterly results",
                "annual results",
                "year over year",
                "year-over-year",
                "quarter over quarter"
            ]
        }
    },


    # ---------------------------------------------------------
    # COMPETITOR ANALYSIS
    # ---------------------------------------------------------

    "competitor_analysis": {

        "threshold": 2,

        "groups": {

            "competitors": [
                "competitor",
                "competitors",
                "key competitors",
                "main competitors",
                "direct competitors"
            ],

            "competitive_analysis": [
                "competitive analysis",
                "competitor analysis",
                "competitive landscape",
                "competitive environment"
            ],

            "comparison": [
                "competitor comparison",
                "competitive comparison",
                "compare competitors",
                "compared with competitors",
                "comparison with competitors"
            ],

            "competitive_advantage": [
                "competitive advantage",
                "competitive edge",
                "differentiator",
                "differentiation",
                "unique advantage",
                "unique selling proposition",
                "usp"
            ]
        }
    },


    # ---------------------------------------------------------
    # VISION
    # ---------------------------------------------------------

    "vision": {

        "threshold": 2,

        "groups": {

            "vision": [
                "our vision",
                "company vision",
                "startup vision",
                "vision statement",
                "vision is",
                "our long-term vision"
            ],

            "mission": [
                "our mission",
                "company mission",
                "mission statement",
                "mission is"
            ],

            "long_term": [
                "long-term goal",
                "long term goal",
                "long-term goals",
                "long term goals",
                "future goals",
                "strategic vision",
                "future vision"
            ]
        }
    }
}


class ComponentDetector:
    """
    Evidence-based startup component detector.

    A component is detected only when enough independent
    evidence groups are found.
    """

    def __init__(self):
        self.rules = COMPONENT_RULES

    @staticmethod
    def _normalize_text(text: str) -> str:
        """
        Normalize document text for reliable matching.
        """

        text = text.lower()

        # Replace repeated whitespace
        text = re.sub(r"\s+", " ", text)

        return text

    @staticmethod
    def _contains_phrase(text: str, phrase: str) -> bool:
        """
        Check whether a phrase exists as a meaningful match.

        Word boundaries reduce accidental substring matches.
        """

        pattern = r"\b" + re.escape(phrase.lower()) + r"\b"

        return re.search(pattern, text) is not None

    def _detect_component(
        self,
        text: str,
        component: str
    ) -> dict:
        """
        Detect one component using evidence groups.
        """

        rule = self.rules[component]

        matched_groups = {}
        matched_keywords = []

        for group_name, keywords in rule["groups"].items():

            group_matches = []

            for keyword in keywords:

                if self._contains_phrase(text, keyword):

                    group_matches.append(keyword)

                    matched_keywords.append(keyword)

            if group_matches:
                matched_groups[group_name] = group_matches

        evidence_count = len(matched_groups)

        threshold = rule["threshold"]

        detected = evidence_count >= threshold

        # Confidence is based on evidence groups.
        confidence = min(
            evidence_count / threshold,
            1.0
        )

        return {
            "detected": detected,
            "evidence_count": evidence_count,
            "threshold": threshold,
            "confidence": round(confidence, 2),
            "matched_groups": matched_groups,
            "matched_keywords": matched_keywords
        }

    def analyze(self, text: str) -> dict:
        """
        Analyze the complete document.

        Returns detailed evidence for every component.
        """

        if not text:
            return {
                component: {
                    "detected": False,
                    "evidence_count": 0,
                    "threshold": rule["threshold"],
                    "confidence": 0.0,
                    "matched_groups": {},
                    "matched_keywords": []
                }
                for component, rule in self.rules.items()
            }

        normalized_text = self._normalize_text(text)

        analysis = {}

        for component in self.rules:

            analysis[component] = self._detect_component(
                normalized_text,
                component
            )

        return analysis

    def detect(self, text: str) -> dict:
        """
        Return simple True/False component availability.

        This method keeps compatibility with health_score.py.
        """

        analysis = self.analyze(text)

        return {
            component: result["detected"]
            for component, result in analysis.items()
        }

    def get_matched_keywords(self, text: str) -> dict:
        """
        Return matched keywords for each component.

        Kept for dashboard/debugging compatibility.
        """

        analysis = self.analyze(text)

        return {
            component: result["matched_keywords"]
            for component, result in analysis.items()
        }

    def get_evidence(self, text: str) -> dict:
        """
        Return complete evidence information.

        Useful for explaining dashboard decisions.
        """

        return self.analyze(text)