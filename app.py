# from lyricsgenius import Genius
# import time
# import re
# import requests
# from bs4 import BeautifulSoup

# # Your Genius API token
# GENIUS_API_TOKEN = '7ejGbZnQIRxT2EuRx9HQ9jIf_-UQWIWoTRue8s8pBS8k9aiRH1vIWoTyykNk9RwL'
# genius = Genius(GENIUS_API_TOKEN)

# # Function to search for lyrics with pagination and handle duplicates
# def search_lyrics_with_pagination(query, max_results=50):
#     current_page = 1
#     all_hits = []
#     seen_titles = set()

#     while len(all_hits) < max_results:
#         try:
#             request = genius.search_lyrics(query, per_page=10, page=current_page)
#             if 'sections' not in request or len(request['sections']) == 0:
#                 break
            
#             hits = request['sections'][0]['hits']
#             if not hits:
#                 break
            
#             for hit in hits:
#                 title = hit['result']['title']
#                 if title not in seen_titles:
#                     seen_titles.add(title)
#                     all_hits.append(hit)
            
#             current_page += 1

#             if len(hits) < 10:  # Less than 10 hits means it's the last page
#                 break

#             # Optional: Add a short delay to avoid hitting rate limits
#             #time.sleep(1)
        
#         except Exception as e:
#             print(f"Error on page {current_page}: {e}")
#             #time.sleep(5)  # Wait before retrying to handle rate limits or temporary issues
#             continue
    
#     return all_hits[:max_results]

# # Function to fetch the lyrics from a Genius song URL
# def fetch_lyrics_from_url(url):
#     page = requests.get(url)
#     html = BeautifulSoup(page.text, 'html.parser')
#     lyrics_div = html.find('div', class_='lyrics')
#     if lyrics_div:
#         return lyrics_div.get_text()
#     else:
#         # Handle the newer Genius page structure
#         lyrics_div = html.find_all('div', class_=re.compile('Lyrics__Container'))
#         lyrics = '\n'.join([div.get_text(separator='\n') for div in lyrics_div])
#         return lyrics

# # Function to find and print the line containing the given lyric
# def find_lyric_line(lyrics, query):
#     for line in lyrics.split('\n'):
#         if re.search(query, line, re.IGNORECASE):
#             return line
#     return None

# # Search for songs with the lyrics "Rivulets descend my plastic smile" and handle pagination
# lyric_query = "Jack Daniel's"
# print(f"Searching for songs with lyrics '{lyric_query}':")
# hits = search_lyrics_with_pagination(lyric_query, max_results=50)

# valid_hits = 0
# for hit in hits:
#     title = hit['result']['title']
#     song_url = hit['result']['url']
#     lyrics = fetch_lyrics_from_url(song_url)
    
#     if lyrics:
#         lyric_line = find_lyric_line(lyrics, lyric_query)
#         if lyric_line:
#             #print(f"Title: {title}\nLyric Line: {lyric_line}\n")
#             valid_hits += 1

# print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")



# from lyricsgenius import Genius
# import time
# import re
# import requests
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt

# # Your Genius API token
# GENIUS_API_TOKEN = '7ejGbZnQIRxT2EuRx9HQ9jIf_-UQWIWoTRue8s8pBS8k9aiRH1vIWoTyykNk9RwL'
# genius = Genius(GENIUS_API_TOKEN)

# # Function to search for lyrics with pagination and handle duplicates
# def search_lyrics_with_pagination(query, max_results=200):
#     current_page = 1
#     all_hits = []
#     seen_titles = set()

#     while len(all_hits) < max_results:
#         try:
#             request = genius.search_lyrics(query, per_page=10, page=current_page)
#             if 'sections' not in request or len(request['sections']) == 0:
#                 break
            
#             hits = request['sections'][0]['hits']
#             if not hits:
#                 break
            
#             for hit in hits:
#                 title = hit['result']['title']
#                 if title not in seen_titles:
#                     seen_titles.add(title)
#                     all_hits.append(hit)
            
#             current_page += 1

#             if len(hits) < 10:  # Less than 10 hits means it's the last page
#                 break

#             # Optional: Add a short delay to avoid hitting rate limits
#             time.sleep(1)
        
#         except Exception as e:
#             print(f"Error on page {current_page}: {e}")
#             time.sleep(1)  # Wait before retrying to handle rate limits or temporary issues
#             continue
    
