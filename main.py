print("================================")
print("      FATHER CHATBOT            ")
print("================================")

while True:
    question = input("\nAsk something about my father: ").lower()

    if "name" in question:
        print("My father's name is Niaz Ali.")

    elif "age" in question:
        print("My father is 45 years old.")

    elif "job" in question or "work" in question:
        print("My father works as a labourer.")

    elif "city" in question or "live" in question:
        print("My father lives in Kabirwala.")

    elif "hobby" in question:
        print("My father's hobby is cooking.")

    elif "father" in question and "tell" in question:
        print("My father's name is Niaz Ali. He is 45 years old, works as a labourer, lives in Kabirwala, and loves cooking.")

    elif question == "bye":
        print("Goodbye! Have a nice day.")
        break

    else:
        print("Sorry, I only know information about my father.")