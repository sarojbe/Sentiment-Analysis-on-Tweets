from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re
import string

# import os


def sampleDataParse():
    stop_words = stopwords.words("english")
    # add custom words here
    stop_words.extend(["iculike", "shit", "bullshit", "hmmm"])

    df = pd.read_excel("sample_data.xlsx")

    # keep orginal PD series, just in case
    df["tweet"] = df["text"].copy()

    # remove  URL from tweets
    def delURL(tweet):
        clean = " ".join(re.sub(r"http[^\s]+", "", tweet).split())
        return clean

    df["tweet"] = df["tweet"].apply(lambda tweet: delURL(str(tweet)))

    # remove username and hashtags from tweets
    def delusername(tweet):
        clean = " ".join(re.sub(r"(@[A-Za-z0-9]+)|(#[a-zA-Z0-9]+)", "", tweet).split())
        return clean

    df["tweet"] = df["tweet"].apply(lambda tweet: delusername(str(tweet)))

    # remove punctuations
    def remove_punc(text):
        no_punc = "".join([x for x in text if x not in string.punctuation])
        return no_punc

    df["tweet"] = df["tweet"].apply(lambda x: remove_punc(x))
    df["tweet"] = df["tweet"].str.lower()
    return df["tweet"].head()
