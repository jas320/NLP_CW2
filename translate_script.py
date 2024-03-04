from deep_translator import GoogleTranslator
import random
import pickle


def write_list_to_file(list1, filename1):
    with open(filename1, 'wb') as file:
        pickle.dump(list1, file)
def read_list_from_file(filename1):
    with open(filename1, 'rb') as file:
        return pickle.load(file)
def translate_group(text_list, label_list):
    aug_text_list = []
    aug_label_list = []
    choices = ['fr', 'de', 'ar']
    translators_to = [GoogleTranslator(source='en', target=x) for x in choices]
    translators_from = [GoogleTranslator(source=x, target='en') for x in choices]
    for text, label in zip(text_list, label_list):
        aug_text_list.append(text)
        for i in range(3):
            new_text = [translators_from[i].translate(translators_to[i].translate(text))]
            aug_text_list.extend(new_text)
        aug_label_list.append(label)
        aug_label_list.extend([label] * len(new_text))
    return aug_text_list, aug_label_list


text, labels = read_list_from_file("full_data_text_list.pkl"), read_list_from_file("full_data_label_list.pkl")
res1, res2 = translate_group(text, labels)
# [print(x) for x in res1]
write_list_to_file(res1, "3_lang_translate_text.txt")
write_list_to_file(res2, "3_lang_labels.txt")