#     return all_hits[:max_results]

# # Function to fetch the lyrics from a Genius song URL
# def fetch_lyrics_from_url(url):
#     page = requests.get(url)
#     html = BeautifulSoup(page.text, 'html.parser')
#     lyrics_div = html.find('div', class_='lyrics')
#     if lyrics_div:
#         return lyrics_div.get_text()
#     else:
#         # Handle the newer Genius page structure
#         lyrics_div = html.find_all('div', class_=re.compile('Lyrics__Container'))
#         lyrics = '\n'.join([div.get_text(separator='\n') for div in lyrics_div])
#         return lyrics

# # Function to find and print the line containing the given lyric
# def find_lyric_line(lyrics, query):
#     for line in lyrics.split('\n'):
#         if re.search(query, line, re.IGNORECASE):
#             return line
#     return None

# # Function to search and count valid hits for a specific lyric query
# def count_valid_hits(lyric_query, max_results=200):
#     print(f"Searching for songs with lyrics '{lyric_query}':")
#     hits = search_lyrics_with_pagination(lyric_query, max_results)
    
#     valid_hits = 0
#     for hit in hits:
#         title = hit['result']['title']
#         song_url = hit['result']['url']
#         lyrics = fetch_lyrics_from_url(song_url)
        
#         if lyrics:
#             lyric_line = find_lyric_line(lyrics, lyric_query)
#             if lyric_line:
#                 #print(f"Title: {title}\nLyric Line: {lyric_line}\n")
#                 valid_hits += 1

#     print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")
#     return valid_hits

# # Search for the terms "Jim Beam" and "Courvoisier"
# # terms = ["Jim Beam", "Courvoisier"]
# terms = ["Jack Daniel's"]
# valid_hits = [count_valid_hits(term) for term in terms]

# # Plot the results using matplotlib
# plt.bar(terms, valid_hits, color=['blue', 'orange'])
# plt.xlabel('Terms')
# plt.ylabel('Valid Hits')
# plt.title('Comparison of Songs Containing Specific Terms')
# plt.show()

# from lyricsgenius import Genius
# import time
# import re
# import requests
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt

# # Your Genius API token
# GENIUS_API_TOKEN = '7ejGbZnQIRxT2EuRx9HQ9jIf_-UQWIWoTRue8s8pBS8k9aiRH1vIWoTyykNk9RwL'
# genius = Genius(GENIUS_API_TOKEN)

# # Function to search for lyrics with pagination and handle duplicates
# def search_lyrics_with_pagination(query, max_results=100):
#     current_page = 1
#     all_hits = []
#     seen_titles = set()

#     while len(all_hits) < max_results:
#         try:
#             request = genius.search_lyrics(query, per_page=10, page=current_page)
#             if 'sections' not in request or len(request['sections']) == 0:
#                 break
            
#             hits = request['sections'][0]['hits']
#             if not hits:
#                 break
            
#             for hit in hits:
#                 if hit['type'] == 'song':  # Only consider hits that are songs
#                     title = hit['result']['title']
#                     if title not in seen_titles:
#                         seen_titles.add(title)
#                         all_hits.append(hit)
            
#             current_page += 1

#             if len(hits) < 10:  # Less than 10 hits means it's the last page
#                 break

#             # Optional: Add a short delay to avoid hitting rate limits
#             time.sleep(1)
        
#         except Exception as e:
#             print(f"Error on page {current_page}: {e}")
#             time.sleep(1)  # Wait before retrying to handle rate limits or temporary issues
#             continue
    
#     return all_hits[:max_results]

# # Function to fetch the lyrics from a Genius song URL
# def fetch_lyrics_from_url(url):
#     page = requests.get(url)
#     html = BeautifulSoup(page.text, 'html.parser')
#     lyrics_div = html.find('div', class_='lyrics')
#     if lyrics_div:
#         return lyrics_div.get_text()
#     else:
#         # Handle the newer Genius page structure
#         lyrics_div = html.find_all('div', class_=re.compile('Lyrics__Container'))
#         lyrics = '\n'.join([div.get_text(separator='\n') for div in lyrics_div])
#         return lyrics

# # Function to find and print the line containing the given lyric
# def find_lyric_line(lyrics, query):
#     for line in lyrics.split('\n'):
#         if re.search(query, line, re.IGNORECASE):
#             return line
#     return None

