import json
from collections import Counter

with open("../dist/chr/allof.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nick_counts = Counter(item["nick"] for item in data)
sorted_nickCounts = nick_counts.most_common()

ranked_data = [{"rank": rank, "nick": nick, "count": count} for rank, (nick, count) in enumerate(sorted_nickCounts, start=1)]

with open("../dist/chr/ranksg.json", "w", encoding="utf-8") as f:
    json.dump(ranked_data, f, indent=4, ensure_ascii=False)