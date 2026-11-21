# https://www.codewars.com/kata/52449b062fb80683ec000024/solutions/python

def generate_hashtag(s):
    words = parse_words(s)
    return hashtagify(words)

def parse_words(s):
    words = s.split()
    return [word for word in words if word]

def hashtagify(words):
    if not words:
        return False
    out = "#" + "".join(word.capitalize() for word in words)
    if len(out) > 140:
        return False
    return out

# def capitalize(word):
#     return word[0].capitalize() + word[1:].lowercase()
