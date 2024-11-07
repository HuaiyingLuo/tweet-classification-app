# tweet-classification-app

In this project, we will build a tweet classification app using a machine learning pipeline. The model will classify tweets into positive or negative sentiment. 

## File Structure

`app/`

`ml-dev/`
`data/`


## Setup

Set up a conda environment in mle-dev with the following command:

```
cd ml-dev
conda create -n nlp python=3.9
conda activate nlp
```

Install the required packages:

```
conda install jupyter ipykernel
ipython kernel install --user --name=nlp
conda install scikit-learn
conda install nltk
conda install pandas
conda install numpy
```


pip install -r requirements.txt
```


## About the Dataset

In this project, we will use the sentiment140 dataset. This dataset can be found on Kaggle:
[Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

It contains 1,600,000 tweets extracted using the twitter api. The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment .

It contains the following 6 fields:
- target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
- ids: The id of the tweet (2087)
- date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
- flag: The query (lyx). If there is no query, then this value is NO_QUERY.
- user: the user that tweeted (robotickilldozr)
- text: the text of the tweet (Lyx is cool)


