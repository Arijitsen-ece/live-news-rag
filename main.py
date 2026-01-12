import time
from news import get_news
from rag import answer
from logger import log_update

REFRESH_INTERVAL = 60
last_refresh = 0
news = []

def refresh_news():
    global news, last_refresh
    print("\nFetching latest news...")
    news = get_news()
    log_update(news)
    last_refresh = time.time()

    print("Latest News Loaded:")
    for i, n in enumerate(news, 1):
        print(f"{i}. {n['title']}")

def run():
    refresh_news()

    while True:
        if time.time() - last_refresh >= REFRESH_INTERVAL:
            refresh_news()

        q = input("\nAsk question (or type exit): ")
        if q.lower() == "exit":
            break

        print("\nAnswer:\n", answer(q, news))

if __name__ == "__main__":
    run()
