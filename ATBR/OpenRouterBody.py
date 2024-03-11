import requests
import json
from OpenRouterBodyExamples import Example1, Example2, example3, Example4, example5, example6
from OpenRouterBodyPrompt import prompt
from seleniumbase import SB

with SB(headless=True, ad_block_on=True) as sb:
    text = prompt(sb)

prompto = '''
You are tasked with formatting a blog post into high quality Search Engine Optimized HTML code.
You will be given the text in chronological order, rewrite the text in high quality HTML code.

You will be given text that you must rewrite into HTML code for a single post. Please carefully review the examples provided to gain a deep understanding of how your response should be structured.
Specifically, pay attention to the 'Input Text:' section, which represents an example text given to you, and then study the 'Response in HTML:' section, which represents the expected response from you based on the input text.
When providing your response, adhere to the following guidelines:

Do not include the "Input Text:" label in your response; only the HTML code should be present.
Do not create or generate content about anything other than the text that is given to you.
Your response must stop after the first occurrence of the phrase "Your destination for culinary inspiration."
Please ensure that you strictly follow these guidelines when generating your response.
'''

model = 'google/gemini-pro'

OPENROUTER_API_KEY = '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'


response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    json={
        "model": f"{model}",
        "messages": [
            {
                "role": "system",
                "content": f"{prompto}"
            },
            {
                "role": "system",
                "content": f"First Example:{Example1}"
            },
            {
                "role": "system",
                "content": f"Second Example:{Example2}"
            },
            {
                "role": "system",
                "content": f"Third Example:{example3}"
            },
            {
                "role": "system",
                "content": f"Fourth Example:{Example4}"
            },
            {
                "role": "system",
                "content": f"Fifth Example:{example5}"
            },
            {
                "role": "system",
                "content": f"Sixth Example:{example6}"
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        "temperature": 0.2,  
        "max_tokens": 131000,
        "stop": "destination for culinary inspiration."
        # Add other parameters as needed
    }
)


print("API Response:")
print(response.text)

# Function to parse the JSON string and extract the "content" from the messages
def parse_content():
    # Parse the JSON string into a Python dictionary
    json_data = json.loads(response.text)

    # Get the list of choices
    choices = json_data.get("choices", [])

    # Check if choices is empty
    if not choices:
        print("No choices found in the API response")
        return ""

    # Get the first choice
    first_choice = choices[0]

    # Get the message content from the first choice
    message = first_choice.get("message", {})
    content = message.get("content", "")

    return content

# Call the parse_content function and print the content if it's not empty
content = parse_content()
if content:
    print("Body Generated: Success")
else:
    print("Failed to extract content from the API response.")


#Start The Keyword Extraction


json_string = response.text

# Parse the JSON string
data = json.loads(json_string)

# Extract the content from the keyword section
content = data['choices'][0]['message']['content']

# Find the start and end positions of the keyword section
start_index = content.find('\n<meta name="keywords" content="') + len('\n<meta name="keywords" content="')
end_index = content.find('">', start_index)

# Extract the keyword content
keyword_content = content[start_index:end_index]

