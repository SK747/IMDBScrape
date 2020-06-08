# %%

import numpy as np
import matplotlib.pyplot


from requests import get


from bs4 import BeautifulSoup




# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
# Extract data from individual movie container
url = 'https://www.imdb.com/user/ur83994895/ratings?sort=your_rating,desc&ratingFilter=0&mode=detail&ref_=undefined&lastPosition=0'

while(url):
        
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-detail')
        print(type(movie_containers))
        print(len(movie_containers))
        
        for container in movie_containers:
                name = container.h3.a.text
                names.append(name)
                # The year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                year2 = int(''.join(i for i in year if i.isdigit()))
                years.append(year2)
                # The IMDB rating
                imdb = container.find('span', class_ = 'ipl-rating-star__rating').text
                imdb_ratings.append(imdb)
                
        soup = BeautifulSoup(response.text ,"lxml")
        url = soup.findAll('a', {'class': 'flat-button lister-page-next next-page'})
        print(url)
        if url:
            url = 'https://www.imdb.com' + url[0].get('href')
        else:
            break

        
import pandas as pd
test_df = pd.DataFrame({'movie': names, 'year': years, 'imdb': imdb_ratings
})
test_df

print(test_df)

test_df.to_csv('allmoviesranked.csv')