### Final Project: English to French Vocabulary Quizzlet

<!-- # Code-In-Place-By-Stanford-University

Code In Place 2024 Final Project -->

<p align="center">
  <a href="https://codeinplace.stanford.edu">
    <img width="200px" src="https://github.com/xiaowuc2/xiaowuc2/blob/master/source/82601797.png" alt="Logo">
  </a>
  <h3 align="center"> Stanford Cs106A Code in Place 2024 Final Project</h3>  
  <p align="center">
  </p>
</p>

```diff

Code in Place is an act of community service over 900 teachers from around the world came together to 
offer a first-of-its-kind volunteer-led course called Code in Place, hosted by Stanford University. 
Code in Place was a great, uplifting, learning experience and over 10,000 students learned how to code 
in Python.

```

#### Overview:
This project is an interactive English to French vocabulary quiz, designed as a final project for the CS106A Stanford Code in Place 2024 course. The objective is to create an engaging application that helps users practice and learn basic French vocabulary. 

#### Features:
- **User Interaction:** Prompts users to translate English words into French.
- **Instant Feedback:** Provides immediate feedback on the user's input.
- **Score Tracking:** Keeps track of correct answers and displays the total score at the end.

#### How It Works:
1. **Initialize Translations:** The program starts by initializing a dictionary containing 25 common English words along with their French translations.
2. **User Prompts:** The user is prompted to input the French translation for each given English word.
3. **Answer Checking:** The user's answer is checked against the correct French translation. Feedback is provided for each response.
4. **Score Summary:** At the end of the quiz, the program displays the number of correct answers out of the total number of words.

#### Sample Words:
The quiz includes translations for words such as "hello" (bonjour), "dog" (chien), "cat" (chat), "house" (maison), and "love" (amour), among others.

#### Code:
```python
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
```


### Conclusion:
This English to French Vocabulary Quiz is a great way to engage users in learning a new language. It offers a fun and interactive method to practice vocabulary, making the learning process enjoyable. By providing immediate feedback and tracking scores, users are encouraged to improve through repeated practice.
