import matplotlib.pyplot as plt
from wordcloud import WordCloud 

text_data = open("fb_hacked_again.txt", "r").read()

def generate_wordcloud(text_data):
    wordcloud = WordCloud(relative_scaling = 0.7).generate(text_data)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

generate_wordcloud(text_data)