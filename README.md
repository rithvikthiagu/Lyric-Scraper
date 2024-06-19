# Lyric Webscraper (In Progress)
This repository contains a Python-based webscraper designed to collect and analyze song lyrics. The goal is to gather a substantial dataset of 100,000 songs and search for terms within the lyrics. The project leverages the Genius API, handles pagination, uses multiprocessing for efficiency, and includes sentiment analysis using NLTK.

## Features
- API Integration: Utilizes the Genius API to fetch song data and lyrics.
- Pagination Handling: Manages pagination to collect a large number of songs in batches.
- Error Handling: Includes robust error handling to manage potential API errors and data inconsistencies.
- Data Management: Efficiently stores and processes large datasets, with intermediate results saved to avoid data loss.
- Keyword Search: Analyzes lyrics to search for specific terms, such as "Jim Beam".
- Sentiment Analysis: Uses NLTK's SentimentIntensityAnalyzer to determine the sentiment of lyrics.

## Installation
1. Clone the repository:
 ```sh
   git clone https://github.com/your-username/lyric-webscraper.git
   cd lyric-webscraper
   ```

2. Install the required dependencies:
```sh
  pip install -r requirements.txt
   ```

3. Obtain an API key from Genius and add it to your environment variables:
```sh
  export GENIUS_API_TOKEN='your_genius_api_key'
   ```

## Usage
Run the main script to start the webscraper:
```sh
  python main.py
   ```
The script will fetch song lyrics, search for the specified terms, analyze the sentiment, and print the total number of songs mentioning the terms along with sentiment analysis results.

## Functions Overview

### search_lyrics_with_pagination(query, max_results)
- Search for lyrics with pagination and handle duplicates.

### fetch_lyrics_and_annotations_from_url(args)
- Fetch lyrics and annotations from a Genius song URL and perform sentiment analysis.

### calculate_sentiment(text)
- Calculate sentiment scores using NLTK's SentimentIntensityAnalyzer.

### count_valid_hits(lyric_query, max_results)
= Search and count valid hits for a specific lyric query, and perform sentiment analysis on the annotations.

### write_titles_to_file(titles, filename)
- Write song titles to a file
