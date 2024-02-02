
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from application.models import NewsItem
from application.database import db


def fetch_hackernews_data(pages=3):
    base_url = 'https://news.ycombinator.com/'

    for page in range(1, pages + 1):
        url = f'{base_url}?p={page}' if page > 1 else base_url
        response = requests.get(url)

        try:
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.select('.athing')

            for item in news_items:
                process_news_item(item)

            db.session.commit()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from HackerNews. Error: {e}")
from datetime import timedelta

from datetime import timedelta

def process_news_item(item):
    title_element = item.select_one('.title a')

    if title_element:
        title = title_element.text
        url = title_element.get('href')
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'

        
        subtext_element = item.find_next('td', class_='subtext')

      
        if subtext_element:
          
            age_element = subtext_element.find('span', class_='age')
            posted_on = (
                datetime.utcnow() - timedelta(hours=int(age_element.text.split()[0]))
                if age_element
                else None
            )

          
            score_element = subtext_element.find('span', class_='score')
            upvotes = int(score_element.text.split()[0]) if score_element else 0

           
            comments_element = subtext_element.find('a', string=lambda s: 'comment' in s.lower())
            comments = int(comments_element.text.split()[0]) if comments_element else 0
           
          
            print("Title:", title)
            print("URL:", url)
            print("Hacker News URL:", hacker_news_url)
            print("Posted On:", posted_on)
            print("Upvotes:", upvotes)
            print("Comments:", comments)

            existing_item = NewsItem.query.filter_by(hacker_news_url=hacker_news_url).first()

            if existing_item:
                existing_item.upvotes = upvotes
                existing_item.comments = comments
                existing_item.posted_on = posted_on
            else:
                new_item = NewsItem(
                    title=title,
                    url=url,
                    hacker_news_url=hacker_news_url,
                    posted_on=posted_on,
                    upvotes=upvotes,
                    comments=comments
                    
                    
                )
                db.session.add(new_item)
        else:
            print("Subtext element not found")
            print(item)  
    else:
        print("Title not found")
        print(item)  



if __name__ == '__main__':
    fetch_hackernews_data(pages=3)

