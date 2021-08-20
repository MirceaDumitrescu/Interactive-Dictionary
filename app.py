import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Please type your word here: ")

def get_word(w):
    w = w.lower()
    if w in data:
        return '\n'.join(data[w])
    elif w.title() in data:
        return '\n'.join(data[w.title()])
    elif w.upper() in data:
        return '\n'.join(data[w.upper()])
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        response = input("Did you mean %s instead? (Y) or (N): " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        response = response.lower()
        if response == "y":
            return '\n'.join(data[get_close_matches(w, data.keys(), cutoff=0.8)[0]])
        elif response == "n":
            return "Please try again"
        else:
            return "Please reply with Y or N only."
    else:
        return ("Word does not exist in data.json, please try again")

print(get_word(word))