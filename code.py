import numpy as np
from scipy.misc import logsumexp

def start_counting(file):
    with open(file,'r') as text:
        string = text.read()

    speech_list = string.split('\n')
    speakers = []
    bag_of_words = []



    for speech in speech_list:
        name = speech.split(' ')[0]
        if name not in speakers and name is not '':
            speakers.append(name)


    for speech in speech_list:
        words = speech.split(' ')[1:]
        for word in words:
            if word not in bag_of_words and word is not '':
                bag_of_words.append(word)

    count_of_documents_in_class = dict()
    count_of_words_in_a_class = dict()

    for speaker in speakers:
        count_of_documents_in_class[speaker] = 0
        count_of_words_in_a_class[speaker] = dict()
        for word in bag_of_words:
            count_of_words_in_a_class[speaker][word] = 0


    for speech in speech_list:
        name = speech.split(' ')[0]
        if name is not '':
            count_of_documents_in_class[name] = count_of_documents_in_class[name] + 1




    for speech in speech_list:
        speaker = speech.split(' ')[0]
        words = speech.split(' ')[1:]
        if speaker is not '':
            for word in words:
                if word is not '':
                    count_of_words_in_a_class[speaker][word] = count_of_words_in_a_class[speaker][word] + 1


    # print(speakers)
    # print(count_of_documents_in_class)
    # print(bag_of_words)
    print(str(count_of_documents_in_class['clinton'])+' Clintons instances of speech')
    print(str(count_of_documents_in_class['trump']) + ' Trumps instances of speech')
    print(str(count_of_words_in_a_class['clinton']['country']) + ' Clinton says Country')
    print(str(count_of_words_in_a_class['clinton']['president']) + ' Clinton says President')
    print(str(count_of_words_in_a_class['trump']['country']) + ' Trump says Country')
    print(str(count_of_words_in_a_class['trump']['president']) + ' Trump says President')

    # Code below to compute probabilities

    probability_of_class = dict()
    total_documents = 0
    for speaker in speakers:
        total_documents = total_documents + count_of_documents_in_class[speaker]
    for speaker in speakers:
        probability_of_class[speaker] = count_of_documents_in_class[speaker]/total_documents

    total_words_in_a_class = dict()
    probability_of_word_given_a_class = dict()
    for word in bag_of_words:
        probability_of_word_given_a_class[word] = dict()
        for speaker in speakers:
            probability_of_word_given_a_class[word][speaker] = 0
            total_words_in_a_class[speaker] = 0


    for speech in speech_list:
        speaker = speech.split(' ')[0]
        words = speech.split(' ')[1:]
        for word in words:
            if word is not '':
                probability_of_word_given_a_class[word][speaker] += 1
                total_words_in_a_class[speaker] += 1

    for speaker in speakers:
        for word in bag_of_words:
            probability_of_word_given_a_class[word][speaker] = probability_of_word_given_a_class[word][speaker]/total_words_in_a_class[speaker]

    print(str(probability_of_class['clinton'])+' P(Clinton)')
    print(str(probability_of_class['trump'])+' P(Trump)')
    print(str(probability_of_word_given_a_class['country']['clinton'])+' P(country,clinton)')
    print(str(probability_of_word_given_a_class['president']['clinton'])+' P(president,clinton)')
    print(str(probability_of_word_given_a_class['country']['trump'])+' P(country,trump)')
    print(str(probability_of_word_given_a_class['president']['trump'])+' P(president,trump)')


    list_of_counts = [speakers, count_of_documents_in_class, bag_of_words, probability_of_class, probability_of_word_given_a_class]
    return list_of_counts

def probability_of_a_class_given_a_string(string, c, c_and_p):
    speakers = c_and_p[0]
    # count_of_documents_in_class = c_and_p[1]
    bag_of_words = c_and_p[2]
    probability_of_class = c_and_p[3]
    probability_of_word_given_a_class = c_and_p[4]
    # cf = 10^9
    s = len(bag_of_words)
    probability_of_string_and_class = dict()
    for speaker in speakers:
        probability_of_string_and_class[speaker] = np.log(probability_of_class[speaker])
        for word in string:
            if word in bag_of_words and probability_of_word_given_a_class[word][speaker] != 0:
                # print(str(probability_of_word_given_a_class[word][speaker])+' P('+word+'|'+speaker+')')
                probability_of_string_and_class[speaker] += np.log(probability_of_word_given_a_class[word][speaker])
            else:
                probability_of_string_and_class[speaker] += np.log(1/s)
                s += 1

    denominator = []
    for speaker in speakers:
        # print(str(probability_of_string_and_class[speaker])+' is the probability of string and '+speaker)
        denominator.append(probability_of_string_and_class[speaker])

    # print(str(denominator)+' is the denominator')

    probability_of_a_class_given_a_str = 0

    if denominator != 0:
        probability_of_a_class_given_a_str = np.exp(probability_of_string_and_class[c]-logsumexp(denominator))
    return probability_of_a_class_given_a_str

def tester(sentence, counts_and_probabilities, answer):
    probability_of_class_given_document_max = {'name': 'No-one', 'probability': 0}
    for speaker in counts_and_probabilities[0]:
        probability_of_class_given_a_document = probability_of_a_class_given_a_string(sentence, speaker,
                                                                                      counts_and_probabilities)
        if probability_of_class_given_document_max['probability'] < probability_of_class_given_a_document:
            probability_of_class_given_document_max['probability'] = probability_of_class_given_a_document
            probability_of_class_given_document_max['name'] = speaker
        # print(str(probability_of_class_given_a_document) + ' = P(' + speaker + '|d)')
    if probability_of_class_given_document_max['name'] ==  answer:
        return 1
    else:
        return 0


counts_and_probabilities = start_counting('train')
with open('dev','r') as file:
    sentence = (file.read().split('\n')[0]).split(' ')[1:]

print('\n\n\nThis is the beginning of c')


sum_of_probabilities = 0
probability_of_class_given_document_max = {'name':'No-one', 'probability':0}
for speaker in counts_and_probabilities[0]:
    probability_of_class_given_a_document = probability_of_a_class_given_a_string(sentence,speaker,counts_and_probabilities)
    if probability_of_class_given_document_max['probability'] < probability_of_class_given_a_document:
        probability_of_class_given_document_max['probability'] = probability_of_class_given_a_document
        probability_of_class_given_document_max['name'] = speaker
    print(str(probability_of_class_given_a_document)+' = P('+speaker+'|d)')
    sum_of_probabilities += probability_of_class_given_a_document

print('The first sentence in dev was mostly spoken by '+probability_of_class_given_document_max['name']+' with a  probability of '+str(probability_of_class_given_document_max['probability']))
print(str(sum_of_probabilities)+' is sum of all probabilities')

print('\n\n\n This is the beginning of d')

with open('test','r') as file:
    list_of_test_documents = file.read().split('\n')

correct_classification = 0
for document in list_of_test_documents:
    answer = document.split(' ')[0]
    test_string = document.split(' ')[1:]
    correct_classification += tester(test_string, counts_and_probabilities, answer)

percentage_correct = correct_classification/len(list_of_test_documents)*100
print('The Classifier accuracy is '+str(percentage_correct)+' %')