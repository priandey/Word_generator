# Word Generator
This project is a program that analyze a word corpus using a Markov Chain (https://en.wikipedia.org/wiki/Markov_chain) and render a list of "real" looking words.

The original program has been made by a french Youtuber, ScienceEtonnante, you can find his video (in french) here : https://www.youtube.com/watch?v=YsR7r2378j0&t=1s.

# How it works
Today, the program is not very stable, but it works like this :

First step, you need a corpus of words from the language you wish to "copy". The file should be raw text, a single word by line. Put it in "source_file", then launch the program (word_generator.py).

Choose your source corpus by entering corresponding number.

Choose a range min and max for words length.

You now have a new corpus of words, procedurally generated and good looking relatively to the corpus you inputed.

# Corpus
The corpus of words in source_file should be as wide as possible, ideally 1k words minimum, but the program will run with 2 words if given so.
