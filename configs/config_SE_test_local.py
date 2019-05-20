##############		variables		##############
##################################################

# Tags file has 'Tags' column and they should be cleaned


project_name = 'StackExchange'

min_date_val = '2015-01-01'
max_date_val = '2019-01-01'

directory = dict(
    files='/Users/habib/Documents/_Courses/_Datasets/_StackExchange/data/CSVs/2019_03_04/',
    save='/Users/habib/Documents/_Courses/_Datasets/_StackExchange/results/test/',
    tags='/Users/habib/Documents/_Courses/_Datasets/_StackExchange/data/CSVs/2019_03_04/',
    mallet='/Users/habib/Documents/_Courses/_Codes/_iNotebook/_LDA/Mallet-master/bin/mallet'
)

template = dict(
    files=dict(
        posts=dict(
            formats=dict(
                file='csv',
                sep=',',
                date='%Y-%m-%dT',
            ),
            cols=dict(
                date='CreationDate',
                id='Id',
                category=None,
                text=['Title', 'Body']
            )
        ),
        comments=dict(
            formats=dict(
                file='csv',
                sep=',',
                date='%Y-%m-%dT',
            ),
            cols=dict(
                date='CreationDate',
                id='Id',
                category=None,
                text=['Text']
            )
        ),
    ),
)

mem = 8000
num_cores = 7
num_topics = 10
LDA_proportion = 4
LDA_iteration_threshold = 2
optimal_LDA_iteration_threshold = 2
start = 4
step = 2
stop = 7
min_keyword_threshold = 5
topic_cutoff_threshold = 0.1

lang_detect=True
progress_bar_allowed = False
zoom_date_on_default_dates = False
date_format = '%Y-%m-%d'

db_file='StackExchange_db_optimal_model-10-10.pickle'
num_sent = 20
TSNE_threshold = 0.20

hist_filenames=[
    'StackExchange_5_coherence_LDA_4_101_4_iter_2000.csv',
    'StackExchange_5_coherence_LDA_6_101_4_iter_2000.csv',
]

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
