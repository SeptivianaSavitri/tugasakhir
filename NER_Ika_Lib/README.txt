DBpedia Entities Expansion in building automatically dataset for Indonesian NER

by Ika Alfina (ika.alfina@gmail.com)

last update: August 15 2016

----------------

README

To create dataset, follow this steps:

1. Get the wikipedia dump
2. Use WikiExtractor.py to get content of Wikipedia dump
3. Use Data1_ArticleAndParagraphSelector.py to get list of paragraphs that certain criterias for each folder from step 2
4. Use Data2_FileCombiner.py to combine all files resulted from step 3
5. Use Data3_SentencerNltk/py to extract sentences from step 4
6. Use Data4_SentencesFilter.py to filter sentences that meet certain criterias
7. Use Data5_IndoDetector.java to filter non Indonesian language
8. Use Data6_FileSplitter.py to split file from step 7, so that each file contains certain number of sentences
9. Use Stanford NER library to format each file in step 8
10. Use NERIka_Tagger to automatically tag the data set