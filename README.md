# Japanese for Engineering
In this repository you can find:
* Technical vocabulary
* Python script to generate vocabulary test
* Ressources to learn engineering Japanese

## Project route map 
- [x] Vocabulary lists
- [x] Python script to generate
- [ ] Flask application

All the materials are based on my experience and readings, and so are incomplete and probably comport errors. Feel free to add your own ressources and correction :) 

# Current vocaulary list
* [General](https://github.com/BenbenIO/Japanese_for_Engineering/blob/master/vocabularyMD/General.md)
* [Embendded systems - Electronics](https://github.com/BenbenIO/Japanese_for_Engineering/blob/master/vocabularyMD/Embedded_Systems.md)
* [Science - Physics](https://github.com/BenbenIO/Japanese_for_Engineering/blob/master/vocabularyMD/Science.md)
* [AI - Machine Learning](https://github.com/BenbenIO/Japanese_for_Engineering/blob/master/vocabularyMD/MachineLearning.md)

# Test generation
Python script that generate vocabulary test based on the vocaulary list. Usage: 
``` python generatePDF --topic --mode ```

The following example was obtained with : 
``` python generatePDF MachineLearning 4 ``` 

<p align="center">
  <img src="/images/example_test.PNG" width="800">
</p>

Available mode are 0: noblank | 1: Kanji test | 2: reading test | 3: translation test | 4: random test

### Dependencies: 
* pandas / numpy / pdf_repport
Special note for pdf_repport, it needs cairolib, which is not so easy to install on Windows. [Here](https://www.cairographics.org/download/) is the tutorial I used.

### Your own vocabulary:
You can generate vocabulary test with your own files. Be sure to populate the _xls_files_ with xls file with compatible kanji format and  heard as kanji | hiragana | english.

### Printing consideration:
Please print the tests the more efficiently way as possible. I recommend: Mutliple page: 2 by 1 / Landscape / both sides of paper.

# Ressources
* Books:
* Website:
* Others:
