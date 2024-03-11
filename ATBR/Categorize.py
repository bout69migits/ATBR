import requests
from ATBRScrape import Category_2, Category_3, Category_4
from seleniumbase import SB

# Authentication details
api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
url = "https://allthebestrecipe.com"
username = "MartyHenderson@pepeslam.com"
password = "XrKt hQM9 lBnR 3lXk Bmpe SpWo'"

# Authentication
auth = (username, password)
with SB(headless=False, ad_block_on=True) as sb:
    # Function to get all categories from WordPress
    def get_categories():
        endpoint = f"{url}/wp-json/wp/v2/categories?per_page=200"
        response = requests.get(endpoint, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve categories.")
            return []

    # Function to create a new category
def create_category(name, parent_id=None):
    endpoint = f"{url}/wp-json/wp/v2/categories"
    data = {"name": name}
    if parent_id:
        data["parent"] = parent_id
    response = requests.post(endpoint, auth=auth, json=data)
    if response.status_code == 201:
        return response.json()["id"]
    else:
        print(f"Failed to create category: {name}")
        return None

# Function to find or create a category
def find_or_create_category(name, parent_id=None):
    endpoint = f"{url}/wp-json/wp/v2/categories?search={name}"
    response = requests.get(endpoint, auth=auth)
    if response.status_code == 200:
        categories = response.json()
        if categories:
            for category in categories:
                if category["name"].lower() == name.lower():
                    return category["id"]
        # If no matching category is found, create a new one
        return create_category(name, parent_id)
    else:
        print("Failed to retrieve categories.")
        return None

# Main script
def main(sb):
    category_1_id = "415"

    category_2 = Category_2(sb)
    category_2_id = find_or_create_category(category_2, parent_id=category_1_id)
    if category_2_id is None:
        print("Category 2 not found or created.")
        return category_1_id, None, None, None

    category_3 = Category_3(sb)
    category_3_id = find_or_create_category(category_3, parent_id=category_2_id)
    if category_3_id is None:
        print("Category 3 not found or created.")
        return category_1_id, category_2_id, None, None

    category_4 = Category_4(sb)
    category_4_id = find_or_create_category(category_4, parent_id=category_3_id)
    if category_4_id is None:
        print("Category 4 not found or created.")
        return category_1_id, category_2_id, category_3_id, None

    return category_1_id, category_2_id, category_3_id, category_4_id



