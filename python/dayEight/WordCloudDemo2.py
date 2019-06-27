'''
    using wordcloud
'''

import wordcloud as wc

w = wc.WordCloud(background_color="White")
w.generate("Life is short, I code with python!")
w.to_file("pylife.png")
