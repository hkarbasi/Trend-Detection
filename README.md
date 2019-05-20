Trend-Detection
===============


This project is to find topics and temporal trends in a corpus using **LDA** and **Cox-Stuart** trend test. It is a scalable and parallel framework and it can be used for large dataset as well. 

The entire work has been broken down to 7 python notebooks as following:

### 1. Text preprocssing ###

It takes the text files from different folders set in the config files and checks the following:

  * All files should have the same format.
  * It filters the data based on the date range set in config.
  * With the set of cleaning rules set in config, the text are cleaned.
  * Unigrams of the text are constructed.
  * Porter stemmping is applied.
  * Using the tags set in config, words that are very common in the dataset are encrypted not be tampered with for the rest of the process.
  * Bigrams of the cleaned texts are constructed.
  * Lemmatization (Noun, Verb, Adj and Adv) are used to remove less meaningful words.
  * Texts less than a threshold (like 5 keywords) are removed.
  
### 2. Text preprocssing ###

It creats a SQL database from cleaned text including original text, cleaned text (all_text), lemmatized text that will be enventually used for LDA and finally decoded keywords.


### 3. Param Search ###

It runs multiple LDA with the range of different number of topics in parallel then coherence value of each model is calculated as a metric to find the best optimal model.
 
### 4. Data Analysis (*Preliminary*) ###

This notebook does the following:
 * It plots the coherence value of the models. 
 * It calculates the distribution of category in the dataset.
 * It plots the histogram of word counts per document for each category and overall.
 
 
### 5. Optimal Model ###

It trains the optimal model with the number of topics found in the previous notebook.


### 6. Visulization (*computation*) ###

Due to the intensity of the computation for large dataset, this notebook calculates all of necessary data needed for the next one for visualization. This notebook does the following:

 * Shows the 10 keywords for each topic.
 * Removes the noisy topic weight by removing those topics and normalize the topic weights for each document.
 * Creates a SQL db stroing each document with dominant topic and its respective weight.
 * Stores **K** *(set in config)* top documents for each topic to help with a better labeling of topic
 * Calculates the topic distribution on the prespecified timeframe
 * Caculates the data for TSNE topic visualization
 * Calculates the data for temporal graph for topics
 

### 7. Visulization (*final*)  ###

 * Plots the histogram of each topic in terms of word weight and word count
 * Shows the word cloud of each topic using the top 10 keywords
 * Plots the distribution of dominant topics
 * Plots TSNE 
 * Plots the temporal graph of topics in terms of number of dominant topic and proportional weight per time unit(*daily, weekly* and *monthly*)
 * Calculates trend using Cox-Stuart test with 95% confidence.
 * Plots increasing/decreasing trends
 
This project has been used on StackExchange and Reddit dataset. You can find more explaination on the PDF.
The available notebooks are the result of Reddit.
Both datasets are four years of data; (*1 Jan 2015- 1 Jan 2019*), 
 * Smaller one is StackExchange (DataScience)
 * Larger one is Reddit (9 DataScience Subreddits)


Datasets can be found on ([my Google Drive](https://drive.google.com/open?id=1q8Dvm-54CgLj-bmVxD6i1hvRT_WhYhpV)) and you are welcome to download and experiment with them! :)
 
 
