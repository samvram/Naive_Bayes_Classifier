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

    list_of_counts = [speakers, count_of_documents_in_class, bag_of_words]
    # print(speakers)
    # print(count_of_documents_in_class)
    # print(bag_of_words)
    print(str(count_of_documents_in_class['clinton'])+' Clinton')
    print(str(count_of_documents_in_class['trump']) + ' Trump')
    print(str(count_of_words_in_a_class['clinton']['country']) + ' Clinton-Country')
    print(str(count_of_words_in_a_class['clinton']['president']) + ' Clinton-President')
    print(str(count_of_words_in_a_class['trump']['country']) + ' Trump-Country')
    print(str(count_of_words_in_a_class['trump']['president']) + ' Trump-President')

    return list_of_counts

count = start_counting('train')