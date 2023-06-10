from tfidf import *
import sys


def main():
    xmltext = load_corpus(sys.argv[1].split("/")[-2] + ".zip")[
        sys.argv[1].split("/")[-1]
    ]
    text = gettext(xmltext)
    count = sorted(
        Counter(stemwords(tokenize(text))).items(), key=lambda x: x[1], reverse=True
    )[:10]
    for element in count:
        print(element[0] + " " + str(element[1]))


if __name__ == "__main__":
    main()
