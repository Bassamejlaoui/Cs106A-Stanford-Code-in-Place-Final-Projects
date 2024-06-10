def main():
    translations = {
        "hello": "bonjour",
        "dog": "chien",
        "cat": "chat",
        "well": "bien",
        "us": "nous",
        "nothing": "rien",
        "house": "maison",
        "time": "temps",
        "car": "voiture",
        "book": "livre",
        "school": "école",
        "water": "eau",
        "food": "nourriture",
        "friend": "ami",
        "family": "famille",
        "day": "jour",
        "night": "nuit",
        "love": "amour",
        "child": "enfant",
        "work": "travail",
        "city": "ville",
        "street": "rue",
        "mountain": "montagne",
        "river": "rivière",
        "forest": "forêt",
        "star": "étoile"
    }
    
    num_correct = 0
    
    print("Translate the following English words to French:")
    
    for english_word, french_word in translations.items():
        answer = input(f"{english_word}: ")
        if answer.lower() == french_word:
            print("Correct!")
            num_correct += 1
        else:
            print(f"Incorrect! The correct translation is {french_word}.")
    
    print()
    print(f"You got {num_correct}/{len(translations)} words correct, come study again soon!")

if __name__ == '__main__':
    main()
