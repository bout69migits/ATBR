import requests
from seleniumbase import SB
from OpenRouterBody import content, keyword_content
from OpenRouter_Title import titlecontent
from OpenRouter_Slug import urlslug
from WPCreateFeaturedMedia import Featured_Img_ID, endPath, imgPath
from Categorize import main
import os
import random

with SB(headless=True, ad_block_on=True) as sb:
    category_1_id, category_2_id, category_3_id, category_4_id = main(sb)

if category_1_id is None or category_2_id is None or category_3_id is None or category_4_id is None:
    print("Some categories were not found or created. Please check the logs.")
else:
    # Use category_1_id, category_2_id, category_3_id, and category_4_id as needed in your WPCreatePost script
    print("Category 1 ID:", category_1_id)
    print("Category 2 ID:", category_2_id)
    print("Category 3 ID:", category_3_id)
    print("Category 4 ID:", category_4_id)


additional_text = """
<h5>All the Best Recipes</h5>
Your ultimate destination for culinary inspiration.

Join us over on <a style="color: #f15641; text-decoration: underline;" href="https://www.facebook.com/profile.php?id=61556103590852">Facebook</a> and let us know what you think of the recipe.

Follow us on <a style="color: #f15641; text-decoration: underline;" href="https://www.instagram.com/allofthebestrecipes/">Instagram</a> to stay up to date on all of the best recipes we have to offer.

<a style="color: #f15641; text-decoration: underline;" href="https://allthebestrecipe.com/">All the Best Recipes</a> - Your ultimate destination for culinary inspiration.
"""

# Post Details
Auth = random.choice([2, 3, 4, 5])

# Authentication details
api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
url = "https://allthebestrecipe.com/wp-json/wp/v2/"
username = "MartyHenderson@pepeslam.com"
password = "XrKt hQM9 lBnR 3lXk Bmpe SpWo'"

# Set the endpoint to interact with
endpoint = 'posts'

# Set the data to send in the request
data = {
    'content': f'''{content}
                {additional_text}''',
    'featured_media' : f'{Featured_Img_ID}',            
    'author': Auth,
    'title': titlecontent,
    'slug': urlslug,
    'categories': [category_1_id, category_2_id, category_3_id, category_4_id],
    'meta': {
        'rank_math_focus_keyword': keyword_content
    }
}

# Create a requests Session object
session = requests.Session()

# Add the API key to the request headers
session.headers.update({'X-API-KEY': api_key})

# Perform a POST request to the API endpoint with authentication
response = session.post(f'{url}{endpoint}',
                         auth=(username, password),
                         json=data)

# Print the response status code and content
print(f'Response status code: {response.status_code}')
if response.status_code == 201:
    os.remove(os.path.join(imgPath, endPath))
    print('Creating wordpress post: Success!')
else:
    os.remove(os.path.join(imgPath, endPath))
    print('Creating wordpress post: Failed!')
