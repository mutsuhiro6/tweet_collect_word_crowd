from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from count_words import count_words
from get_tweets import get_tweets


fp = FontProperties(fname=r'/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc', size=50)


def draw_word_cloud(word_freq_dict, fig_title):
    word_cloud = WordCloud(background_color='white', min_font_size=15, font_path='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc',
                          max_font_size=200, width=1000, height=500)
    word_cloud.generate_from_frequencies(word_freq_dict)
    plt.figure(figsize=[20, 20])
    plt.title(fig_title, fontproperties=fp)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    draw_word_cloud(
        count_words(get_tweets('桜木町', '201308010800', '201308011000', loop=10)),
        '2013-08-01 17:00-19:00 query:桜木町'
    )
