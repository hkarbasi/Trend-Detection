##############		variables		##############
##################################################

# Tags file has 'Tags' column and they should be cleaned
# Make sure that Mallet JVM has enough memory

project_name = 'Reddit'

min_date_val = '2015-01-01'
max_date_val = '2019-01-01'

directory = dict(
    files='/Users/habib/Documents/_Courses/_Datasets/_Reddit/data/test/',
    save='/Users/habib/Documents/_Courses/_Datasets/_Reddit/data/_results/',
    tags='/Users/habib/Documents/_Courses/_Datasets/_StackExchange/data/CSVs/2019_03_04/',
    mallet='/Users/habib/Documents/_Courses/_Codes/_iNotebook/Mallet/mallet-2.0.8/bin/mallet'
)

template = dict(
    files=dict(
        submissions=dict(
            formats=dict(
                file='csv',
                sep=',',
                date='timestamp',  # 'timestamp' or '%y-%m-%d'
            ),
            cols=dict(
                date='created_utc',
                id='id',
                category='subreddit',
                text=['title', 'selftext']
            )
        ),
        comments=dict(
            formats=dict(
                file='csv',
                sep=',',
                date='timestamp',
            ),
            cols=dict(
                date='created_utc',
                id='id',
                category='subreddit',
                text=['body']
            )
        ),
    ),
)

mem = 8000
num_cores = 7
num_topics = 62
LDA_iteration_threshold = 10
optimal_LDA_iteration_threshold = 1000
start = 4
step = 2
stop = 10
no_below = 2 # number of documents at least
no_above = 0.6  # % of the documents
min_keyword_threshold = 5
topic_cutoff_threshold = 0.1

lang_detect=True
progress_bar_allowed = False
zoom_date_on_default_dates = False
date_format = '%Y-%m-%d'

params = [
    "num_cores",
    "mem",
    "start",
    "stop",
    "step",
    "num_topics",
    "LDA_iteration_threshold",
    "optimal_LDA_iteration_threshold",
]

replacements = [
    # Remove [character] 
    ('\[.*?\]', ' '),

    # Remove Emails
    ('\S*@\S*\s?', ' '),

    # Remove @text
    ('@\S+', ' '),

    # Remove new line characters
    ('\s+', ' '),

    # Remove <code> ... </code>
    ('<code>[\S*\s*]*?</code>', ' '),

    # Remove <string>
    ('<.*?>', ' '),

    # Remove $ ... $
    ('$.*?$', ' '),

    # Remove $...
    ('$\S+', ' '),

    # Remove &...
    ('&\S+', ' '),

    # Remove URL)
    ('(http.*?)', ' '),

    # Remove URL
    ('http\S+', ' '),

    # Remove subreddit /r/
    ('/r/', ' '),

    # Remove c:...
    ('c:\S+', ' '),

    # Remove /...
    ('/S+', ' '),

]

tags_dict = None
tags = dict(
    name='tags.csv',
    col_name='TagName',
    extra=[
        'data-science',
        'big-data',
        'z-score',
        't-score',
        'datasets',
        'images',
        'buzzword',
        'buzzwords',
        'vizword',
        'vizwords',
        'buzzword',
        'buzzwords',
        'buzzword',
        'buzz-word',
        'buzz-words',
    ]
)

stop_words_extensions = [
    'from',
    'however',
    'subject',
    're',
    'edu',
    'use',
    'would',
    'could',
    'should'
]

topic_labels = list(range(1, 100))

num_dict = {0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
            }
