import os
import re
import string
import random

from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, "r") as f:
        text = f.read()

        text = re.sub(r"\[(.+)\]", " ", text)

        text = " ".join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    return words


def make_graph(words):
    g = Graph()

    prev_word = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if prev_word:
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []

    word = g.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    # Takes text from Harry Potter sorcerer stone
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # Takes text from all files in given folder
    words = []

    for song_file in os.listdir(f"songs/{artist}"):
        song_words = get_words_from_text(f"songs/{artist}/{song_file}")
        words.extend(song_words)

    g = make_graph(words)
    composition = compose(g, words, 100)

    return " ".join(composition)


if __name__ == "__main__":
    text = main("green_day")
    print(text)
