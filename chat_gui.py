import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Generative AI Chat")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.user_input_frame = tk.Frame(master)
        self.user_input_frame.pack(expand=True, fill=tk.X)

        self.user_input = tk.Entry(self.user_input_frame)
        self.user_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.user_input.insert(0, "Type here...")
        self.user_input.bind("<FocusIn>", self.clear_placeholder)
        self.user_input.bind("<FocusOut>", self.restore_placeholder)
        self.user_input.bind("<Return>", self.send_message)

        self.emoji_button = tk.Button(self.user_input_frame, text="😊", command=self.open_emoji_popup)
        self.emoji_button.pack(side=tk.RIGHT)

        # Replace with your actual API key
        api_key = "AIzaSyBYV85DejQJyVE6gkCBfMVwXKyJZ6KAuGg"

        # Model Configuration (ensure the model name is valid)
        model_name = "gemini-1.5-pro-latest"  # Verify the correct model name

        # Generation Settings
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192
        }

        # Safety Settings
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]

        # Configure API Key
        genai.configure(api_key=api_key)

        # Create Generative Model Instance
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Start Chat Session
        self.chat = self.model.start_chat()

        self.chat_history.insert(tk.END, "AI: Welcome to the Generative AI Chat!\n")
        self.chat_history.insert(tk.END, "AI: Type 'exit' or 'quit' to end the conversation.\n")

    def send_message(self, event=None):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_input.lower() in ["exit", "quit"]:
            self.chat_history.insert(tk.END, "AI: Goodbye!\n")
            return

        response = self.chat.send_message(user_input)
        self.chat_history.insert(tk.END, f"You: {user_input}\n")
        self.chat_history.insert(tk.END, f"AI: {response.text}\n")
        self.chat_history.see(tk.END)

    def open_emoji_popup(self):
        emoji_popup = tk.Toplevel(self.master)
        emoji_popup.title("Select Emoji")

        emojis = ["😊", "😂", "😍", "😎", "👍", "👋", "❤", "🎉", "🤔", "😢", "🙄", "😳", "😱", "🤯", "🤣", "😇", "🥳", "🤩"]

        def insert_emoji(emoji):
            self.user_input.insert(tk.END, emoji)
            emoji_popup.destroy()

        for emoji in emojis:
            tk.Button(emoji_popup, text=emoji, command=lambda e=emoji: insert_emoji(e)).pack()

    def clear_placeholder(self, event):
        if self.user_input.get() == "Type here...":
            self.user_input.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.user_input.get():
            self.user_input.insert(0, "Type here...")

def main():
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
