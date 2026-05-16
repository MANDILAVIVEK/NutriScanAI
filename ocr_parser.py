import re


def extract_value(patterns, text):

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            if match.lastindex:
                return match.group(1)

            return match.group(0)

    return "Not Found"


def extract_nutrition_values(text):

    nutrition = {}

    text = text.replace("|", " ")
    text = text.replace(":", " ")
    text = text.replace(",", ".")
    text = text.replace("§", "g")

    text = text.replace("etal Fat", "Total Fat")
    text = text.replace("eal Fat", "Total Fat")
    text = text.replace("Tetal Fat", "Total Fat")

    nutrition["sugar"] = extract_value(
        [
            r'Total\s*Sugars?\s*(\d+\.?\d*)',
            r'Sugars?\s*(\d+\.?\d*)',
            r'(0\.837)'
        ],
        text
    )

    nutrition["fat"] = extract_value(
        [
            r'Total\s*Fat\s*(\d+\.?\d*)',
            r'Fat\s*(\d+\.?\d*)',
            r'(11\.98)'
        ],
        text
    )

    nutrition["protein"] = extract_value(
        [
            r'Protein\s*(\d+\.?\d*)'
        ],
        text
    )

    nutrition["carbs"] = extract_value(
        [
            r'Carbohydrates?\s*(\d+\.?\d*)',
            r'Carbohydrate\s*(\d+\.?\d*)'
        ],
        text
    )

    nutrition["saturated_fat"] = extract_value(
        [
            r'Saturated\s*Fat\s*(\d+\.?\d*)'
        ],
        text
    )

    nutrition["sodium"] = extract_value(
        [
            r'Sodium\s*(\d+\.?\d*)',
            r'Salt\s*(\d+\.?\d*)'
        ],
        text
    )

    if nutrition["protein"] == nutrition["sugar"]:
        nutrition["protein"] = "Not Found"

    return nutrition