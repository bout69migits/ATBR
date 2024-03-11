import requests
import json
from OpenRouter_Title import titlecontent
from OpenRouterSlugExamples import Example__1, Example__2, Example__3, Example__4, Example__5, Example__6, Example__7, Example__8, Example__9, Example__10, Example__11

titleprompt = '''
You are tasked with creating a url slug out of the title given to you.
You must keep it less than 37 characters long, there are no exceptions to this limit.
You will be given examples in the next 
'''

OPENROUTER_API_KEY = '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'

slug = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "google/gemini-pro",
        "messages": [
            {
                "role": "system",
                "content": f"{titleprompt}"
            },
            {
                "role": "system",
                "content": f"Example 1:{Example__1}"
            },
            {
                "role": "system",
                "content": f"Example 2:{Example__2}"
            },
            {
                "role": "system",
                "content": f"Example 3:{Example__3}"
            },
            {
                "role": "system",
                "content": f"Example 4:{Example__4}"
            },
            {
                "role": "system",
                "content": f"Example 5:{Example__5}"
            },
            {
                "role": "system",
                "content": f"Example 6:{Example__6}"
            },
            {
                "role": "system",
                "content": f"Example 7:{Example__7}"
            },
            {
                "role": "system",
                "content": f"Example 8:{Example__8}"
            },
            {
                "role": "system",
                "content": f"Example 9:{Example__9}"
            },
            {
                "role": "system",
                "content": f"Example 10:{Example__10}"
            },
            {
                "role": "system",
                "content": f"Example 11:{Example__11}"
            },
            {
                "role": "user",
                "content": f"Title: {titlecontent}"
            }
         ],
        "temperature": 0.3,  
        "max_tokens": 90,  
        # Add other parameters as needed
    }
))

# Check if the request was successful
if slug.status_code == 200:
    # Parse the JSON response
    json_data = json.loads(slug.text)

    # Get the list of choices
    choices = json_data.get("choices", [])

    # Iterate over the choices and extract the message content
    for choice in choices:
        message = choice.get("message", {})
        urlslug = message.get("content", "")
        print("SLUG Generation: Success")
else:
    print(f"Request failed with status code: {slug.status_code}")
