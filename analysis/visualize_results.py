import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import string

# Input file path
file_path = os.path.join("..", "output", "result.txt")

data = []

# Read and clean data
with open(file_path, "r", encoding="latin1") as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("##") or line.startswith("#*"):
            continue
        try:
            hashtag, count_str = line.rsplit(maxsplit=1)
            count_cleaned = re.sub(r"\D", "", count_str)
            if not count_cleaned:
                continue
            count = int(count_cleaned)
            data.append((hashtag.strip(), count))
        except ValueError:
            continue

df = pd.DataFrame(data, columns=["Hashtag", "Count"])

def clean_text(text):
    printable = set(string.printable)
    return ''.join(filter(lambda x: x in printable, text))

df["Hashtag"] = df["Hashtag"].apply(clean_text)

# Plot and save
if df.empty:
    print("No valid data found to plot.")
else:
    df = df.sort_values(by="Count", ascending=False).head(20)
    plt.figure(figsize=(12, 8))
    plt.barh(df["Hashtag"], df["Count"], color="skyblue")
    plt.xlabel("Count")
    plt.ylabel("Hashtag")
    plt.title("Top 20 Hashtags by Count")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    output_dir = os.path.join("plots")
    os.makedirs(output_dir, exist_ok=True) 
    save_path = os.path.join(output_dir, "top_hashtags.png")
    plt.savefig(save_path, dpi=300)
    print(f"Plot saved to: {save_path}")

    plt.show()
