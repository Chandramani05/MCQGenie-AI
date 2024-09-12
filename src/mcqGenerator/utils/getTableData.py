import json
import traceback

def get_table_data(quiz_data):
    """
    Process quiz data, which can either be a string (JSON) or a dictionary, to extract table data.
    """
    try:
        # Check if it's a string and convert it to a dictionary if necessary
        if isinstance(quiz_data, str):
            if not quiz_data.strip():
                raise ValueError("Empty or invalid JSON string received")
            quiz_dict = json.loads(quiz_data)
        elif isinstance(quiz_data, dict):
            quiz_dict = quiz_data
        else:
            raise ValueError("Invalid input data. Expected a JSON string or dictionary.")

        # Process the quiz dictionary
        quiz_table_data = []
        for key, value in quiz_dict.items():
            mcq = value.get("mcq", "No question provided")
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value.get("options", {}).items()
                ]
            )
            correct = value.get("correct", "No correct answer provided")
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
