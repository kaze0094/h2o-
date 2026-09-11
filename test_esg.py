from services.esg_ai_service import (
    generate_esg_summary,
    calculate_social_impact_score
)


score = calculate_social_impact_score(

    "P001"

)


summary = generate_esg_summary(

    "P001"

)


print("ESG SCORE:")
print(score)


print("\nESG SUMMARY:")
print(summary)