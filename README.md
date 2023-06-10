# TF-IDF Text Summarization
This repository contains Python scripts for performing TF-IDF (Term Frequency-Inverse Document Frequency) based text summarization. TF-IDF is a widely used technique in natural language processing and information retrieval to identify the most important words or phrases in a document collection.

## Scripts
The repository consists of three Python files:

1. **tfidf.py**: This file contains functions and classes for text processing, including tokenization, stemming, and TF-IDF computation. It defines the following functions: 
- `gettext(xmltext)`: Parses an XML document and returns the combined text from `<title>` and `<text>` tags. 
- `tokenize(text)`: Tokenizes the input text, converts it to lowercase, removes punctuation and digits, removes stop words, and filters out words with a length less than 3. 
- `stemwords(words)`: Stems each word in the input list using the Porter stemming algorithm. 
- `tokenizer(text)`: Combines the tokenization and stemming steps into a single function. 
- `compute_tfidf(corpus)`: Trains a TF-IDF vectorizer on a corpus of documents and returns the trained vectorizer. The corpus is provided as a dictionary mapping file names to XML text. 
- `summarize(tfidf, text, n)`: Given a trained TF-IDF vectorizer and an XML text, returns up to `n` word-score pairs sorted by TF-IDF score in reverse order. 
- `load_corpus(zipfilename)`: Reads XML files from a zip archive and returns a dictionary mapping file names to XML text. 

2. **common.py**: This file imports the necessary functions from `tfidf.py` and defines a `main()` function to extract and print the top 10 most frequent stemmed words from a given XML text file. It utilizes the `load_corpus()` and other functions from `tfidf.py` to process the text.

3. **summarize.py**: This script also imports the required functions from `tfidf.py` and defines a `main()` function to compute the TF-IDF scores for a specific file within a given corpus. It utilizes the `load_corpus()`, `compute_tfidf()`, and `summarize()` functions from `tfidf.py` to generate and print the top 20 important words or phrases based on their TF-IDF scores.

## Getting Started
To use the scripts in this repository, follow the steps below:

1. Make sure you have Python installed on your system (version 3 or above).

2. Clone the repository to your local machine using the following command:
   ```bash
   $ git clone https://github.com/wangyuhsin/tfidf-text-summarization.git
   ```
   
3. Navigate to the cloned repository's directory:
   ```bash
   $ cd tfidf-text-summarization
   ```

4. Install the required dependencies by running the following command:
   ```bash
   $ pip install -r requirements.txt
   ```

5. Ensure that you have the necessary XML files or corpus available to be processed by the scripts.

## Usage

### common.py
This script demonstrates an example usage of the `tfidf.py` module. It imports the required functions and defines a `main()` function that takes an XML text file as input. It extracts the text from the file and computes the top 10 most frequent stemmed words using TF-IDF. The results are then printed to the console.

To run the script, use the following command:
```bash
$ python common.py [path/to/xmlfile.xml]
```

### summarize.py
This script also showcases the usage of the `tfidf.py` module. It imports the necessary functions and defines a `main()` function that takes two arguments: the path to a corpus (a zip file containing XML files) and the name of a specific file within the corpus. It loads the corpus, computes the TF-IDF scores for the specified file, and prints the top 20 important words or phrases based on their TF-IDF scores.

To execute the script, use the following command:
```bash
$ python summarize.py [path/to/corpus.zip] [filename.xml]
```

## Example
Here's an example to demonstrate how to use the scripts in this repository:

Suppose we have a corpus named `reuters-vol1-disk1-subset.zip` containing multiple XML files, and we want to summarize the contents of a specific file named `33313newsML.xml`. We can perform the following steps:

1. Place the corpus file (`reuters-vol1-disk1-subset.zip`) in a directory accessible to the script.

2. Run the `summarize.py` script with the following command:
   ```bash
   $ python summarize.py data/reuters-vol1-disk1-subset.zip 33313newsML.xml
   transmiss 0.428
   gener 0.274
   power 0.254
   electr 0.253
   zealand 0.235
   tran 0.215
   signal 0.214
   esanz 0.191
   cost 0.162
   leay 0.143
   gisborn 0.143
   charg 0.131
   new 0.130
   island 0.128
   auckland 0.113
   effici 0.110
   pricipl 0.096
   eastland 0.096
   ```

   The script will compute the TF-IDF scores for the specified file within the

 corpus and print the top 20 important words or phrases based on their scores.

## Notes
- The scripts assume that the XML files are formatted according to a specific structure, as described in the `tfidf.py` file's comments. Please ensure that your XML files follow a similar structure for the scripts to work correctly.

- You can modify the scripts according to your specific requirements, such as changing the number of top words or phrases to be summarized or customizing the text preprocessing steps.

- Make sure to check the Python version and install any missing dependencies before running the scripts.

## References
- The TF-IDF algorithm and its implementation in this repository are based on the concepts covered in the [MSDS692 TF-IDF lecture](https://github.com/USFCA-MSDS/msds692/blob/master/hw/tfidf.md).

- The scripts utilize the following libraries:
  - NLTK (Natural Language Toolkit): https://www.nltk.org/
  - scikit-learn: https://scikit-learn.org/

## License
This repository is licensed under the MIT License. See the [LICENSE](https://github.com/your-username/your-repo/blob/main/LICENSE) file for more details.
