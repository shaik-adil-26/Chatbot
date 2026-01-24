class ChatBot:
    def __init__(self, name):
        # Bot name
        self.name = name

        # Bot knowledge (memory)
        self.knowledge = {
            "course": "We offer Python, AI, ML and Data courses.",
            "fees": "Fee details are available with the admin team.",
            "timing": "Classes usually run for 4 hours daily.",
            "location": "Our academy is located in the city center."
        }

    def greet(self):
        print(f"\n{self.name}: Hi! I am {self.name}. Type 'bye' to exit.\n")

    def get_reply(self, user_text):
        # Greeting logic
        if user_text in ["hi", "hello", "hey"]:
            return "Hello! How can I help you?"

        # Keyword matching using dictionary
        for key in self.knowledge:
            if key in user_text:
                return self.knowledge[key]

        # Default response
        return "Sorry, I didn't understand. Try asking about course, fees, timing, or location."

    def run(self):
        self.greet()

        while True:
            user_text = input("You: ").lower().strip()

            if user_text == "bye":
                print(f"{self.name}: Goodbye! Have a great day.")
                break

            reply = self.get_reply(user_text)
            print(f"{self.name}: {reply}")


# Create object and start chatbot


bot = ChatBot("Chat Bot")
bot.run()
