from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(result, filename="Nutrition_Report.pdf"):
    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "AI Food & Nutrition Assistant",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"<b>BMI:</b> {result['bmi']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>BMR:</b> {result['bmr']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Daily Calories:</b> {result['calories']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Meal Plan</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            result["meal_plan"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Recipes</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            result["recipes"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Grocery List</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            result["grocery_list"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Reflection Report</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            result["final_report"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename