# YouTube ETL Project

The purpose of this project is to create an ETL pipeline, automated with Airflow.

## Extraction phase
The information is extracted from YouTube using its API. The data in question is the Top 10 videos that appeared in the **Trending** page in the category of _Gaming_ in each country/region on YouTube. To obtain as much useful information for future analysis as possible, the following information is queried using the API:

- The region list containing all the region codes and names on YouTube
- The information and statistics of the Top 10 videos in each region
- The information and statistics of every _unique_ channel whose video trended

This information will be extracted daily.

## Transformation phase
Throughout the extraction process, the data must be cleaned in order to retrieve all the important information and get rid of data that won't be useful for future analysis.
For the purposes of this project, the information that is considered relevant or important are as follows:

- The region codes and names of every region on YouTube
- For every video in the Top 10 in each region:
  - The video's ID 
  - Title of the video 
  - Publication date
  - View count
  - Like count
  - Comment count
  - And, if available, the video's tags and the audio's language
- For every _unique_ channel whose video trended in _one or multiple regions_:
  - The channel's ID
  - Name of the channel
  - Creation date
  - The channel's country/region
  - Total view count
  - Subscriber count
  - Video count

## Load phase
Once cleaned up, the data will be uploaded to Firestore, where it will be stored as documents. The regions will be fixed, since they rarely change, but the videos and channels will be constantly updated.

## Future analysis
Some findings I'm hoping to achieve include but are not limited to:
- Game that trended the most in a region and worldwide
- Channel that trended the most in a region and worldwide
- Compare the view-counts of channels that trended in every region
- Find a correlation between a channel's creation date and the amount of times that they trended
- etc.

The experiment will be repeated in intervals of 1 month, 3 months, 6 months, 9 months and 12 months, to observe how the data changes over time and other interesting observations.