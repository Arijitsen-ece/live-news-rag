from datetime import datetime

def log_update(news):
    with open("update_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== Update at {datetime.now()} ===\n")
        for n in news:
            f.write(f"- {n['title']}\n")
