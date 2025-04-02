# Returns number of words in string
def get_num_words(string):
    count = 0
    string_list = string.split()
    for word in string_list:
        count += 1
    return count

# Returns characters + occurrence in dictionary format
def count_characters(text):
    characters_dict = {}
    for char in text:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict

# A helper function that takes a dictionary and returns the value of the "count" key
def sort_on(dict):
    return dict["count"]

# Returns a sorted dictionary from greatest to least by count
def sorted_characters(characters_dict):
    characters_list = []
    for item in characters_dict:
        entry = {"character": item, "count": characters_dict[item]}
        characters_list.append(entry)
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list