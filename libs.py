import string
import re
import nltk
from pycorenlp import *
import collections
import json
nlp=StanfordCoreNLP("http://localhost:9000/")
import sys
import spacy
from spacy.lang.en import English
nlp_model = spacy.load('en_core_web_sm')
import os

from nltk.tree import ParentedTree
from nltk.parse import stanford
os.environ['CLASSPATH']=r'C:\Users\dell\isimp\Sentence-Simplification\stanford-parser-full-2020-11-17'
os.environ['JAVA_HOME']=r"C:\Program Files\Java\jdk1.8.0_291\bin"

#import SBAR#from nltk.parse.stanford import StanfordDependencyParser as sdp
from nltk.parse.stanford import StanfordParser as sp

from anytree import NodeMixin, Node,AnyNode,RenderTree

import json

print("Imported")