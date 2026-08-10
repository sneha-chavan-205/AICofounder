from health.health_score import StartupHealthEngine


company_id = "company_001"

components = {
    "business_plan": True,
    "pitch_deck": True,
    "financial_report": True,
    "competitor_analysis": False,
    "vision": True
}


engine = StartupHealthEngine(company_id)

result = engine.evaluate(components)


print("=" * 60)
print("STARTUP HEALTH DASHBOARD - VERSION 1")
print("=" * 60)

print("Company ID:", result.company_id)
print("Health Score:", result.health_score)
print("Status:", result.status)

print("\nComponents:")

for component, available in result.components.items():
    print(f"  {component}: {'Available' if available else 'Missing'}")

print("\nMissing Components:")

for component in result.missing_components:
    print(" ", component)

print("\nRecommendations:")

for recommendation in result.recommendations:
    print(" ", recommendation)

print("=" * 60)