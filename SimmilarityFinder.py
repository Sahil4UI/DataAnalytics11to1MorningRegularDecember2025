#Simmilarity Finder


komal = '''Python is a popular general-purpose programming language that can be used for a wide variety of applications. It includes high-level data structures, dynamic typing, dynamic binding, and many more features that make it as useful for complex application development as it is for scripting or "glue code" that connects components together. It can also be extended to make system calls to almost all operating systems and to run code written in C or C++. Due to its ubiquity and ability to run on nearly every system architecture, Python is a universal language found in a variety of different applications.

'''

ragu = komal
#tokenization-extracting words from sentences
token1 = set(ragu.split())
token2 = set(komal.split())

#remove stopwords -
import nltk
#Natural Language Processing ToolKit
nltk.download("stopwords")

from nltk.corpus import stopwords

st = set(stopwords.words("english"))

token1 = token1.difference(st)
token2 = token2.difference(st)

#simmilary
common = len(token1.intersection(token2))
all = len(token1.union(token2))

print(common/all*100)
