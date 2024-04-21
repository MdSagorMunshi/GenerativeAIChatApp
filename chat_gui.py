import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Generative AI Chat")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.user_input_frame = tk.Frame(master)
        self.user_input_frame.pack(expand=True, fill=tk.X)

        self.user_input = tk.Entry(self.user_input_frame)
        self.user_input.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)  # Increase size of input box
        self.user_input.insert(0, "Type here...")
        self.user_input.bind("<FocusIn>", self.clear_placeholder)
        self.user_input.bind("<FocusOut>", self.restore_placeholder)
        self.user_input.bind("<Return>", self.send_message)
        self.user_input.bind("<Control-a>", self.select_all_text)

        self.emoji_button = tk.Button(self.user_input_frame, text="😊", command=self.open_emoji_popup)
        self.emoji_button.pack(side=tk.RIGHT)

        # Small box to display current date and time
        self.time_date_frame = tk.Frame(master)
        self.time_date_frame.pack(fill=tk.X)
        self.current_time_label = tk.Label(self.time_date_frame, text="", padx=5)
        self.current_time_label.pack(side=tk.RIGHT)
        self.update_time()

        # Get API key from environment variable
        api_key = os.getenv("API_KEY")

        if not api_key:
            messagebox.showerror("Error", "API key not found. Please set the API_KEY environment variable in the .env file.")
            master.destroy()
            return

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
        self.current_session_file = None  # Track the current session file
        self.subject = ""  # Subject to be determined
        self.waiting_for_subject = True  # Flag to indicate if waiting for subject

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=current_time)
        self.current_time_label.after(1000, self.update_time)

    def send_message(self, event=None):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if self.waiting_for_subject:
            self.subject = user_input.strip()  # Extract subject from the first user input
            self.waiting_for_subject = False  # No longer waiting for subject
            self.start_new_session()  # Start new session with the determined subject
            self.chat_history.insert(tk.END, f"You: {user_input}\n", "user_message")
            self.send_first_message()  # Send the first AI message
            return

        if user_input.lower() in ["exit", "quit"]:
            self.chat_history.insert(tk.END, "AI: Goodbye, See you soon..! 😊\n")
            self.save_message(f"AI: Goodbye, See you soon..! 😊\n")
            print("Goodbye, See you soon..! 😊")  # Display in terminal
            self.master.destroy()  # Close the visual window
            os._exit(0)  # Close the Python file
            return

        response = self.chat.send_message(user_input)
        self.chat_history.insert(tk.END, f"You: {user_input}\n", "user_message")
        self.chat_history.insert(tk.END, f"AI: {response.text}\n", "ai_message")
        self.chat_history.see(tk.END)
        self.save_message(f"You: {user_input}\nAI: {response.text}\n")  # Save the message

    def save_message(self, message):
        if self.current_session_file:
            self.current_session_file.write(message)
            self.current_session_file.flush()  # Flush to ensure immediate write to file

    def start_new_session(self):
        # Close the previous session file if open
        if self.current_session_file:
            self.current_session_file.close()

        # Create a new session file
        current_time = datetime.now().strftime("%d_%b_%Y_%H_%M_%S")
        subject = self.subject.replace(" ", "_")  # Replace spaces with underscores
        session_filename = f"Chat_List/{subject}_{current_time}.txt"
        os.makedirs(os.path.dirname(session_filename), exist_ok=True)
        self.current_session_file = open(session_filename, "w")

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

    def select_all_text(self, event):
        self.user_input.select_range(0, tk.END)

    def send_first_message(self):
        first_message = self.chat.send_message("Hello")  # Send a starting message
        self.chat_history.insert(tk.END, f"AI: {first_message.text}\n", "ai_message")
        self.chat_history.see(tk.END)
        self.save_message(f"AI: {first_message.text}\n")

def main():
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    # Adding text color tags
    chat_gui.chat_history.tag_config("user_message", foreground="blue")
    chat_gui.chat_history.tag_config("ai_message", foreground="green")
    root.mainloop()

    print("Goodbye, See you soon..! 😊")  # Display in terminal

if __name__ == "__main__":
    main()
