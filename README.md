# Word Generator
This project is a program that analyze a word corpus using a Markov Chain (https://en.wikipedia.org/wiki/Markov_chain) and render good looking words.

The original program has been made by a french Youtuber, ScienceEtonnante, you can find his video (in french) here : https://www.youtube.com/watch?v=YsR7r2378j0&t=1s.

# How it works
Today, the program is not very stable, but it works like this :

First step, you need a corpus of words from the language you wish to "copy". The file should be raw text, a single word by line. Put it in "source_file", then launch the program.

Enter your text file name (with extension if needed).
Enter the name your proba file should have.
Enter the name of the render file.
Determine a max and min lenght of words generated.

You know have a new corpus of words, procedurally generated and good looking relatively to the corpus you inputed.

# Corpus
The corpus of words in source_file should be as wide as possible, ideally 1k words minimum, but the program will run with 2 words if given so.
