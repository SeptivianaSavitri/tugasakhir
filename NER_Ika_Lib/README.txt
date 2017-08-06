Further Studies of DBpedia Entities Expansion in building automatically dataset for Indonesian NER

by Ika Alfina (ika.alfina@gmail.com) & Septiviana Savitri (septivianasavitri37@gmail.com)

last update: July 25 2017

----------------

README

To create unlabeled dataset, follow this steps:

1. Get the wikipedia dump
Source : https://dumps.wikimedia.org/idwiki/latest/
Data yang dipilih : idwiki-20170120-pages-articles-multistream.xml

2. Use WikiExtractor.py to get content of Wikipedia dump
Source code : https://github.com/attardi/wikiextractor
Syntax : python WikiExtractor.py idwiki-20170120-pages-articles-multistream.xml -b 500K -o extracted
Input : idwiki-20170120-pages-articles-multistream.xml
Output : Folder extracted yang berisi folder AA....ZZ dengan setiap folder berisi maksimal 100 data.

3. Use Data1_ArticleAndParagraphSelector.py to get list of paragraphs that certain criterias for each folder from step 2
Fungsi : menghitung paragraf yang bakal diambil dan juga ngebersihin tag dari wiki. 
input : wikitext/AA/ ->isi nya ada wiki_00 sampai wiki_99 () data yang jumlahnya 100 (or less) yang uda diproses WikiExtractor). 
output: data/training/prep/paragraphs_test.txt  ->  list of paragraf yang sudah bersih dari tag html

4. Use Data2_FileCombiner.py to combine all files resulted from step 3
Fungsi : menggabungkan file file output langkah 3 (kan bisa AA ... ZZ) untuk dijadikan satu file
Input  : output langkah 3 untuk file-file berbeda (jumlah file bebas).
output : data/training/prep/allParagraphs.txt  ->  satu file hasil penggabungan biar lebih ringkas.


5. Use Data3_SentencerNltk/py to extract sentences from step 4
Requirement : Python 3.5, NLTK , NLTK Data
Fungsi		: Dari list of paragraph diubah menjadi list of sentences (memotong paragraf menjadi kalimat dengan bantuan NLTK).
input       : data/training/prep/allParagraphs.txt -? list of paragraphs
output      : data/training/prep/allSentences.txt -> list of sentences hasil pecahan paragraf file input.


6. Use Data4_SentencesFilter.py to filter sentences that meet certain criterias
Fungsi 	 : Memilih kalimat yang sesuai dengan kriteria.
Kriteria : Suatu kalimat dipilih jika memenuhi -> Terdiri dari minimal 15 kata, Mengandung minimal 5 huruf kapital, Diakhiri oleh titik (akhir kalimat).
Input    : data/training/prep/allSentences.txt
Output   : data/training/prep/all_good_sentences1.txt -> list of sentences yang sesuai kriteria.

7. Use Data5_IndoDetector.java to filter non Indonesian language
Requirement : https://github.com/shuyo/language-detection (Language Detection Tool), https://osdn.net/projects/jsonic/devel/ (bundle jsonic)
Fungsi : Memilih kalimat yang menggunakan Bahasa Indonesia saja.
input  : data/training/prep/all_good_sentences1.txt 
output : data/training/prep/all_ID_sentences.txt -> list of sentences yang berisi kalimat berbahasa Indonesia.

8. Use Data6_FileSplitter.py to split file from step 7, so that each file contains certain number of sentences
Fungsi : Membagi keseluruhan list of sentences kedalam file berbeda dengan -n jumlah kalimat per file.
Input  : data/training/prep/all_ID_sentences.txt
Output : data/training/prep/ID_sentences1_xx , dimana xx mulai dari 00 - n, sesuai jumlah kalimat.

9. Use Stanford NER library to format each file in step 8
Source : http://nlp.stanford.edu/software/CRF-NER.shtml#Download
code   : java -cp stanford-ner.jar edu.stanford.nlp.process.PTBTokenizer [file_input] > [file_output]
Fungsi : Membuat setiap baris hanya terdapat 1 kata (token)
Input  : data/training/prep/ID_sentences1_xx
Output : data/training/prep/ID_formatted1_xx, dimana xx mulai dari 00 - n, menyesuaikan ID_sentences1_xx.

Tagging process:
1. Use test_NER_Tagger to automatically tag the data set
	-choose different kind of DBpedia entites in function.py (original/cleansing/normalization/expanded/validate)
	-fill in the input and output file
	-run the program

2. (optional) Place the tagged data set from tagging process (1) into Stanford NER as data training
	source : https://nlp.stanford.edu/software/CRF-NER.shtml
	- buat file properties seperti contoh : http://nlp.stanford.edu/software/crf-faq.html
	- compile file properti (input : ID_tagged1_xx | output : outputmodelxx-xx.gz)
	  java -mx4g -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop [nama_file_prop]
	- test dengan data goldstandard
      java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier outputmodelxx-xx.gz -testFile goldstandard-0811.txt