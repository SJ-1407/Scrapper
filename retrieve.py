'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

def fetch_hackernews_data(pages=3):
    base_url = 'https://news.ycombinator.com/'

    for page in range(1, pages + 1):
        url = f'{base_url}?p={page}' if page > 1 else base_url
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.select('.athing')

            for item in news_items:
                title_element = item.select_one('.storylink')

                if title_element:
                    title = title_element.text
                    url = title_element['href']
                    hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
                    posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
                    upvotes = int(item.select_one('.score').text.split()[0])

                    comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
                    comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

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

            db.session.commit()
        else:
            print(f"Failed to fetch data from HackerNews. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)
'''

'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

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
'''

'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

def fetch_hackernews_data(pages=3):
    base_url = 'https://news.ycombinator.com/'

    try:
        for page in range(1, pages + 1):
            url = f'{base_url}?p={page}' if page > 1 else base_url
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.select('.athing')

            for item in news_items:
                process_news_item(item)

        db.session.commit()
        print("HackerNews data fetched and stored successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from HackerNews. Error: {e}")

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

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

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)'''
'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

        print("Extracted Data:", title, url, hacker_news_url, posted_on, upvotes, comments)

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

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)'''

'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

        print("Extracted Data:", title, url, hacker_news_url, posted_on, upvotes, comments)

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

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)'''
'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

        print("Extracted Data:", title, url, hacker_news_url, posted_on, upvotes, comments)

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

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)'''

'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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

def process_news_item(item):
    title_element = item.select_one('.storylink')

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes = int(item.select_one('.score').text.split()[0])

        comments_tag = item.find_next_sibling('tr', class_='athing', recursive=False)
        comments = int(comments_tag.select_one('.subtext').a.text.split()[0]) if comments_tag else 0

        print("Extracted Data:", title, url, hacker_news_url, posted_on, upvotes, comments)

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

if __name__ == '__main__':
    fetch_hackernews_data(pages=3)'''
'''orifginal
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app import db
from application.models import NewsItem

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
            print(f"Failed to fetch data from HackerNews. Error: {e}")'''

'''def process_news_item(item):
    title_element = item.select_one('.title a')  # Adjust the CSS selector based on your HTML structure
    print(title_element)

    if title_element:
        title = title_element.text
        url = title_element['href']
        hacker_news_url = f'https://news.ycombinator.com/item?id={item["id"]}'
        age_element = item.select_one('.age')
        posted_on = datetime.utcfromtimestamp(int(age_element['data-time'])).strftime('%Y-%m-%d %H:%M:%S') if age_element else None

        #posted_on = datetime.utcfromtimestamp(int(item.select_one('.age')['data-time'])).strftime('%Y-%m-%d %H:%M:%S')
        upvotes_element = item.select_one('.score')
        upvotes = int(upvotes_element.text.split()[0]) if upvotes_element else 0

        # Extracting comments count more robustly
        subtext_element = item.select_one('.subtext')
        comments_element = subtext_element.select_one('a[href*="item?id="]') if subtext_element else None
        comments = int(comments_element.text.split()[0]) if comments_element else 0

        # Print the extracted data
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
        print("Title not found")'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from application.models import NewsItem
from application.database import db
#from flask_login import current_user

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

        # Extracting posted_on, upvotes, and comments
        subtext_element = item.find_next('td', class_='subtext')

        # Check if the subtext element is present before trying to extract data
        if subtext_element:
            # Check if the age element is present before trying to extract data
            age_element = subtext_element.find('span', class_='age')
            posted_on = (
                datetime.utcnow() - timedelta(hours=int(age_element.text.split()[0]))
                if age_element
                else None
            )

            # Check if the score element is present before trying to extract data
            score_element = subtext_element.find('span', class_='score')
            upvotes = int(score_element.text.split()[0]) if score_element else 0

            # Extracting comments count more robustly
            comments_element = subtext_element.find('a', string=lambda s: 'comment' in s.lower())
            comments = int(comments_element.text.split()[0]) if comments_element else 0
           
            #user_id = current_user.id if current_user.is_authenticated else 0
           
            # Print the extracted data for debugging
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
                    #user_id=user_id
                    
                )
                db.session.add(new_item)
        else:
            print("Subtext element not found")
            print(item)  # Print the entire item for further debugging
    else:
        print("Title not found")
        print(item)  # Print the entire item for further debugging



if __name__ == '__main__':
    fetch_hackernews_data(pages=3)


