# Python3 code for movie recommendation based on your emotion

# Import library for web
# scrapping
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

# Main Function for scraping


def main(emotion):

    # IMDb Url for Drama genre of
    # movie against emotion Sad
    if emotion == "Anger":
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    elif emotion in ["Anticipation", "Joy"]:
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif emotion == "Disgust":
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    elif emotion == "Fear":
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    elif emotion == "Sad":
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif emotion == "Surprise":
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    elif emotion == "Trust":
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    # HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")

    return soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})


# Driver Function
if __name__ == '__main__':

    print(
        "Select Your Emotion:\n 1. Anger\n 2. Anticipation\n 3. Disgust\n 4. Fear\n 5. Joy\n 6. Sad\n 7. Surprise\n 8. Trust"
    )
    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0

    if emotion in ["Disgust", "Anger", "Surprise"]:

        for i in a:

            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split('>;')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 11):
                break
            count += 1
