# %%

import numpy as np
import matplotlib.pyplot

from time import sleep
from random import randint



from requests import get

from bs4 import BeautifulSoup


pages = [str(i*50) for i in range(0,9)]

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for page in pages:
        response = get('https://www.imdb.com/search/title/?my_ratings=restrict&sort=year,asc&start=' + page + '51&ref_=adv_nxt')
        
        sleep(randint(1,2))
        
        html_soup = BeautifulSoup(response.text, 'html.parser')
        
        movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

        for container in movie_containers:
                
# If the movie has Metascore, then extract:
                if container.find('div', class_ = 'ratings-metascore') is not None:
                # The name
                        name = container.h3.a.text
                        names.append(name)
                # The year
                        year = container.h3.find('span', class_ = 'lister-item-year').text
                        year2 = int(''.join(i for i in year if i.isdigit()))
                        years.append(year2)
                # The IMDB rating
                        imdb = float(container.strong.text)
                        imdb_ratings.append(imdb)
                # The Metascore
                        m_score = container.find('span', class_ = 'metascore').text
                        metascores.append(int(m_score))
                # The number of votes
                        vote = container.find('span', attrs = {'name':'nv'})['data-value']
                        votes.append(vote)
        
import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes,
})
test_df

