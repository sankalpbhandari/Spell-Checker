import readWords
import editDistance
import multiprocessing

path = "english_words.txt"


def chunk_list(my_word, chunk_size):
    chunk_size = len(my_word) // chunk_size
    return [my_word[i:i + chunk_size] for i in range(0, len(my_word), chunk_size)]


def spell_checker(list_words):
    min_distance = 999999
    suggestion = None
    for word in list_words:
        distance = editDistance.dynamic_soln(word, myword)
        if distance < min_distance:
            suggestion = word
            min_distance = distance
    return suggestion


listOfWords = readWords.read_files(path)
myword = input("Please input the word ")
if __name__ == '__main__':

    pool = multiprocessing.Pool()

    resultList = pool.map(spell_checker, chunk_list(listOfWords, 500))

    print("Correct spell is", spell_checker(resultList))

# print "Suggestion is",suggestion
