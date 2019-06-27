'''
    wordcloud 词云☁️
    How to do that?
    step 1:     create a wordcloud object
    step 2:     load the wordcloud text
    step 3:     output to the file
'''

import wordcloud
import matplotlib

'''
    what did wordcloud do for us?
    1.separate words
    2.do statistic analysis
    3.text style configuration

'''
c = wordcloud.WordCloud(min_font_size=10, max_font_size=20)
c.generate("python by wordcloud")
c.to_file("pywordcloud.png")
