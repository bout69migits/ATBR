import requests
import json
from OpenRouterTitleExamples import Example_1,Example_2, Example_3, Example_4, Example_5, Example_6, Example_7, Example_8, Example_9, Example_10, Example_11, Example_12, Example_13
from OpenRouterBody import content
from html.parser import HTMLParser

class HTMLToTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text)

def parse_html_to_text(html_content):
    parser = HTMLToTextParser()
    parser.feed(html_content)
    return parser.get_text()

# Provide the value for html_content
html_content = f"{content}"

plain_text = parse_html_to_text(html_content)

titleprompt = '''
Create an engaging, concise title for the given text that follows the format of the examples below.
Include at least one relevant number in the title whenever possible.
The text you need to create a title for will be provided after all of the examples.
Respond with only the generated title itself, you must not include any labels like "Title:" in your response.
'''

OPENROUTER_API_KEY = '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'

xa = requests.post(
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
                "content": f"{Example_1}"
            },
            {
                "role": "system",
                "content": f"{Example_2}"
            },
            {
                "role": "system",
                "content": f"{Example_3}"
            },
            {
                "role": "system",
                "content": f"{Example_4}"
            },
            {
                "role": "system",
                "content": f"{Example_5}"
            },
            {
                "role": "system",
                "content": f"{Example_6}"
            },
            {
                "role": "system",
                "content": f"{Example_7}"
            },
            {
                "role": "system",
                "content": f"{Example_8}"
            },
            {
                "role": "system",
                "content": f"{Example_9}"
            },
            {
                "role": "system",
                "content": f"{Example_10}"
            },
            {
                "role": "system",
                "content": f"{Example_11}"
            },
            {
                "role": "system",
                "content": f"{Example_12}"
            },
            {
                "role": "system",
                "content": f"{Example_13}"
            },
            {
                "role": "user",
                "content": f"{plain_text}"
            },
            {
                "role": "user",
                "content": "Remove 'Title:' from your response."
            },
         ],
        "temperature": 0.3,  
        "max_tokens": 90,  
        # Add other parameters as needed
    }
))

# Check if the request was successful
if xa.status_code == 200:
    # Parse the JSON response
    json_data = json.loads(xa.text)

    # Get the list of choices
    choices = json_data.get("choices", [])

    # Iterate over the choices and extract the message content
    for choice in choices:
        message = choice.get("message", {})
        titlecontent = message.get("content", "")
        print("Title Generation: Success")
else:
    print(f"Request failed with status code: {xa.status_code}")
