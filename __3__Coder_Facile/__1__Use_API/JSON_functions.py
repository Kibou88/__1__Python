"""Modules to list the JSON functions
JSON: JavaScript Object Notation"""
def format_json(obj):
    """Function to format a JSON object to understand format by user"""
    import json
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)