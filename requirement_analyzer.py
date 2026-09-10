import json
from openai import OpenAI

client = OpenAI(api_key="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")
#YOUR_OPENAI_API_KEY

def analyze_requirement(requirement):
    prompt = f"""
    You are an expert Excel Business Requirement Analyzer.

    Analyze the following business requirement and return ONLY valid JSON.
    Do not return explanations, markdown, or code fences.

    Business Requirement:
    {requirement}

    Supported operations:
    - add_sheet
    - delete_sheet
    - rename_sheet
    - add_column
    - delete_column
    - rename_column
    - insert_row
    - delete_row
    - update_cell
    - update_formula

    Return JSON in the following format:

    {{
      "operation": "",
      "sheet": "",
      "target": {{}},
      "parameters": {{
          "new_sheet": "",
          "old_sheet": "",
          "new_column": "",
          "old_column": "",
          "new_name": "",
          "position": "",
          "cell": "",
          "value": "",
          "formula": "",
          "columns": []
      }}
    }}

    Rules:

    1. If the requirement is to create a new worksheet, set:
       - operation = "add_sheet"
       - Extract the sheet name.
       - Extract all column names into the "columns" array.

    Example 1

    Requirement:
    Create a new sheet named Dummy with columns Predict, Accurate and Value.

    Output:

    {{
      "operation": "add_sheet",
      "sheet": "",
      "target": {{}},
      "parameters": {{
          "new_sheet": "Dummy",
          "columns": [
              "Predict",
              "Accurate",
              "Value"
          ]
      }}
    }}
    
   
   Example 2

    Requirement:
    Add a new column Region after Customer column in Sales tab in production workbook sheet.

    Output:

   {{
    "operation": "add_column",
    "target": {{
      "sheet": "<sheet_name>",
      "column_name": "<column_name>",
      "after_column": "<after_column>"
             }},
  "reason": ""
    }}


    Example 3

    Requirement:
    Create a worksheet Employee_Report having columns Employee ID, Employee Name and Salary.

    Output:

    {{
      "operation": "add_sheet",
      "sheet": "",
      "target": {{}},
      "parameters": {{
          "new_sheet": "Employee_Report",
          "columns": [
              "Employee ID",
              "Employee Name",
              "Salary"
          ]
      }}
    }}

    Return ONLY JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    print(content)

    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    result = json.loads(content)

    return result
