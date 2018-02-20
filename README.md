# Naive Bayes Classifier

In this assignment, we will build various text classification models and use them to classify sentences from 2016 presidential debates(United States of America) according to speakers.

## Classifier Characteristics
Implementing a Naïve Bayes classifier:-

We need **P(class|sentence)** = **P(class|w1)** **P(class|w2)** **P(class|w3)**... 

* Wrote code to read in the training documents and collect counts,  for all speakers, and all words.
* Wrote code to compute the probabilities, **P(word|class)** which will act as a prior probability for finding **P(class|word)**.
* Trained the data on the training set present in the file `train`.
* Wrote code to compute the probabilities **P(class|sentence)** for each sentence, tested on `dev`
* Ran the code for all sentences in `test` and reported the output, accuracy. 

## Formulae and Assumptions

* **P(word)** = count(word)/Sum(count(All words in BagOfWords))
* **P(class)** = count(class)/Sum(count(All classes present))
* **P(word|class)** = count(word in class)/sum(count(all words in class))
* **P(class|word)** = **P(word|class)** x **P(class)** / **P(word)**
* **Sentence** = **w1** **w2** **w3** ....
* **P(class|sentence)** = **P(class|w1)** **P(class|w2)** **P(class|w3)**... 
* **Prediction** is done by selecting the class which has **M**aximum **A**posteriori **P**robability(**MAP**)
## Evaluation

There are 2 codes present
* `code.py` - This is the inital code with no extra implementation and it 
gives the results as follows:-

```
455 Clintons instances of speech
637 Trumps instances of speech
84 Clinton says Country
182 Clinton says President
161 Trump says Country
39 Trump says President
0.14416983523447402 P(Clinton)
0.20183776932826364 P(Trump)
0.0016090104585679806 P(country,clinton)
0.0034861893268972916 P(president,clinton)
0.004245668626882203 P(country,trump)
0.0010284538909838875 P(president,trump)



This is the beginning of c
1.34876566554e-11 = P(sanders|d)
8.63668832496e-05 = P(clinton|d)
2.5214234427e-15 = P(chafee|d)
2.21736286658e-13 = P(o'malley|d)
3.42010063663e-05 = P(webb|d)
0.00493783502371 = P(bush|d)
9.18071216872e-11 = P(cruz|d)
8.57514306273e-09 = P(trump|d)
0.00288056513665 = P(christie|d)
2.81212628456e-06 = P(rubio|d)
0.000223718240588 = P(kasich|d)
1.98518349875e-08 = P(fiorina|d)
0.986688830667 = P(paul|d)
7.55985573038e-05 = P(carson|d)
1.81859031664e-06 = P(huckabee|d)
0.00506822523563 = P(walker|d)
1.57653107963e-45 = P(perry|d)
The first sentence in dev was mostly spoken by paul with a  probability of 0.986688830667
1.0 is sum of all probabilities



This is the beginning of d
The Classifier accuracy is 51.12219451371571 %
```

* `improve_code.py` - This is a slightly modified code whose bag of word has been
reduced to essential words only. This gives results as follows:-
```
455 Clintons instances of speech
637 Trumps instances of speech
84 Clinton says Country
182 Clinton says President
161 Trump says Country
39 Trump says President
0.14416983523447402 P(Clinton)
0.20183776932826364 P(Trump)
0.0021680776378277928 P(country,clinton)
0.004697501548626884 P(president,clinton)
0.005814373420007223 P(country,trump)
0.0014084507042253522 P(president,trump)



This is the beginning of c
2.08872325105e-09 = P(sanders|d)
0.0467792734344 = P(clinton|d)
1.04489927538e-16 = P(chafee|d)
1.43010153696e-12 = P(o'malley|d)
4.30577115347e-05 = P(webb|d)
0.0331835271518 = P(bush|d)
2.02922660015e-08 = P(cruz|d)
2.27158985852e-06 = P(trump|d)
0.014068911545 = P(christie|d)
4.01253502532e-05 = P(rubio|d)
0.00206513955972 = P(kasich|d)
1.2293413779e-09 = P(fiorina|d)
0.903277059839 = P(paul|d)
2.83339736986e-05 = P(carson|d)
4.4002453648e-07 = P(huckabee|d)
0.000511836208921 = P(walker|d)
4.95468785128e-44 = P(perry|d)
The first sentence in dev was mostly spoken by paul with a  probability of 0.903277059839
1.0 is sum of all probabilities



This is the beginning of d
The Classifier accuracy is 54.3640897755611 %
```

## Conclusion
The results clearly show that the accuracy of both the classifiers are well above
the required thresold of **50%**, which is the probability of random guess.