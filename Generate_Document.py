# O(n + m) time | O(n+m) space - where n is the length of the characters and m is the length of the document
def generate_document(characters, document):
    characters_hash_map = {}
    for character in characters:
        if characters_hash_map.get(character) is None:
            characters_hash_map[character] = 1
        characters_hash_map[character] += 1
    document_hash_map = {}
    for character in document:
        if document_hash_map.get(character) is None:
            document_hash_map[character] = 1
        document_hash_map[character] += 1
    for key, value in document_hash_map.items():
        if characters_hash_map.get(key) is None:
            return False
        if characters_hash_map[key] < value:
            return False
    return True


# print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
print(generate_document(" ", "hello"))



