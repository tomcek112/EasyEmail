# These code snippets use an open-source library.
response = unirest.post("https://textanalysis.p.mashape.com/textblob-noun-phrase-extraction",
  headers={
    "X-Mashape-Key": "tb0NKUuhy7mshsTSq5TsvEq9Tf6gp1m4NAKjsnWO4ewgznNE9j",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "text": "Natural language processing (NLP) deals with the application of computational models to text or speech data. Application areas within NLP include automatic (machine) translation between languages; dialogue systems, which allow a human to interact with a machine using natural language; and information extraction, where the goal is to transform unstructured text into structured (database) representations that can be searched and browsed in flexible ways. NLP technologies are having a dramatic impact on the way people interact with computers, on the way people interact with each other through the use of language, and on the way people access the vast amount of linguistic data now in electronic form. From a scientific viewpoint, NLP involves fundamental questions of how to structure formal models (for example statistical models) of natural language phenomena, and of how to design algorithms that implement these models"
  }
)