print("=" *100)
print("Welcome to the Smart Text Analyzer!")
print("=" *100)
print("Type or paste(Ctrl+V) your text below, and when you're done, type 'exit' and press (Enter) to see the analysis results.")
lines= []
while True:
    Enter_text = input("Enter text to analyze:\n ")  # Prompt the user for input text
    if Enter_text.lower() == "exit":
        print("*" * 130)
        print(" NOTE: If your input text come to end, then just write (exit) ,so the program will display the analysis result.")
        

        print("Thanks for entering your lovely text!")
        print("=" * 130)
        break
    lines.append(Enter_text)  # Store the input text in a list for further processing
text = " ".join(lines)  # Join the list into a single string for analysis
text = text.lower()  # Convert the text to lowercase for consistent analysis

print(">" * 50)
print("This is the Analysis's result!")
print("<" * 50)
count_words = len(text.split())
print(f"Number of words: {count_words}")

pharagraphs_count = text.count('\n')+1  # Count the number of paragraphs based on newlines
print(f"Number of paragraphs: {pharagraphs_count}")

count_characters = len(text.replace(" ", ""))  # Count characters excluding spaces
print(f"Number of characters (excluding spaces): {count_characters}")

count_sentence = 0
for char in text:  # Count the number of sentences based on punctuation marks
    if char in ".,;:!?\"\'-()[]{}":
        count_sentence += 1
print(f"Number of sentences: {count_sentence}")

count_punctuation = 0
for char in text:
    if char in ".,;:!?\"\'-()[]{}":
       count_punctuation += 1
print(f"Number of punctuations: {count_punctuation}")


count_digits= 0
for char in text:
    if char in "0123456789":
        count_digits += 1
print(f"Number of digits: {count_digits}")

count_vowle= "aeiou"
text_lower = text.lower()  # Convert the text to lowercase for vowel counting
print("Vowel Count:")
for vowel in count_vowle:
    print(f"\n{vowel}: {text_lower.count(vowel)}")
    
print("=" * 50)
print("Thanks for using the Smart text Analyzer!")
print("=" * 50)

