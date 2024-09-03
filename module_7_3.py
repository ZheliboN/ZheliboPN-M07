class WordsFinder:
    def __init__(self, *filenames):
        self.filenames = []
        if len(filenames) > 0:
            for filename in filenames:
                self.filenames.append(filename)

    def get_all_words(self):
        list_symbol = [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ']
        all_words = {}
        for filename in self.filenames:
            words = []
            with open(filename, encoding='utf-8') as file:
                for line in file:
                    find_symbol = False
                    newline = line.lower()
                    for replace_symbol in list_symbol:
                        if replace_symbol in newline:
                            find_symbol = True
                            newline = newline.replace(replace_symbol, ' ')
                    if not find_symbol:
                        newline = line.lower()
                    words += newline.split()
            all_words[filename] = words
        return all_words

    def find(self, word):
        find1 = False
        find_word = {}
        all_words = self.get_all_words()
        print(all_words)
        for key, value in all_words.items():
            if word.lower() in value:
                find1 = True
                index = value.index(word.lower())
                index += 1
                find_word[key] = index
            else:
                continue
        if not find1:
            find_word = None
        return find_word

    def count(self, word):
        find1 = False
        find_word = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            count_word = 0
            for word_in_list in value:
                if word.lower() == word_in_list:
                    find1 = True
                    count_word += 1
                else:
                    continue
            if find1:
                find_word[key] = count_word
        if not find1:
            return None
        else:
            return find_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder3.get_all_words())
print(finder3.find('child'))
print(finder3.count('child'))

finder4 = WordsFinder('Rudyard Kipling - If.txt')
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
