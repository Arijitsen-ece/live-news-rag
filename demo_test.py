from news import get_news
import time

print("First fetch:")
news1 = get_news()
for n in news1:
    print(n["title"])

print("\nWaiting 60 seconds...\n")
time.sleep(60)

print("Second fetch:")
news2 = get_news()
for n in news2:
    print(n["title"])
