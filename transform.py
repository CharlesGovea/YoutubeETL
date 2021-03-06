import pandas as pd


def clean_regions(data):
    data = data['items']
    cleaned = dict()

    # Create an entry in the dictionary using the region code as key and the name as its value
    for region in data:
        snippet = region['snippet']
        cleaned[snippet['gl']] = snippet['name']

    # Return the data as a dataframe
    cleaned = pd.DataFrame(cleaned.items(), columns=['regionCode', 'regionName'])
    return cleaned


def clean_video_list(data, columns, now, code):
    # Initialize the lists where the clean data will be stored
    keys = list()
    titles = list()
    published = list()
    channels = list()
    views = list()
    likes = list()
    comments = list()
    languages = list()
    extraction = list()
    trended_region = list()

    data = data['items']
    for item in data:
        # For every video in the video list, create a new entry using the videoID as key
        key = item['id']
        keys.append(key)

        snippet = item['snippet']
        statistics = item['statistics']

        # Get the important information from the video's data
        titles.append(snippet['title'])
        published.append(snippet['publishedAt'])
        channels.append(snippet['channelId'])
        views.append(statistics['viewCount'])

        # Not all videos contain all the data for privacy or other reasons, so those values will be set to None
        language = snippet['defaultAudioLanguage'] if 'defaultAudioLanguage' in snippet.keys() else None
        languages.append(language)

        like_count = statistics['likeCount'] if 'likeCount' in statistics.keys() else None
        likes.append(like_count)

        comment_count = statistics['commentCount'] if 'commentCount' in statistics.keys() else None
        comments.append(comment_count)

        extraction.append(now)
        trended_region.append(code)

    # Create a new dataframe using the value of each video as row, and each important feature as column
    values = list(zip(keys, titles, published, channels, views, likes, comments, languages, trended_region, extraction))
    df = pd.DataFrame(values, columns=columns)

    # Return also the set of channels whose video trended
    return df, set(channels)


def clean_channels(data, columns, now):
    # Initialize the lists where the clean data will be stored
    keys = list()
    name = list()
    creation_date = list()
    countries = list()
    views = list()
    subs = list()
    video_count = list()
    extraction = list()

    data = data['items']
    for channel in data:
        # For every channel in the list, create a new entry using its ID as key
        key = channel['id']
        keys.append(key)

        snippet = channel['snippet']
        statistics = channel['statistics']

        # Get the most important information from the channel
        name.append(snippet['title'])
        creation_date.append(snippet['publishedAt'])

        country = snippet['country'] if 'country' in snippet.keys() else None
        countries.append(country)

        views.append(statistics['viewCount'])

        sub = statistics['subscriberCount'] if 'subscriberCount' in statistics.keys() else None
        subs.append(sub)

        video_count.append(statistics['videoCount'])
        extraction.append(now)

    # Create a new dataframe with the clean data
    values = list(zip(keys, name, creation_date, countries, views, subs, video_count, extraction))
    df = pd.DataFrame(values, columns=columns)

    return df
