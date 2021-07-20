# DSF
Document Similarity framework
A framework to compare the documents by extracting and comparing triplets of the sentences in documents.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:
Required Python modules in addition to basic libraries:
1. sys
2. os
3. nltk (StanfordDependencyParser)
4. subprocess 
5. parse
6. pycorenlp

```
pip install spacy (>=3.0.6)
pip install networkx (>=2.5.1)
pip install flask (>=2.0.1)
pip isntall pycorenlp (>=0.3.0)
```
Install en_core_web_sm for nlp model:
```
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
```

### Installing external requirements  

We will use two Stanford packages. Download the packages using the link below:
* StanfordCoreNLP : https://stanfordnlp.github.io/CoreNLP/download.html 
* Stanford parsor using https://nlp.stanford.edu/software/stanford-parser-4.2.0.zip

Note : Make sure you have java 8 and jdk 8 installed in your system. Then give the respective path name for CLASS_NAME and JAVAHOME environment variables (in simplification.py)


### Running stanfordcoreNLP server 
Open the command propmpt and run the following command( path_name : path where coreNLP file is downloaded)
```
java -mx4g -cp "{path_name}\stanford-corenlp-4.2.2\stanford-corenlp-4.2.2\*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,depparse,natlog,openie" -outputFormat "json" -openie.triple.strict "true" -openie.max_entailments_per_clause 3
```


## Running the program
Open the terminal or new command prompt and go to 'dsf' folder: 

```
flask run
```
* Open the browser and open http://localhost:5000/
* You can see the dsf framework running (It may take a little time initially to import all modules at first)
* Select the text files and upload it(The processing time depends on the processor speed and complexity of documents uploaded)
* Click on the buttons to get the reuired result(i.e, similarity score, keyword search or knowledge graph)

## Team

* **4SF17IS017** - [Deeksha](https://github.com/deekshakulal)
* **4SF17IS029** - [Glenisha](https://github.com/Glenisha16)
* **4SF17IS031** - [Jasirah](https://github.com/JASIRAHS)
* **4SF17IS015** - [Crisel](https://github.com/crisellm)

