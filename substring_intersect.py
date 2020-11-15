import ahocorasick

'''
function substring_intersect (substrings text[], search_strings text[)**
A fast, multi-string to joining 2 datasets using a 'like %pattern%' 

- returns substrings and what they matched
  - substring text, matched_search_strings text[]
'''

def substring_intersect(substrings, search_strings):
  if not substrings or len(substrings) == 0 or not isinstance(substrings, list):
    return {}

  if not search_strings or len(search_strings) == 0 or not isinstance(search_strings, list):
    return {}

  # build trie from substrings to search for
  A = ahocorasick.Automaton()

  for index, str in enumerate(substrings, start=0):
    A.add_word(str, index)

  A.make_automaton()

  # prep search
  SEPARATOR = chr(31) # unit seperator code
  corpus = SEPARATOR.join(search_strings)
  corpus_length = len(corpus)

  # results keyed on substring, value is a dict of search_strings
  results = {}

  # search
  for corpus_index, substring_index in A.iter(corpus):
    # extract the item around the corpus_index
    left_index = corpus.rfind(SEPARATOR, 0, corpus_index)
    left_index = left_index + 1 if left_index > -1 else 0
    right_index = corpus.find(SEPARATOR, corpus_index) or corpus_length
    right_index = right_index if right_index > -1 else corpus_length

    substring = substrings[substring_index]
    search_string = corpus[left_index:right_index]

    # add the found substring and its search_string to results
    if not substring in results:
      results[substring] = {search_string}
    elif search_string not in results[substring]:
      results[substring].add(search_string)

  # complete
  return results