# # Function to search and count valid hits for a specific lyric query
# def count_valid_hits(lyric_query, max_results=100):
#     print(f"Searching for songs with lyrics '{lyric_query}':")
#     hits = search_lyrics_with_pagination(lyric_query, max_results)
    
#     valid_hits = 0
#     for hit in hits:
#         title = hit['result']['title']
#         song_url = hit['result']['url']
#         lyrics = fetch_lyrics_from_url(song_url)
        
#         if lyrics:
#             lyric_line = find_lyric_line(lyrics, lyric_query)
#             if lyric_line:
#                 #print(f"Title: {title}\nLyric Line: {lyric_line}\n")
#                 valid_hits += 1

#     print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")
#     return valid_hits

# # Search for the terms "Jim Beam" and "Courvoisier"
# terms = [ "Jack Daniel's"]
# valid_hits = [count_valid_hits(term) for term in terms]

# # Plot the results using matplotlib
# plt.bar(terms, valid_hits, color=['blue', 'orange'])
# plt.xlabel('Terms')
# plt.ylabel('Valid Hits')
# plt.title('Comparison of Songs Containing Specific Terms')
# plt.show()

# from lyricsgenius import Genius
# import time
# import re
# import requests
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
# from multiprocessing import Pool

# # Your Genius API token
# GENIUS_API_TOKEN = '7ejGbZnQIRxT2EuRx9HQ9jIf_-UQWIWoTRue8s8pBS8k9aiRH1vIWoTyykNk9RwL'
# genius = Genius(GENIUS_API_TOKEN)

# # Function to search for lyrics with pagination and handle duplicates
# def search_lyrics_with_pagination(query, max_results=1):
#     current_page = 1
#     all_hits = []
#     seen_titles = set()

#     while len(all_hits) < max_results:
#         try:
#             request = genius.search_lyrics(query, per_page=50, page=current_page)
#             if 'sections' not in request or len(request['sections']) == 0:
#                 break
            
#             hits = request['sections'][0]['hits']
#             if not hits:
#                 break
            
#             print_songs_on_page(hits, current_page)  # Print songs on the current page
            
#             for hit in hits:
#                 if hit['type'] == 'song':  # Only consider hits that are songs
#                     title = hit['result']['title']
#                     if title not in seen_titles:
#                         seen_titles.add(title)
#                         all_hits.append(hit)
            
#             current_page += 1

#             # if len(hits) < 1:  # Less than 10 hits means it's the last page
#             #     break

#             # Optional: Add a short delay to avoid hitting rate limits
#             time.sleep(5)
        
#         except Exception as e:
#             print(f"Error on page {current_page}: {e}")
#             time.sleep(1)  # Wait before retrying to handle rate limits or temporary issues
#             continue
    
#     print(f"Total hits retrieved: {len(all_hits)}")
#     return all_hits[:max_results]

# # Function to print song titles on the current page
# def print_songs_on_page(hits, page_number):
#     print(f"\nSongs on page {page_number}:")
#     for hit in hits:
#         if hit['type'] == 'song':
#             title = hit['result']['title']
#             print(f"- {title}")

# # Function to fetch the lyrics from a Genius song URL
# def fetch_lyrics_from_url(hit):
#     try:
#         url = hit['result']['url']
#         page = requests.get(url)
#         html = BeautifulSoup(page.text, 'html.parser')
#         lyrics_div = html.find('div', class_='lyrics')
#         if lyrics_div:
#             return hit['result']['title'], lyrics_div.get_text()
#         else:
#             # Handle the newer Genius page structure
#             lyrics_div = html.find_all('div', class_=re.compile('Lyrics__Container'))
#             lyrics = '\n'.join([div.get_text(separator='\n') for div in lyrics_div])
#             return hit['result']['title'], lyrics
#     except Exception as e:
#         print(f"Error fetching lyrics for {hit['result']['title']}: {e}")
#         return hit['result']['title'], None

# # Function to find and print the line containing the given lyric
# def find_lyric_line(lyrics, query):
#     for line in lyrics.split('\n'):
#         if re.search(query, line, re.IGNORECASE):
#             return line
#     return None

# # Function to write song titles to a file
# def write_titles_to_file(titles, filename="checked_songs.txt"):
#     with open(filename, 'w', encoding='utf-8') as file:
#         for title in titles:
#             file.write(f"{title}\n")

