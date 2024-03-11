from ATBRScrape import Intro, Details, Ingredients, Steps, get_image1, get_image2, get_image3, get_image4, get_image5, get_image6, get_image7, get_image8, get_image9, Nutrition
from WPCreateFeaturedMedia import url, imgalt

def prompt(sb):
    intro_text = Intro(sb)
    details_text = Details(sb)
    ingredients_text = Ingredients(sb)
    steps_text = Steps(sb)
    image_url1, imgalt1 = get_image1(sb)
    image_url2, imgalt2 = get_image2(sb)
    image_url3, imgalt3 = get_image3(sb)
    image_url4, imgalt4 = get_image4(sb)
    image_url5, imgalt5 = get_image5(sb)        
    image_url6, imgalt6 = get_image6(sb)
    image_url7, imgalt7 = get_image7(sb)
    image_url8, imgalt8 = get_image8(sb)
    image_url9, imgalt9 = get_image9(sb)
    nutri_text = Nutrition(sb)

    text = f'''
    {intro_text}
    {details_text}
    {ingredients_text}
    {steps_text}
    {image_url1} {imgalt1}
    {image_url2} {imgalt2}
    {image_url3} {imgalt3}
    {image_url4} {imgalt4}
    {image_url5} {imgalt5}
    {image_url6} {imgalt6}
    {image_url7} {imgalt7}
    {image_url8} {imgalt8}
    {image_url9} {imgalt9}
    {url} {imgalt}
    {nutri_text}
    '''
    return text

# Call the prompt function within the with block
#with SB(headless=True) as sb:
    #text = prompt(sb)