# Multimodal-Activity-Classification
6.S191 Deep Learning Project: Classifying Activities from information of various source types. 


### 1. Initial Data is Collected or Scrapped From Yelp, BBC, or Google Search </br>
Snapshot of Reviews Collected From Yelp </br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/85134229/151624020-8271d0a2-207d-43c2-a3f3-c3ee161646cc.png" | width=500/> </br>
</p>
</br>
</br>
Snapshot of Website Information Collected from Google </br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/85134229/152094927-c22f7ffe-5143-4b88-a00c-231bccbb2a7e.png" | width=500/> </br>
</p>
</br>
</br>
</br>

### 2. Text Processing Tokenized Text </br>
Specifically, I removed all stop words, numbers, punctuation, and non-english words (not taking into account mis-spelling). I then tokenized by words and stored them in an array. </br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/85134229/152095648-7fff8260-a334-45e9-a216-df888a4443c9.png" | width=700/> </br>
</p>

### 2. Trained a Gensim Word2Vec Model and Compared Outputs for Associated and Disassociated Content </br>
The model predicted 51% of the google website correctly to the yelp reviews associated with the activity. Given the limited data set we have, I was happy with the results (the model only took 10 sec to train). Obviously, the biggest limitation in this model is the vocabulary. Many of the words in non-training samples are not found in the vocabulary. Additionally, with limited data, it is especially hard to make predictions on data formated differently than the training data. In this case, I simply concatenated all the information provided by Google for each website. Ideally, I would attempt this again by training on a variety of information and preclassify like activities. In the training set, there were 3 escape room activities. It's no wonder that the model preformed poorly on most of those activities. Also, the descriptions of the lawn on boston and cambridge center roof garden are difficult to distinguish (even by hand once names were taken out).</br>

In a model attempting to classify activities from people's lives, it will be important to get a time and location stamp to help strengthen activities that should be grouped together. I propose first collecting a substantial database of journals and information relating to activites of those people who journaled. Then I would first group information by location and time. I would further train a model simply for weeding out non-similar data. Then I would train a seperate model for recognizing similar type data. Importantly, the two approaches for cleaning the data and then training on the final model will need to be different and require more thought.
