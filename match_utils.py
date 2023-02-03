from fuzzysearch import find_near_matches
from fuzzywuzzy import process

def fuzzy_extract(qs, ls, threshold):
    for word, _ in process.extractBests(qs, (ls,), score_cutoff=threshold):
        for match in find_near_matches(qs, word, max_l_dist=1):
            match = word[match.start:match.end]
            index = ls.find(match)
            yield (match, index)

def check_comment(comment, comment_cache):
    for comment_id in comment_cache:
        original = comment_cache[comment_id]
        for match, index in fuzzy_extract(comment, original, 90):
            print(f"Match!\nOriginal: {original}\nPotential Bot: {comment}\n\n")
            return True