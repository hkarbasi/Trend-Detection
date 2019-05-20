##############		library installation		##############
##############################################################

# !pip install pandarallel --user
# !conda install -n lda -c conda-forge spacy joblib nltk matplotlib altair vega_datasets notebook vega vega3
#                                       selenium gensim wordcloud papermill dask langdetect sqlalchemy
# !pip install spacy-langdetect


# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
# !python3 -m spacy download en
# OR
# pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz

# import nltk
# nltk.download('stopwords')


##############		Imports		##############
##############################################

import gc
import pandas as pd
from pandas.plotting import register_matplotlib_converters

import multiprocessing
# We must import this explicitly, it is not imported by the top-level
# multiprocessing module.
import multiprocessing.pool
from multiprocessing import Pool
import os, sys, getopt, copy, importlib
import pickle
import nltk
# nltk.download('stopwords')
# NLTK Stop words
import time
from sqlalchemy import create_engine
import errno

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from langdetect import detect_langs
from langdetect.detector_factory import *

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import re
from datetime import datetime, timezone, timedelta
import string
from pprint import pprint

from multiprocessing import Lock
# from joblib import Parallel, delayed
from pandarallel import pandarallel
import dask.dataframe as dd
from dask.multiprocessing import get
import signal
import requests
from requests.adapters import HTTPAdapter

# spacy for lemmatization
import spacy
from spacy_langdetect import LanguageDetector

from IPython.display import display, HTML, Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
import matplotlib
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import matplotlib.ticker as plticker

from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
from bokeh.io import output_notebook
import bokeh.plotting as bp
from bokeh.models import HoverTool
from bokeh.plotting import save
import altair as alt

from scipy.stats import binom
from sklearn.manifold import TSNE

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Plotting tools
# import pyLDAvis
# import pyLDAvis.gensim  # don't skip this

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
