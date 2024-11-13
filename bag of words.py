class MalayalamAutomata:
    def __init__(self):
        self.state = 'initial'
        self.buffer = ''

    def process(self, char, next_char=None):
        result = ''

        if self.state == 'initial':
            if char in ['ം', 'ഃ']:
                self.state = 'special'
            elif char in ['്', 'ാ', 'ി', 'ീ', 'ു', 'ൂ', 'ൃ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ']:
                self.state = 'vowel_sign'
            else:
                self.state = 'consonant'

        if self.state == 'special':
            if char == 'ം':
                result = 'm'
            elif char == 'ഃ':
                result = 'h'
            self.state = 'initial'

        elif self.state == 'vowel_sign':
            if char == '്':
                result = ''
            elif char == 'ാ':
                result = 'a'
            elif char == 'ി':
                result = 'i'
            elif char == 'ീ':
                result = 'ee'
            elif char == 'ു':
                result = 'u'
            elif char == 'ൂ':
                result = 'oo'
            elif char == 'ൃ':
                result = 'ru'
            elif char == 'െ':
                result = 'e'
            elif char == 'േ':
                result = 'e'
            elif char == 'ൈ':
                result = 'ai'
            elif char == 'ൊ':
                result = 'o'
            elif char == 'ോ':
                result = 'o'
            elif char == 'ൌ':
                result = 'au'

            if self.buffer:
                result = self.buffer + result
                self.buffer = ''
            self.state = 'initial'

        elif self.state == 'consonant':
            self.buffer += malayalam_to_manglish.get(char, char)
            if next_char not in ['്', 'ാ', 'ി', 'ീ', 'ു', 'ൂ', 'ൃ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ']:
                result = self.buffer + 'a'
                self.buffer = ''
                self.state = 'initial'
            else:
                self.state = 'vowel_sign'

        return result

    def flush(self):
        result = self.buffer
        self.buffer = ''
        return result


malayalam_to_manglish = {
    'അ': 'a', 'ആ': 'aa', 'ഇ': 'i', 'ഈ': 'ee', 'ഉ': 'u', 'ഊ': 'oo',
    'ഋ': 'ru', 'എ': 'e', 'ഏ': 'e', 'ഐ': 'ai', 'ഒ': 'o', 'ഓ': 'o', 'ഔ': 'au',
    'ക': 'k', 'ഖ': 'kh', 'ഗ': 'g', 'ഘ': 'gh', 'ങ': 'ng',
    'ച': 'ch', 'ഛ': 'chh', 'ജ': 'j', 'ഝ': 'jh', 'ഞ': 'nj',
    'ട': 't', 'ഠ': 'th', 'ഡ': 'd', 'ഢ': 'dh', 'ണ': 'n',
    'ത': 'th', 'ഥ': 'th', 'ദ': 'd', 'ധ': 'dh', 'ന': 'n',
    'പ': 'p', 'ഫ': 'f', 'ബ': 'b', 'ഭ': 'bh', 'മ': 'm',
    'യ': 'y', 'ര': 'r', 'ല': 'l', 'വ': 'v', 'ശ': 'sh',
    'ഷ': 'sh', 'സ': 's', 'ഹ': 'h', 'ള': 'l', 'ഴ': 'zh',
    'റ': 'r', 'ൻ': 'n', 'ർ': 'r', 'ൽ': 'l', 'ൾ': 'l',
}


def handle_exceptions(text):
    exceptions = {
        'ന്റ': 'nt',
        'ങ്ക': 'nk',
        'ഞ്ച': 'nch',
        'ക്ക': 'kk',
        'ത്ത': 'tth',
        'പ്പ': 'pp',
        'ല്ല': 'll',
        'ന്ന': 'nn',
        'മ്മ': 'mm',
        'യ്യ': 'yy',
        'ച്ച': 'chch',
        'ങ്ങ': 'ng',
        'ണ്ണ': 'nn',
        'ര്': 'r',
        'ല്': 'l',
        'ള്': 'l',
        'ന്': 'n',
        'ണ്': 'n',
        'എൻ്റെ': 'ente',
        'പേര്': 'peru',
    }
    for mal, eng in exceptions.items():
        text = text.replace(mal, eng)
    return text


def translate_malayalam_to_manglish(text):
    automata = MalayalamAutomata()
    result = []
    for i, char in enumerate(text):
        next_char = text[i + 1] if i + 1 < len(text) else None
        result.append(automata.process(char, next_char))
    result.append(automata.flush())
    return ''.join(result)


def malayalam_to_manglish_translator(input_text):
    # Preprocess the text to handle exceptions
    preprocessed_text = handle_exceptions(input_text)

    # Translate the preprocessed text
    translated_text = translate_malayalam_to_manglish(preprocessed_text)

    # Post-process the translated text
    post_processed_text = post_process(translated_text)

    return post_processed_text


def post_process(text):
    processed = ''
    for i, char in enumerate(text):
        if i == 0 or char != text[i - 1] or (char in 'aeiou' and text[i - 1] in 'aeiou'):
            processed += char

    processed = processed.replace('au', 'ow')
    processed = processed.replace('ai', 'ay')

    # Handle specific cases
    processed = processed.replace('aa', 'a')
    processed = processed.replace('oo', 'u')
    processed = processed.replace('ee', 'i')

    return processed


def main():
    print("Malayalam to Manglish Translator")
    print("Enter 'q' to quit")

    while True:
        malayalam_text = input("\nEnter Malayalam text: ")

        if malayalam_text.lower() == 'q':
            print("Thank you for using the translator. Goodbye!")
            
            break

        manglish_text = malayalam_to_manglish_translator(malayalam_text)
        print(f"Manglish translation: {manglish_text}")


if __name__ == "__main__":
    main()