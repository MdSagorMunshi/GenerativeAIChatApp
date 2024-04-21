### **Generative AI Chat App**
[![Version](https://img.shields.io/badge/Version-2.0.0-green.svg)](https://github.com/MdSagorMunshi/GenerativeAIChatApp)
[![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=MdSagorMunshi.GenerativeAIChatApp)](https://github.com/MdSagorMunshi/GenerativeAIChatApp)

This project is a Graphical User Interface (GUI) chat application built using Tkinter that allows users to interact with a large language model powered by Google Generative AI. The application provides a user-friendly interface for engaging in conversations with the AI and exploring its capabilities.

### **Features**

*   **Interactive Chat:** Users can type messages and receive responses from the AI model in real-time.
*   **Emoji Support:**  A button is available to insert emojis into chat messages, enhancing expressiveness.
*   **Scrolled Text History:** The chat history is displayed in a scrollable text box, allowing users to review past conversations.
*   **Safety Measures:** The AI model is configured with safety settings to mitigate potential risks of harmful content.
*   **Exit Commands:** Users can type "exit" or "quit" to terminate the chat session.

### **New Features and Changes**

- **Dynamic Subject Naming:** Automatically names session files based on the chat subject.
- **Auto-Saving:** Chat messages are saved automatically without the need for explicit commands.
- **Time Stamping:** Each message in the chat history is timestamped with the current time.
- **Time Box Display:** A small box displays the current time during the chat session.
- **Visual Indication of AI Replies:** AI-generated responses are displayed in a different color for easy differentiation.
- **Emoji Selection:** Users can insert emojis into their messages using a pop-up emoji selection menu.
- **Improved Emoji Button:** The emoji button in the input box offers a more intuitive way to access emojis.
- **Graceful Shutdown:** Closes the visual window and terminates the Python process upon exiting the chat.
- **Environmental Configuration:** Utilizes a `.env` file to manage API keys securely.
- **Enhanced Error Handling:** Error messages are displayed in a distinct color for better visibility.
- **Dependency Management:** New dependency added: `python-dotenv` for managing environment variables.

### **Technologies Used**

*   **Python:** The primary programming language used for the application.
*   **Tkinter:** A Python library for creating graphical user interfaces.
*   **google-generativeai:** The official Python client library for interacting with Google Generative AI models.
*   **python-dotenv:** A Python library for managing environment variables.

### **Installation Instructions**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MdSagorMunshi/GenerativeAIChatApp.git
    ```

2. Change Directory
   ```bash
   cd GenerativeAIChatApp
   ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Obtain a Google Generative AI API Key:** 
    Follow the instructions on the [Google Generative AI Studio](https://aistudio.google.com/app/apikey) to obtain an API key. Once you have the API key, create a file named `.env` in your project directory and add the following line to it:
    ```
    API_KEY=YOUR_API_KEY_HERE
    ```
    Replace `YOUR_API_KEY_HERE` with your actual API key. This file will securely store your API key and ensure it is not exposed in your code.
5.  **Verify the Model Name:**  
    Ensure that the `model_name` variable in the code is set to a valid Generative AI model name. You can find available models and their names in the [Google Generative AI documentation](https://cloud.google.com/python/docs/reference/generativeai/latest).
6.  **Run the application:**
    ```bash
    python chat_gui.py 
    ``` 

### **Usage Instructions**

1.  **Launch the application:** Run the `chat_gui.py` file. 
2.  **Start chatting:** Type your messages into the entry box and press Enter to send them to the AI. 
3.  **Use emojis:** Click the emoji button to select and insert emojis into your messages.
4.  **Review chat history:** Scroll through the text box to see previous messages. 
5.  **Exit the chat:** Type "exit" or "quit" and press Enter to end the conversation and close the application. 

### **Contribution Guidelines**

(Optional) If you'd like others to contribute to your project, you can add a section outlining how they can do so. This might include information on:

*   How to report bugs or suggest features
*   How to submit pull requests
*   Coding style guidelines

### **FAQ**

* **Q: What generative AI models does this app support?**
    * A: Currently, the app is configured to work with the `gemini-1.5-pro-latest` model. However, you can modify the code to use other generative models supported by the `google.generativeai` library. Ensure you have the correct model name and API key. 
* **Q: How do I get an API key?**
    * A: You can obtain an API key by signing up for Google Generative AI and following their instructions. 
* **Q: Can I contribute to this project?**
    * A: Absolutely! Feel free to fork the repository, make improvements, and submit pull requests.


### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
