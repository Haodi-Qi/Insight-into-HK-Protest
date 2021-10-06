# Insight-into-HK-Protest
Computational Social Analytics Project - An insight into Hong Kong Protest

Disclaimer: The project is solely for research and academic purpose; the data is analysed in a subjective manner and the findings do not represent any of the team members' or supervisor's opinions. 

This project is carried out under SMU IS434 Social Analytics and Application in AY2019-2020 Semester 1. The topic of the project is to understand public opinions and sentiment on social media platforms and retrieve insights that may be valuable to researchers and news agencies. 

## Data ##
The data is scaped from Reddit and Twitter using their respective APIs. 

The twitter data ranges from 24-09-2019 to 30-10-2019, with a total of 150,889 tweets. Relevant keywords were used during the crawling; different keywords were used when certain events occurred. 

The Reddit data ranges from 26-09-2019 to 29-10-2019. The subreddit data is scraped daily based on the Reddit 5 sorting method: new, hot, controversial, rising and top. Unfortunatebly, the data file is missing. 

Data filtering and processing were done before the analysis. Note that only English content is analyzed in this project.

## Text Analysis 
Two main text analysis were carried out: popular words extraction and sentiment analysis.

Popular words (N grams) were extracted and visualized using Word Clouds. Sentiment analysis was done using VADER sentiment analysis. 

The analysis results were combined to discover more insights. Time-series anslysis was carried out to observe overall sentiment changes over times and sentiment related to particular keywords over time.

## Network Analysis
Social network analysis was carried out on Twitter data. The nodes are the users and edges if there was a reply/retweet between two users. The network was visualized using Gephi, an open-sourced software. 

Social networks were visualized on a daily basis and key users were identified based on various centrality values. We went to check the twitter profiles of the identified users and analyzed their roles and impacts in the social media in HK protest.  

## Final deliverables 

The final deliverables are one report of the entire project including how we scraped data, how we processed them and the findings, one slide deck for our presentation, and one poster to showcase our project.

The tools and technology used are Twitter Streaming API and PRAW (Python Reddit API Wrapper) for data scraping; NLTK, Gensim, Textblob, WordCloud for text analysis; Networkx and Gephi for network analysis and visualization.

We also published our project and findings on the website https://thesupremepresses.wordpress.com/. 

Credit to Team members: BU Wende, JIANG Hanyu, ZHANG Chengzi; Supervisor: Kyong Jin Shim
