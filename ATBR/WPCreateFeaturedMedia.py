import requests
from ATBRScrape import URL
import os
from seleniumbase import SB
import wget
import time
download_dir = r"C:\Users\dtayl\OneDrive\Documents\VSS\BrowserBased\ATBR\WPMedia"

#ATBR AUTH
api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
url = "https://allthebestrecipe.com/wp-json/wp/v2/"
username = "MartyHenderson@pepeslam.com"
password = "XrKt hQM9 lBnR 3lXk Bmpe SpWo'"
endpoint = 'media'

with SB(
    incognito=True, rtf=True, undetectable=True, uc_subprocess=True, disable_js=False, uc_cdp=True, do_not_track=True, headless2=False, ad_block_on=True, block_images=False, 
) as sb:
        
    sb.open(URL)

    try:
        img = sb.get_attribute('#img.primary-image__image', 'data-src')
        url = img
        imgalt = sb.get_attribute('#img.primary-image__image', 'alt')
        if imgalt is None:
            raise Exception("Alt text not found for the first element")
    except Exception as e:
        print(f"First try failed: {str(e)}. Trying another element.")
        time.sleep(2)
        try:
            sb.click('#gallery-photo_1-0 .universal-image__image', by="css selector", timeout=5) 
            time.sleep(2)  
            img = sb.get_attribute('#photo-dialog__item_1-0 .universal-image__image', 'data-src')
            url = img
            imgalt = sb.get_attribute('#photo-dialog__item_1-0 .universal-image__image', 'alt')
            sb.click('#photo-dialog_1-0 .dialog__close', by="css selector")
            
            if imgalt is None:
                raise Exception("Alt text not found for the second element")
        except Exception as e:
            print(f"Second try failed: {str(e)}. Unable to find a suitable image.")
            url = None
            imgalt = None
    
    if url is not None:
        #Check to see if the image is a "Step"
        image = wget.download(url, out=download_dir)

        #Authentication Details for WP
        api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
        wp_url = "https://allthebestrecipe.com/wp-json/wp/v2/"
        username = "MartyHenderson@pepeslam.com"
        password = "XrKt hQM9 lBnR 3lXk Bmpe SpWo'"

        #File Details for WP
        endPath = os.path.basename(image)
        imgPath = 'C:/Users/dtayl/OneDrive/Documents/VSS/BrowserBased/ATBR/WPMedia/'
        fileName = endPath

        # Open the file in binary mode
        with open(os.path.join(imgPath, endPath), 'rb') as file:

            # Create the payload for the API request
            payload = {
                'file': (fileName, file),
                'alt_text': f"{imgalt}",
                'description': f"{imgalt}",
            }

            # Create a requests Session object
            session = requests.Session()

            # Add the API key to the request headers
            session.headers.update({'X-API-KEY': api_key})

            # Perform a POST request to the API endpoint with authentication
            response = session.post(wp_url + 'media', auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                # Get the image ID from the response
                image_id = response.json()['id']

                # Assign the image ID to the Featured_Img_ID variable
                Featured_Img_ID = image_id

                # Update the alt_text of the uploaded image
                update_url = wp_url + 'media/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                    print(Featured_Img_ID)
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
                Featured_Img_ID = None
    else:
        print("No suitable image found.")
        Featured_Img_ID = None



