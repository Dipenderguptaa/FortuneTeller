import random

def main():
    print("🔮 Welcome to Deepander Gupta's Fortune Teller (21JE0290) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    happy_fortunes = [
        "✨ Your fortune: Wonderful moments lie ahead, Deepander Gupta! Keep that smile alive. ✨",
        "✨ Your fortune: Your cheerful vibe will bring exciting chances your way today! ✨",
        "✨ Your fortune: The world feels brighter when you're happy—keep spreading that joy! ✨"
    ]

    sad_fortunes = [
        "✨ Your fortune: Hang in there—joyful days are just around the corner. ✨",
        "✨ Your fortune: Even when it feels tough, Deepander Gupta, your inner strength shines. ✨",
        "✨ Your fortune: Sadness fades with time; happiness is patiently waiting for you. ✨"
    ]

    neutral_fortunes = [
        "✨ Your fortune: Staying balanced will guide you smoothly through the day. ✨",
        "✨ Your fortune: Deepander Gupta, your steady nature might uncover something unexpected. ✨",
        "✨ Your fortune: You're walking a steady road—trust in your journey. ✨"
    ]

    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))   
    else:
        print("✨ Your fortune: I cannot read your mood, but Deepander Gupta's destiny is still bright! ✨")

if __name__ == "__main__":
    main()