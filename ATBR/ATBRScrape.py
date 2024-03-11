from seleniumbase import SB
import requests
import wget
import os
#URL to be scraped
URL = "https://www.allrecipes.com/recipe/278581/air-fryer-french-fries/"

download_dir = r"C:\Users\dtayl\OneDrive\Documents\VSS\BrowserBased\ATBR\WPMedia"

#ATBR AUTH
api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
url = "https://allthebestrecipe.com/wp-json/wp/v2/"
username = "MartyHenderson@pepeslam.com"
password = "XrKt hQM9 lBnR 3lXk Bmpe SpWo'"
endpoint = 'media'




with SB(
    incognito=True, rtf=True, undetectable=True, uc_subprocess=True, disable_js=False, uc_cdp=True, do_not_track=True, headless2=False, ad_block_on=True, block_images=True, 
) as sb:
        #Title
    def Title(sb):
            sb.open(URL)
            try:
                sb.assert_element('h1.article-heading', timeout=10)
                headingelem = sb.get_text('h1.article-heading')
                print(headingelem)
                return headingelem
            except Exception as e:
                print(f"Error occurred while locating the element: {str(e)}")
        #Category
    def Category_4(sb):
        sb.open(URL)
        try:
            sb.assert_element('a#mntl-text-link_12-0', timeout=10)
            Category_4 = sb.get_text('a#mntl-text-link_12-0')
            print(Category_4)
            return Category_4.title()
        except Exception as e:
            print(f"Error occurred while locating the element: {str(e)}")

    def Category_3(sb):
        sb.open(URL)
        try:
            sb.assert_element('a#mntl-text-link_11-0', timeout=10)
            Category_3 = sb.get_text('a#mntl-text-link_11-0')
            print(Category_3)
            return Category_3.title()
        except Exception as e:
            print(f"Error occurred while locating the element: {str(e)}")

    def Category_2(sb):
        sb.open(URL)
        try:
            sb.assert_element('a#mntl-text-link_10-0', timeout=10)
            Category_2 = sb.get_text('a#mntl-text-link_10-0')
            print(Category_2)
            return Category_2.title()
        except Exception as e:
            print(f"Error occurred while locating the element: {str(e)}")

    def Category_1(sb):
        sb.open(URL)
        try:
            sb.assert_element('a#mntl-text-link_10-0', timeout=10)
            Category_1 = sb.get_text('a#mntl-text-link_10-0')
            print(Category_1)
            return Category_1.title()
        except Exception as e:
            print(f"Error occurred while locating the element: {str(e)}")

    def Intro(sb):
            #Intro Content
            sb.open(URL)
            try:
                sb.assert_element('p.article-subheading', timeout=10)
                introelem = sb.get_text('p.article-subheading')
                print(introelem)
                return introelem
            except Exception as e:
                print(f"Error occurred while locating the element: {str(e)}")

    def Details(sb):
            #Recipe Details
            sb.open(URL)
            try:
                sb.assert_element('div.mntl-recipe-details__content', timeout=10)
                detailelem = sb.get_text('div.mntl-recipe-details__content')
                print(detailelem)
                return detailelem
            except Exception as e:
                print(f"Error occurred while locating the element: {str(e)}")

    def Ingredients(sb):
            #Ingredients
            sb.open(URL)
            try:
                sb.assert_element('ul.mntl-structured-ingredients__list', timeout=10)
                ingredelem = sb.get_text('ul.mntl-structured-ingredients__list')
                print(ingredelem)
                return ingredelem
            except Exception as e:
                print(f"Error occurred while locating the element: {str(e)}")

    def Steps(sb):
            #Steps
            sb.open(URL)
            try:
                sb.assert_element('ol#mntl-sc-block_50-0', timeout=10)
                stepselem = sb.get_text('ol#mntl-sc-block_50-0')
                print(stepselem)
                return stepselem
            except Exception as e:
                print(f"Error occurred while locating the element: {str(e)}")

    def get_image1(sb):

        # Get the URL and alt text of the first image.
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_2-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_2-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')

            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
            
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None
    
    def get_image2(sb):
        # Get the URL and alt text of the first image.
            
            sb.open(URL)
            try:
                img = sb.get_attribute('img#mntl-sc-block-image_3-0', 'data-src')
                url = img
                imgalt = sb.get_attribute('img#mntl-sc-block-image_3-0', 'alt')
                print("Successfully pulled Image!") 
                #Check to see if the image is a "Step"
                if "Step" not in url:
                    
                    print("Skipping image upload: URL does not contain 'Step'.")
                    return None, None 
                else:        
                    image = wget.download(url, out=download_dir)
                    #Authentication Details for WP
                    api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                    url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                    response = session.post(url + endpoint, auth=(username, password), files=payload)

                # Check the response status code
                if response.status_code == 201:
                    print('Image uploaded successfully!')
                    #Delete Local Image
                    os.remove(os.path.join(imgPath, endPath))

                    #Get Image URL
                    response_json = response.json()
                    image_url = response_json['source_url']
                    print(f'Image URL: {image_url}')

                    image_id = response.json()['id']

                # Update the alt_text of the uploaded image
                    update_url = url + endpoint + '/' + str(image_id)
                    update_payload = {
                        'alt_text': imgalt
                    }
                    update_response = session.post(update_url, auth=(username, password), json=update_payload)

                    # Check the update response status code
                    if update_response.status_code == 200:
                        print('Image alt_text updated successfully!')
                    else:
                        print(f'Error updating image alt_text. Status code: {update_response.status_code}')
                else:
                    print(f'Error uploading image. Status code: {response.status_code}')
                return image_url, imgalt
            except Exception as e:
                print(f"Failed to locate an image at the element: {str(e)}")
                return None, None

    def get_image3(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_4-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_4-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
           
    def get_image4(sb):
        # Get the URL and alt text of the first image.
            
            sb.open(URL)
            try:
                img = sb.get_attribute('img#mntl-sc-block-image_5-0', 'data-src')
                url = img
                imgalt = sb.get_attribute('img#mntl-sc-block-image_5-0', 'alt')
                print("Successfully pulled Image!") 
                #Check to see if the image is a "Step"
                if "Step" not in url:
                    
                    print("Skipping image upload: URL does not contain 'Step'.")
                    return None, None 
                else:        
                    image = wget.download(url, out=download_dir)
                    #Authentication Details for WP
                    api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                    url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                    response = session.post(url + endpoint, auth=(username, password), files=payload)

                # Check the response status code
                if response.status_code == 201:
                    print('Image uploaded successfully!')
                    #Delete Local Image
                    os.remove(os.path.join(imgPath, endPath))

                    #Get Image URL
                    response_json = response.json()
                    image_url = response_json['source_url']
                    print(f'Image URL: {image_url}')

                    image_id = response.json()['id']

                # Update the alt_text of the uploaded image
                    update_url = url + endpoint + '/' + str(image_id)
                    update_payload = {
                        'alt_text': imgalt
                    }
                    update_response = session.post(update_url, auth=(username, password), json=update_payload)

                    # Check the update response status code
                    if update_response.status_code == 200:
                        print('Image alt_text updated successfully!')
                    else:
                        print(f'Error updating image alt_text. Status code: {update_response.status_code}')
                else:
                    print(f'Error uploading image. Status code: {response.status_code}')
                return image_url, imgalt
            except Exception as e:
                print(f"Failed to locate an image at the element: {str(e)}")
                return None, None
            
    def get_image5(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_6-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_6-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
        
    def get_image6(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_7-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_7-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
        

    def get_image7(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_8-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_8-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
    def get_image8(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_9-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_9-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
        
    def get_image9(sb):
# Get the URL and alt text of the first image.
        
        sb.open(URL)
        try:
            img = sb.get_attribute('img#mntl-sc-block-image_10-0', 'data-src')
            url = img
            imgalt = sb.get_attribute('img#mntl-sc-block-image_10-0', 'alt')
            print("Successfully pulled Image!") 
            #Check to see if the image is a "Step"
            if "Step" not in url:
                
                print("Skipping image upload: URL does not contain 'Step'.")
                return None, None 
            else:        
                image = wget.download(url, out=download_dir)
                #Authentication Details for WP
                api_key = "9cun603nrm4mvftl6f43iefonz1lbk2f"
                url = "https://allthebestrecipe.com/wp-json/wp/v2/"
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
                response = session.post(url + endpoint, auth=(username, password), files=payload)

            # Check the response status code
            if response.status_code == 201:
                print('Image uploaded successfully!')
                #Delete Local Image
                os.remove(os.path.join(imgPath, endPath))

                #Get Image URL
                response_json = response.json()
                image_url = response_json['source_url']
                print(f'Image URL: {image_url}')

                image_id = response.json()['id']

            # Update the alt_text of the uploaded image
                update_url = url + endpoint + '/' + str(image_id)
                update_payload = {
                    'alt_text': imgalt
                }
                update_response = session.post(update_url, auth=(username, password), json=update_payload)

                # Check the update response status code
                if update_response.status_code == 200:
                    print('Image alt_text updated successfully!')
                else:
                    print(f'Error updating image alt_text. Status code: {update_response.status_code}')
            else:
                print(f'Error uploading image. Status code: {response.status_code}')
            return image_url, imgalt
        except Exception as e:
            print(f"Failed to locate an image at the element: {str(e)}")
            return None, None 
    def Nutrition(sb):
        #Nutrition Facts
        sb.open(URL)
        try:
            sb.scroll_into_view("span[class='mntl-nutrition-facts-label__button-text']", by="css selector", timeout=None)
            sb.click("span[class='mntl-nutrition-facts-label__button-text']", by="css selector", timeout=10)
            nutrielem = sb.get_text('table.mntl-nutrition-facts-label__table')
            print(nutrielem)
            return nutrielem
        except Exception as e:
            print(f"Error occurred while locating the element: {str(e)}")



    #Call All Of The Elements
    def scrape_recipe(sb):
        Title(sb)
        Category_1(sb)
        Category_2(sb)
        Category_3(sb)
        Category_4(sb)
        Intro(sb)
        Details(sb)
        Ingredients(sb)
        Steps(sb)
        get_image1(sb)
        get_image2(sb)
        get_image3(sb)
        get_image4(sb)
        get_image5(sb)
        get_image6(sb)
        get_image7(sb)
        get_image8(sb)
        get_image9(sb)
        Nutrition(sb)