# # Function to search and count valid hits for a specific lyric query
# def count_valid_hits(lyric_query, max_results=100000):
#     print(f"Searching for songs with lyrics '{lyric_query}':")
#     hits = search_lyrics_with_pagination(lyric_query, max_results)
    
#     valid_hits = 0
#     checked_titles = []

#     # Use multiprocessing to fetch lyrics in parallel
#     with Pool(5) as pool:
#         results = pool.map(fetch_lyrics_from_url, hits)
    
#     for title, lyrics in results:
#         checked_titles.append(title)
#         if lyrics:
#             lyric_line = find_lyric_line(lyrics, lyric_query)
#             if lyric_line:
#                 print(f"Title: {title}\nLyric Line: {lyric_line}\n")
#                 valid_hits += 1

#     # Write all checked titles to the file after processing all hits
#     write_titles_to_file(checked_titles, filename=f"checked_songs_{lyric_query.replace(' ', '_')}.txt")
#     print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")
#     return valid_hits

# if __name__ == '__main__':
#     # Search for the terms "Jim Beam" and "Courvoisier"
#     terms = ["Jim Beam","Jack Daniels", "Makers Mark", "Bookers", "Old Crow", "Knob Creek", "Sqrrl", "Little Book", "Overholt", "Clermont Steep", "Old Grand Dad", "Basil Hayden", "Kessler", "Hardins Creek"]
#     valid_hits = [count_valid_hits(term) for term in terms]

#     # Plot the results using matplotlib
#     plt.bar(terms, valid_hits, color=['blue', 'orange'])
#     plt.xlabel('Terms')
#     plt.ylabel('Valid Hits')
#     plt.title('Comparison of Songs Containing Specific Terms')
#     plt.show()

from lyricsgenius import Genius
import time
import re
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords



# Your Genius API token
GENIUS_API_TOKEN = '7ejGbZnQIRxT2EuRx9HQ9jIf_-UQWIWoTRue8s8pBS8k9aiRH1vIWoTyykNk9RwL'
genius = Genius(GENIUS_API_TOKEN)
sid = SentimentIntensityAnalyzer()
sentiment_lol = []



def calculate_sentiment(text):
    scores = sid.polarity_scores(text)
    #print(scores)
    compound_score = scores['compound']
    
    if compound_score >= 0.05:
        sentiment_label = 'Positive'
    elif compound_score <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    #print(sentiment_label)
    return sentiment_label

def calculate_average(text):
    scores = sid.polarity_scores(text)
    compound_score = scores['compound']
    return compound_score


# Function to search for lyrics with pagination and handle duplicates
def search_lyrics_with_pagination(query, max_results=100000):
    current_page = 1
    all_hits = []
    seen_titles = set()

    while len(all_hits) < max_results:
        try:
            request = genius.search_lyrics(query, per_page=50, page=current_page)
            if 'sections' not in request or len(request['sections']) == 0:
                break
            
            hits = request['sections'][0]['hits']
            if not hits:
                break
            
            #print_songs_on_page(hits, current_page)  # Print songs on the current page
            
            for hit in hits:
                if hit['type'] == 'song':  # Only consider hits that are songs
                    title = hit['result']['title']
                    if title not in seen_titles:
                        seen_titles.add(title)
                        all_hits.append(hit)
            
            current_page += 1

            # Optional: Add a short delay to avoid hitting rate limits
            time.sleep(5)
        
        except Exception as e:
            print(f"Error on page {current_page}: {e}")
            time.sleep(1)  # Wait before retrying to handle rate limits or temporary issues
            continue
    
    print(f"Total hits retrieved: {len(all_hits)}")
    return all_hits[:max_results]

# Function to print song titles on the current page
def print_songs_on_page(hits, page_number):
    #print(f"\nSongs on page {page_number}:")
    for hit in hits:
        if hit['type'] == 'song':
            title = hit['result']['title']
            #print(f"- {title}")

