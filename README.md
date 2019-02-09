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
_If you have any interresting ressources please share it with me !_
### Books:
* __トコトン やさしい__: my personnal favorite to learn! 
Proposing lot of domains, the format of 1 explaination page / 1 illustration page make it easy to understand, and organize your study (like 2 pages a day). The content is maded for Middle/High Schoold Student. [HERE](https://www.amazon.co.jp/s/?ie=UTF8&keywords=%E3%83%88%E3%82%B3%E3%83%88%E3%83%B3%E3%82%84%E3%81%95%E3%81%97%E3%81%84%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA&index=aps&jp-ad-ap=0&tag=googhydr-22&ref=pd_sl_7cl99cz5ww_b&adgrpid=48807802930&hvpone=&hvptwo=&hvadid=259311874221&hvpos=1t1&hvnetw=g&hvrand=4275094671531241966&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009280&hvtargid=kwd-302126771652) is an amazone link but don't forget to check out your school or local library mine have the full collection for free :)

### Website:
* __NHK website__: allows you to search with keywords, and select the size of the articles. [HERE](https://www2.nhk.or.jp/news/nsearch/query.cgi?col=news&charset=utf-8&qi=3&qt=%E4%BA%BA%E5%B7%A5%E7%9F%A5%E8%83%BD) is the result for A.I without size constraint, a lot of article !!
### Others:
* __TeamAI podcast__: are a great to get use to follow AI related topics. The format is around 20min, and kind of business oriented.

