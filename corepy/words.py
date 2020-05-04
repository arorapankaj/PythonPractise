from urllib.request import urlopen

def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt")
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for words in line_words:
            story_words.append(words)
    story.close()

    for words in story_words:
        print(words)
        
if __name__ == "__main__":
    fetch_words()