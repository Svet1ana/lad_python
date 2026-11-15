dirty_title = " dfasdf ' 'a  :: :  asdfasdf "

clean_title = dirty_title.strip()
print(clean_title)

for symbol in ['{', '}', '«', '»', '"', "'"]:
    clean_title = clean_title.replace(symbol, "")

words = clean_title.split()

capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())

result = " ".join(capitalized_words)
print(result)