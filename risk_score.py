def calculate_risk_score(result, impact):

    score = 0
    reasons = []

    operation = result.get("operation", "").lower()
    impact_level = impact.get("impact level", "").lower()
    total_rows = impact.get("total rows", 0)
    total_columns = impact.get("total columns", 0)

    # -----------------------------
    # Operation Based Score
    # -----------------------------
    if operation == "update_formula":
        score += 40
        reasons.append("Formula updated")

    elif operation == "add_column":
        score += 20
        reasons.append("New column added")

    elif operation == "delete_column":
        score += 45
        reasons.append("Column deleted")

    elif operation == "rename_sheet":
        score += 30
        reasons.append("Sheet renamed")

    elif operation == "add_sheet":
        score += 15
        reasons.append("New sheet added")

    elif operation == "delete_sheet":
        score += 60
        reasons.append("Sheet deleted")

    elif operation == "update_value":
        score += 15
        reasons.append("Cell value updated")

    # -----------------------------
    # Impact Level Score
    # -----------------------------
    if impact_level == "high":
        score += 40
        reasons.append("High impact change")

    elif impact_level == "medium":
        score += 20
        reasons.append("Medium impact change")

    else:
        score += 10
        reasons.append("Low impact change")

    # -----------------------------
    # Rows Impact
    # -----------------------------
    if total_rows > 1000:
        score += 20
        reasons.append("Large workbook")

    elif total_rows > 100:
        score += 10
        reasons.append("Moderate number of rows")

    else:
        reasons.append("Few rows affected")

    # -----------------------------
    # Columns Impact
    # -----------------------------
    if total_columns > 20:
        score += 10
        reasons.append("Many columns affected")

    # -----------------------------
    # Limit Score
    # -----------------------------
    if score > 100:
        score = 100

    # -----------------------------
    # Risk Level
    # -----------------------------
    if score >= 80:
        level = "High"
    elif score >= 50:
        level = "Medium"
    else:
        level = "Low"

    # -----------------------------
    # Return Result
    # -----------------------------
    return {
        "risk_score": score,
        "risk_level": level,
        "reason": reasons
    }
