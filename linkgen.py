import json

def get_title_slug_link_by_id(nos):
    """
    Retrieve the full LeetCode problem link based on its questionFrontendId from a JSON file.

    :param nos: Integer representing the questionFrontendId.
    :return: The problem link if found, else None.
    """
    try:
        with open("problems.json", 'r') as file:
            data = json.load(file)  # Load the JSON data from the file
        
        # Iterate through the question list to find the matching questionFrontendId
        for question in data.get("problemsetQuestionList", []):
            if str(question.get("questionFrontendId")) == str(nos):
                title_slug = question.get("titleSlug")
                if title_slug:
                    return f"leetcode.com/problems/{title_slug}/description"
        return None  # Return None if no match is found
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    return None

