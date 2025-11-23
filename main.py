from agents.parent import ParentAgent

if __name__ == "__main__":
    bot = ParentAgent()

    while True:
        user_input = input("Ask something: ")

        if user_input.lower() == "exit":
            break

        response = bot.process(user_input)
        print("\n" + response + "\n")
