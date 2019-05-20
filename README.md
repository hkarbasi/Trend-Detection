# Trend-Detection
Temporal trend detection using LDA

This project is to find topics and temporal trends in a corpus using LDA and Cox-Stuart trend test. It is a scalable and parallel framework and it can be used for large dataset as well. 

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
 
  



Datasets can be found [here](https://drive.google.com/open?id=1q8Dvm-54CgLj-bmVxD6i1hvRT_WhYhpV)
