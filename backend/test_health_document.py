from memory.parser import DocumentParser
from health.health_score import StartupHealthEngine


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

company_id = "company_001"

file_path = (
    "uploads/company_001/documents/"
    "TSLA-Q2-2026-Update.pdf"
)


# ---------------------------------------------------------
# Parse document
# ---------------------------------------------------------

print("=" * 60)
print("STARTUP HEALTH DOCUMENT TEST")
print("=" * 60)

print("\nParsing document...")

parser = DocumentParser()

text = parser.extract_text(file_path)

print("Document parsed successfully.")
print("Extracted characters:", len(text))


# ---------------------------------------------------------
# Health analysis
# ---------------------------------------------------------

print("\nRunning Startup Health Analysis...")

engine = StartupHealthEngine(company_id)

result = engine.evaluate_document(text)


# ---------------------------------------------------------
# Final result
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("STARTUP HEALTH RESULT")
print("=" * 60)

print("Company ID:", result.company_id)
print("Health Score:", result.health_score, "/ 100")
print("Status:", result.status)


# ---------------------------------------------------------
# Components
# ---------------------------------------------------------

print("\nDetected Components:")

for component, available in result.components.items():

    status = (
        "Available"
        if available
        else "Missing"
    )

    print(f"  {component}: {status}")


# ---------------------------------------------------------
# Detailed evidence
# ---------------------------------------------------------

analysis = engine.get_document_analysis(text)

print("\n" + "=" * 60)
print("DETAILED EVIDENCE")
print("=" * 60)

for component, data in analysis.items():

    print(f"\n{component}")

    print(
        "  Evidence groups:",
        data["evidence_count"],
        "/",
        data["threshold"]
    )

    print(
        "  Confidence:",
        data["confidence"]
    )

    print(
        "  Detected:",
        data["detected"]
    )

    print("  Matched groups:")

    if data["matched_groups"]:

        for group, keywords in data[
            "matched_groups"
        ].items():

            print(f"    {group}:")

            for keyword in keywords:
                print(f"      - {keyword}")

    else:

        print("    None")


# ---------------------------------------------------------
# Missing components
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING COMPONENTS")
print("=" * 60)

if result.missing_components:

    for component in result.missing_components:
        print(" ", component)

else:

    print(" None")


# ---------------------------------------------------------
# Recommendations
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)

if result.recommendations:

    for recommendation in result.recommendations:
        print(" ", recommendation)

else:

    print(" No recommendations")


print("\n" + "=" * 60)
print("DOCUMENT HEALTH ANALYSIS COMPLETE")
print("=" * 60)