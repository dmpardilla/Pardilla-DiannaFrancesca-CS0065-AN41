import sys
from textblob import TextBlob

LITERARY_PRESETS = [
    "There is some good in this world, and it is worth fighting for.",
    "In a hole in the ground there lived a hobbit.",
    "It was the worst of times, full of terrible despair and misery.",
    "I am cathedrally happy, and so content with this wonderful life.",
    "A cold, painful gloom fell over the dark and dreary room.",
    "He opened the old book and read the first page in quiet silence.",
    "Whatever our souls are made of, his and mine are pure joy and love.",
    "The heavy iron gate closed with a loud and sharp click.",
    "Each unhappy family is miserable and sorrowful in its own tragic way.",
    "What a brilliant, radiant, and magnificent morning to be alive!"
]

class VibeCheckInspector:
    def __init__(self):
        self.reset_metrics()

    def reset_metrics(self):
        self.results = {"Positive": 0, "Neutral": 0, "Negative": 0}
        self.polarities = []

    def classify_polarity(self, polarity: float) -> str:
        """Categorizes sentiment based on TextBlob polarity score."""
        if polarity < 0:
            return "Negative"
        elif polarity == 0:
            return "Neutral"
        elif 0 < polarity <= 1:
            return "Positive"

    def process_sentence(self, sentence: str, index: int, total: int):
        blob = TextBlob(sentence)
        p = blob.sentiment.polarity
        sentiment_tag = self.classify_polarity(p)
        
        self.results[sentiment_tag] += 1
        self.polarities.append(p)
        
        print(f"[{index:02d}/{total:02d}] Text: \"{sentence}\"")
        print(f"     └─ Polarity Score: {p:+.4f} | Sentiment: [{sentiment_tag}]\n")

    def display_summary(self, total_runs: int):
        avg_polarity = sum(self.polarities) / len(self.polarities) if self.polarities else 0.0
        
        print("\n" + "═" * 65)
        print("                  BATCH SENTIMENT SUMMARY METRICS                 ")
        print("═" * 65)
        print(f" Total Evaluated   : {total_runs}")
        print(f" Mean Polarity     : {avg_polarity:+.4f}")
        print("-" * 65)
        
        for category, count in self.results.items():
            percentage = (count / total_runs) * 100
            bar = "█" * int(percentage // 5)
            print(f" {category:<10} | {count:2d} ({percentage:5.1f}%) | {bar}")
            
        print("═" * 65 + "\n")

    def run_manual_batch(self, count: int = 10):
        self.reset_metrics()
        print(f"\n--- MANUAL ENTRY BATCH MODE ({count} SENTENCES) ---")
        for i in range(1, count + 1):
            text = input(f"Enter sentence {i}/{count}: ").strip()
            self.process_sentence(text, i, count)
        self.display_summary(count)

    def run_preset_batch(self):
        self.reset_metrics()
        total = len(LITERARY_PRESETS)
        print(f"\n--- LITERARY CLASSIC PRESET BATCH ({total} SENTENCES) ---")
        for i, text in enumerate(LITERARY_PRESETS, start=1):
            self.process_sentence(text, i, total)
        self.display_summary(total)

    def run_single_check(self):
        print("\n--- QUICK SINGLE SENTENCE TEST ---")
        text = input("Enter a sentence to test: ").strip()
        blob = TextBlob(text)
        p = blob.sentiment.polarity
        tag = self.classify_polarity(p)
        print(f"-> Polarity Score : {p:+.4f}")
        print(f"-> Sentiment Tag  : {tag}\n")

    def show_main_menu(self):
        while True:
            print("=================================================================")
            print("    VIBECHECK 3000: TEXTBLOB POLARITY BATCH INSPECTOR            ")
            print("    Programmed by Pardilla and Vergara - AN41                    ")
            print("=================================================================")
            print("  [1] Run 10-Sentence Manual Entry Batch")
            print("  [2] Run Literary Classics Preset Batch (10 Famous Quotes)")
            print("  [3] Single Sentence Quick Check")
            print("  [4] Exit Program")
            print("=================================================================")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":
                self.run_manual_batch(10)
            elif choice == "2":
                self.run_preset_batch()
            elif choice == "3":
                self.run_single_check()
            elif choice == "4":
                print("\nExiting VibeCheck 3000. Have a great day!")
                break
            else:
                print("\n[!] Invalid selection. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    app = VibeCheckInspector()
    app.show_main_menu()