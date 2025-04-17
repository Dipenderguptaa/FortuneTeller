import random

def main():
    print("🔮 Welcome to Deepander Gupta's Fortune Teller (21JE0290) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral/excited/stressed/confused/motivated/lazy): ").lower()
    
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

    excited_fortunes = [
        "✨ Your fortune: Let your excitement fuel a bold new idea today! ✨",
        "✨ Your fortune: Deepander Gupta’s spark will ignite motivation in those around him! ✨",
        "✨ Your fortune: Your enthusiasm is magnetic—expect great things to follow! ✨"
    ]

    stressed_fortunes = [
        "✨ Your fortune: Breathe deeply—this storm will pass, and peace will follow. ✨",
        "✨ Your fortune: Deepander Gupta, every challenge makes you more unshakable. ✨",
        "✨ Your fortune: Today’s tension is tomorrow’s growth in disguise. ✨"
    ]

    confused_fortunes = [
        "✨ Your fortune: Answers have a way of arriving when you quiet the noise. ✨",
        "✨ Your fortune: Deepander Gupta, let your gut feeling lead the way through this fog. ✨",
        "✨ Your fortune: Confusion is just the beginning of discovery. ✨"
    ]
    
    motivated_fortunes = [
        "✨ Your fortune: Your drive today will open doors you didn’t know existed. ✨",
        "✨ Your fortune: Deepander Gupta, your determination is unstoppable—keep pushing forward! ✨",
        "✨ Your fortune: Every small effort adds up—success is closer than you think. ✨"
    ]

    lazy_fortunes = [
        "✨ Your fortune: Rest is productive too—sometimes doing nothing is doing something. ✨",
        "✨ Your fortune: Deepander Gupta, take it easy today—your chill vibe is unmatched. ✨",
        "✨ Your fortune: Even the sun takes a break at night—you’ve earned yours too. ✨",
        "✨ Your fortune: Great ideas often come when you’re lying down doing absolutely nothing. ✨"
    ]

    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))   
    elif mood == "excited":
        print(random.choice(excited_fortunes))
    elif mood == "stressed":
        print(random.choice(stressed_fortunes))
    elif mood == "confused":
        print(random.choice(confused_fortunes))
    elif mood == "motivated":
        print(random.choice(motivated_fortunes))
    elif mood == "lazy":
        print(random.choice(lazy_fortunes))
    else:
        print("✨ Your fortune: I cannot read your mood, but Deepander Gupta's destiny is still bright! ✨")

if __name__ == "__main__":
    main()