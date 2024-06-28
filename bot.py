import time
import tweepy
import keys as keys

# Initialize Tweepy
client = tweepy.Client(
    consumer_key=keys.api_key,
    consumer_secret=keys.api_key_secret,
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret
)

# Define variables
word_count = 0
words = []

# Function to sort words from file
def sort_words():
    global words
    with open('shakespeare.txt', 'r') as file:
        words = file.read().split()

# Function to get the next word
def get_word():
    global word_count
    word_count += 1
    if word_count < len(words):
        log_word_count()
        return words[word_count]
    else:
        return None

# Function to log the current word count to a file
def log_word_count():
    with open('word_count.log', 'w') as log_file:
        log_file.write(str(word_count))

# Function to read the word count from the log file
def read_word_count():
    global word_count
    try:
        with open('word_count.log', 'r') as log_file:
            word_count = int(log_file.read().strip())
    except FileNotFoundError:
        word_count = -1
    except ValueError:
        word_count = -1

# Function to tweet the word
def tweet(word: str):
    try:
        client.create_tweet(text=word)
        print("Tweeted successfully")
    except tweepy.TweepyException as e:
        print(f"Error occurred: {e}")

# Main execution
if __name__ == '__main__':
    read_word_count()
    sort_words()

    while True:
        time.sleep(1)
        word = get_word()
        if word:
            print(word)
        else:
            print("Could not fetch a word")