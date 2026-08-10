"""
Data models for Startup Health Dashboard.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class HealthResult:
    """
    Represents the final startup health evaluation.
    """

    company_id: str
    health_score: int
    status: str
    components: Dict[str, bool]
    missing_components: List[str]
    recommendations: List[str]