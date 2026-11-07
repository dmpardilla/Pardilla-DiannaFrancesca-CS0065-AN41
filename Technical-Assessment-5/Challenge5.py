import re

HAPPY_LEXICON = {
    "happy", "joy", "joyful", "delighted", "cheerful", "ecstatic", "glad",
    "content", "excited", "blessed", "wonderful", "amazing", "great", "love",
    "loving", "awesome", "fantastic", "pleased", "radiant", "thrilled", "sunny",
    "smile", "smiling", "laugh", "laughing", "good", "best", "brilliant", "vibrant",
    "triumphant", "peaceful", "elated", "optimistic", "thriving", "splendid"
}

SAD_LEXICON = {
    "sad", "unhappy", "depressed", "gloomy", "heartbroken", "miserable",
    "sorrowful", "down", "disappointed", "mournful", "tragic", "crying",
    "cry", "upset", "grief", "pain", "hurt", "despair", "melancholy",
    "terrible", "bad", "awful", "horrible", "lonely", "dejected", "somber",
    "dreary", "heartbreaking", "distressed", "disheartened"
}

LITERARY_TEST_PRESETS = {
    "1": ("Happy Dominant", "She felt delighted, cheerful, and ecstatic in the warm sunny garden."),
    "2": ("Sad Dominant", "He sat alone feeling sad, gloomy, and miserable in the dreary town."),
    "3": ("Neutral / Tie", "Though she was sad to leave home, she felt glad and excited for the adventure ahead.")
}

def _extract_tokens(text: str) -> list[str]:
    """Normalizes input text and tokenizes into lowercase alphabetic words."""
    return re.findall(r'\b[a-z]+\b', text.lower())

def number_happy(sentence: str) -> int:
    """Returns the total count of happy dataset words present in the sentence."""
    tokens = _extract_tokens(sentence)
    return sum(1 for token in tokens if token in HAPPY_LEXICON)

def number_sad(sentence: str) -> int:
    """Returns the total count of sad dataset words present in the sentence."""
    tokens = _extract_tokens(sentence)
    return sum(1 for token in tokens if token in SAD_LEXICON)

def perform_lexical_analysis(sentence: str):
    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)

    tokens = _extract_tokens(sentence)
    matched_happy = [t for t in tokens if t in HAPPY_LEXICON]
    matched_sad = [t for t in tokens if t in SAD_LEXICON]

    if happy_count > sad_count:
        analysis_statement = "The tone of the sentence is Happy (Positive)."
    elif sad_count > happy_count:
        analysis_statement = "The tone of the sentence is Sad (Negative)."
    else:
        analysis_statement = "The tone of the sentence is Neutral."

    print("\n" + "─" * 58)
    print("                   TONE ANALYSIS BREAKDOWN                ")
    print("─" * 58)
    print(f" Target Sentence   : \"{sentence}\"")
    print(f" Happy Words Count : {happy_count:<2d} | Matched: {matched_happy}")
    print(f" Sad Words Count   : {sad_count:<2d} | Matched: {matched_sad}")
    print("─" * 58)
    print(f" FINAL STATEMENT   : {analysis_statement}")
    print("─" * 58 + "\n")

def view_lexicon_datasets():
    print("\n" + "=" * 58)
    print("                 LOADED LEXICON DATASETS                  ")
    print("=" * 58)
    print(f" Happy Vocabulary ({len(HAPPY_LEXICON)} words):")
    print(" ", ", ".join(sorted(HAPPY_LEXICON)))
    print("-" * 58)
    print(f" Sad Vocabulary ({len(SAD_LEXICON)} words):")
    print(" ", ", ".join(sorted(SAD_LEXICON)))
    print("=" * 58 + "\n")

def run_preset_menu():
    print("\n--- SELECT A LITERARY PRESET ---")
    for key, (label, text) in LITERARY_TEST_PRESETS.items():
        print(f"  [{key}] {label}: \"{text}\"")
    
    preset_choice = input("Select preset (1-3): ").strip()
    if preset_choice in LITERARY_TEST_PRESETS:
        _, quote = LITERARY_TEST_PRESETS[preset_choice]
        perform_lexical_analysis(quote)
    else:
        print("\n[!] Invalid preset selection.\n")

def show_main_menu():
    while True:
        print("┌──────────────────────────────────────────────────────────┐")
        print("│         LEXIMOOD: THE HAPPY VS. SAD WORD SHOWDOWN        │")
        print("│         Programmed by Pardilla and Vergara - AN41        │")
        print("└──────────────────────────────────────────────────────────┘")
        print("  [1] Analyze Custom Sentence")
        print("  [2] Analyze Literary Preset Quotes")
        print("  [3] View Loaded Happy/Sad Lexicon Datasets")
        print("  [4] Exit Program")
        print("────────────────────────────────────────────────────────────")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            text = input("\nEnter a sentence to dissect: ").strip()
            if text:
                perform_lexical_analysis(text)
            else:
                print("\n[!] Input sentence cannot be empty.\n")
        elif choice == "2":
            run_preset_menu()
        elif choice == "3":
            view_lexicon_datasets()
        elif choice == "4":
            print("\nExiting LexiMood. Have a great day!")
            break
        else:
            print("\n[!] Invalid selection. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    show_main_menu()