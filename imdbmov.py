# %%

import numpy as np
import matplotlib.pyplot


from requests import get


from bs4 import BeautifulSoup


# test

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
# Extract data from individual movie container
url = ''

while(url):
        
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
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
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)
                
        soup = BeautifulSoup(response.text ,"lxml")
        url = soup.findAll('a', {'class': 'lister-page-next next-page'})
        if url:
            url = 'https://www.imdb.com' + url[0].get('href')
        else:
            break

        
import pandas as pd
test_df = pd.DataFrame({'movie': names, 'year': years, 'imdb': imdb_ratings
})
test_df

print(test_df)

test_df.to_csv('1800movies.csv')