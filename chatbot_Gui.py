import random
import tkinter as tk
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],

    "how are you": [
        "I am fine!",
        "Doing great!",
        "I'm good. What about you?"
    ],

    "thank you": [
        "You're welcome!",
        "Glad to help!",
        "No problem!"
    ],
    "good morning":[
        "Good morning!",
        "Good morning have a nice day!",
        "What do you want to talk"
    ],
    "tell me a joke": [
    "Why did the computer sleep? Because it was tired!",
    "Why do programmers hate bugs? Because bugs are annoying!",
    "Why was the laptop cold? It left its Windows open!"
],

"good evening": [
    "Good evening!",
    "Hope you had a great day!",
    "Good evening! How are you today?"
],

"what is python": [
    "Python is a programming language.",
    "Python is easy and beginner-friendly.",
    "Python is widely used in AI and web development."
],

"who are you": [
    "I am a simple Python chatbot.",
    "I am your chatbot friend!",
    "I was created using Python."
],

"motivate me": [
    "Keep learning. You are improving every day!",
    "Small steps lead to big success.",
    "Believe in yourself and keep coding!"
]
}
math={
    "2+2":"4",
    "3+3":"6",
    "4+4":"8"
}
def chatbot_reply(user):
    
    if user == "bye":
        return "Goodbye!"

    elif user in responses:
        return random.choice(responses[user])
    elif user in math:
        return math[user]

    else:
        return "Sorry, I don't understand."


def send_message():

    user = entry_box.get().lower()

    chat_area.insert(tk.END, "You: " + user + "\n")

    reply = chatbot_reply(user)

    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")

    entry_box.delete(0, tk.END)


window = tk.Tk()
window.title("Simple Chatbot")
window.geometry("700x700")
window.configure(bg="lightblue")
window.bind('<Return>', lambda event: send_message())


heading = tk.Label(
    window,
    text="Simple Python Chatbot",
    font=("Arial", 22, "bold")
)

heading.pack(pady=10)
chat_area = tk.Text(window, height=25, width=60)
chat_area.pack(pady=10)

entry_box = tk.Entry(window, width=70)
entry_box.pack(pady=5)
entry_box.focus()

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

window.mainloop()