def fetch_lyrics_and_annotations_from_url(args):
    sentiment_scores = []
    hit, term = args  # Unpack the tuple containing hit and term
    sentiment_labels = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    count = 0
    output_file = f"{term.replace(' ', '_')}_annotations.txt"  # Dynamic output file name based on the current term
    try:
        url = hit['result']['url']
        page = requests.get(url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics_div = html.find('div', class_='lyrics')
        if lyrics_div:
            lyrics = lyrics_div.get_text()
        else:
            # Handle the newer Genius page structure
            lyrics_div = html.find_all('div', class_=re.compile('Lyrics__Container'))
            lyrics = '\n'.join([div.get_text(separator='\n') for div in lyrics_div])
        
        annotations = genius.song_annotations(hit['result']['id'])
        
        # Check if the lyrics contain the term
        if re.search(term, lyrics, re.IGNORECASE):
            count = count + 1
            with open(output_file, 'a', encoding='utf-8') as file:
                for annotation in annotations:
                    #print(len(annotations))
                    annotated_lyric = annotation[0]
                    annotation_comment = annotation[1][0][0] if annotation[1] else None
                    
                    if annotated_lyric and term and annotated_lyric.lower().find(term.lower()) != -1:
                        file.write(f"\nAnnotated Lyric: {annotated_lyric}\nAnnotation Comment: {annotation_comment}\n\n")
                        stop_words = set(stopwords.words('english'))
                        filtered_comment = ' '.join([word for word in annotation_comment.split() if word.lower() not in stop_words])
                        # Calculate sentiment score for the filtered annotation comment
                        sentiment_score = calculate_sentiment(filtered_comment)
                        sentiment_labels[sentiment_score] += 1
                        sentiment_lol.append(sentiment_score)
                        sentiment_value = calculate_average(filtered_comment)
                        file.write(f"Filtered Comment: {filtered_comment}\nSentiment Score: {sentiment_score}\nSentiment Value: {sentiment_value}\n")
        
        #print(len(sentiment_scores))
        labels = sentiment_labels.keys()
                
       
        return hit['result']['title'], lyrics, annotations
    except Exception as e:
        print(f"Error fetching lyrics and annotations for {hit['result']['title']}: {e}")
        return hit['result']['title'], None, None

# # Function to search and count valid hits for a specific lyric query
# def count_valid_hits(lyric_query, max_results=100):
#     print(f"Searching for songs with lyrics '{lyric_query}':")
#     hits = search_lyrics_with_pagination(lyric_query, max_results)
#     #print(len(hits))
#     sentiment_labels = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    
#     valid_hits = 0
#     checked_titles = []
#     hit_titles = []
#     total_annotations_checked = 0
#     # Use multiprocessing to fetch lyrics and annotations in parallel
#     with Pool(5) as pool:
#         results = pool.map(fetch_lyrics_and_annotations_from_url, [(hit, lyric_query) for hit in hits])

#     sentiment_scores = []
#     average_sentiment = []
#     for title, lyrics, annotations in results:
#         checked_titles.append(title)
#         if lyrics and annotations:
#             valid_hits += 1
#             hit_titles.append(title)
#             # print(f"Title: {title}\nLyrics: {lyrics}\nAnnotations: {annotations}\n")
#             #print(len(results))

#             # Calculate average sentiment score for annotations of each song
            
#             for annotation in annotations:
#                 if annotation[1]:
#                     annotation_comment = annotation[1][0][0]
#                     stop_words = set(stopwords.words('english'))
#                     filtered_comment = ' '.join([word for word in annotation_comment.split() if word.lower() not in stop_words])
#                     sentiment_score = calculate_sentiment(filtered_comment)
#                     average_sent = calculate_average(filtered_comment)
#                     sentiment_scores.append(sentiment_score)
#                     average_sentiment.append(average_sent)
#                     sentiment_labels[sentiment_score] += 1
#                     print(f"Title: {title}, Annotation Comment: {annotation_comment}, Sentiment Score: {sentiment_score}")
#                     total_annotations_checked += 1
#                     print(f"Total hits retrieved: {len(hit_titles)}")
#                     print(f"Total songs checked: {len(checked_titles)}")
#                     print(f"Total annotation comments' scores checked: {total_annotations_checked}")
#     sum = 0
#     for score in average_sentiment:
#         #print(score)
#         sum = sum + score

#     average = sum / len(average_sentiment)
#     #print (average)
#     #print(len(sentiment_scores))
#       # Plot sentiment scores
#     plt.scatter(range(len(average_sentiment)), average_sentiment)
#     plt.xlabel(lyric_query)
#     plt.ylabel('Sentiment Scores')
#     plt.title('Sentiment Scores Distribution')
#     plt.show()

#     labels = sentiment_labels.keys()
#     frequencies = sentiment_labels.values()
#     plt.bar(labels, frequencies)
#     plt.xlabel('Sentiment Labels')
#     plt.ylabel('Frequency')
#     plt.title('Sentiment Label Frequencies')
#     plt.show()

#     # Calculate average sentiment score
#     if sentiment_scores:
#         #print(sentiment_scores)
#         most_frequent_sentiment = max(set(sentiment_scores), key=sentiment_scores.count)
#         print(f"Most frequent sentiment: {most_frequent_sentiment}")

#     # Write all checked titles to the file after processing all hits
#     write_titles_to_file(hit_titles, filename=f"checked_songs_{lyric_query.replace(' ', '_')}.txt")
#     print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")
#     return valid_hits, average_sentiment

def count_valid_hits(lyric_query, max_results=100000):
    print(f"Searching for songs with lyrics '{lyric_query}':")
    hits = search_lyrics_with_pagination(lyric_query, max_results)
    sentiment_labels = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    
    valid_hits = 0
    checked_titles = []
    hit_titles = []
    total_annotations_checked = 0
    # Use multiprocessing to fetch lyrics and annotations in parallel
    with Pool(5) as pool:
        results = pool.map(fetch_lyrics_and_annotations_from_url, [(hit, lyric_query) for hit in hits])

    sentiment_scores = []
    average_sentiment = []
    for title, lyrics, annotations in results:
        checked_titles.append(title)
        if lyrics and annotations:
            valid_hits += 1
            hit_titles.append(title)
            
            # Check if any annotation matches the lyrics before performing sentiment analysis
            for annotation in annotations:
                annotated_lyric = annotation[0]
                annotation_comment = annotation[1][0][0] if annotation[1] else None
                
                if annotated_lyric and lyric_query and annotated_lyric.lower().find(lyric_query.lower()) != -1:
                    stop_words = set(stopwords.words('english'))
                    filtered_comment = ' '.join([word for word in annotation_comment.split() if word.lower() not in stop_words])
                    sentiment_score = calculate_sentiment(filtered_comment)
                    average_sent = calculate_average(filtered_comment)
                    sentiment_scores.append(sentiment_score)
                    average_sentiment.append(average_sent)
                    sentiment_labels[sentiment_score] += 1
                    total_annotations_checked += 1

    sum = 0
    for score in average_sentiment:
        print(score)
        sum = sum + score

    average = sum / len(average_sentiment)
    print (average)

    # Plot sentiment scores, similar to what you did in fetch_lyrics_and_annotations_from_url
    # Plot the sentiment label frequencies
    labels = sentiment_labels.keys()
    frequencies = sentiment_labels.values()
    plt.bar(labels, frequencies)
    plt.xlabel('Sentiment Labels')
    plt.ylabel('Frequency')
    plt.title('Sentiment Label Frequencies')
    for i, value in enumerate(frequencies):
        plt.text(i, value + 0.1, str(value), ha='center')
    plt.show()

    # Optionally, you can also calculate average sentiment scores and plot them
    if sentiment_scores:
        most_frequent_sentiment = max(set(sentiment_scores), key=sentiment_scores.count)
        print(f"Most frequent sentiment: {most_frequent_sentiment}")

    write_titles_to_file(hit_titles, filename=f"checked_songs_{lyric_query.replace(' ', '_')}.txt")
    print(f"\nFound {valid_hits} songs with lyrics containing '{lyric_query}' out of {len(hits)} total results")
    return valid_hits, average_sentiment
 


# Function to write song titles to a file
def write_titles_to_file(titles, filename="checked_songs.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(f"{title}\n")

if __name__ == '__main__':
    terms = ["Buffalo Trace", "Four Roses"]
    valid_hits_and_sentiment = [count_valid_hits(term) for term in terms]

    # Plot the results using matplotlib for valid hits
    valid_hits = [hits for hits, _ in valid_hits_and_sentiment]
    plt.bar(terms, valid_hits, color=['blue', 'orange'])
    plt.xlabel('Terms')
    plt.ylabel('Valid Hits')
    plt.title('Comparison of Songs Containing Specific Terms')
    plt.show()

    # Plot the average sentiment scores
    for term, (_, sentiment_scores) in zip(terms, valid_hits_and_sentiment):
        plt.bar(term, sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0, color='green')
        plt.xlabel('Terms')
        plt.ylabel('Average Sentiment Score')
        plt.title(f'Average Sentiment Score for Term "{term}"')
        plt.show()

    # Calculate average sentiment for each term
