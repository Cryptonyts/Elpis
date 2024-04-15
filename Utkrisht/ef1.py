import random
import sys, fitz  # import the bindings
#fname = sys.argv[1]  # get filename from command line
doc = fitz.open('lec.pdf')  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("./fold/page-%i.png" % page.number)  # store image as a PNG






    ######
    
'''
class DyslexiaLearningAssistant:
    def __init__(self):
        self.words = ["cat", "dog", "house", "apple", "banana"]
        self.current_word_index = 0
        self.score = 0

    def display_menu(self):
        print("1. Learn Words")
        print("2. Quiz")
        print("3. Exit")

    def learn_words(self):
        print("\n-- Learning Mode --")
        print("Type the word you see correctly to move to the next one.")
        print("Type 'quit' to exit learning mode.")
        
        while self.current_word_index < len(self.words):
            word = self.words[self.current_word_index]
            user_input = input(f"Word: {word} - Type it: ")
            
            if user_input.lower() == "quit":
                break
            
            if user_input.lower() == word:
                print("Correct!")
                self.score += 1
                self.current_word_index += 1
            else:
                print("Incorrect. Try again.")

    def quiz(self):
        print("\n-- Quiz Mode --")
        print("Choose the correct word for each definition.")
        print("Type 'quit' to exit quiz mode.")
        
        while True:
            word = random.choice(self.words)
            definition = f"A small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws. ({word[0]}****)"
            options = [word] + random.sample(self.words, k=3)
            random.shuffle(options)

            print(f"\nDefinition: {definition}")
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            user_input = input("Your choice: ")
            
            if user_input.lower() == "quit":
                break
            
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                chosen_word = options[int(user_input) - 1]
                if chosen_word == word:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect. The correct answer was:", word)
            else:
                print("Invalid input. Please choose a number between 1 and 4.")

    def start(self):
        print("Welcome to the Dyslexia Learning Assistant!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.learn_words()
            elif choice == "2":
                self.quiz()
            elif choice == "3":
                print("Thanks for using the Dyslexia Learning Assistant!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    assistant = DyslexiaLearningAssistant()
    assistant.start()
'''