# PyWebIO ChatGPT Integration with Nagai.ai

This repository showcases an integration of PyWebIO and Nagai.ai for building a conversational chatbot powered by ChatGPT.

## Requirements

Before running the code in this repository, make sure you have the following dependencies installed:

- Python 3.6+
- PyWebIO 1.8.0+
- OpenAI GPT library
- Nagai.ai
- Additional plugins (such as WolframAlpha)

## Usage

To use this integration and communicate with ChatGPT, follow the steps below:

1. Install the necessary dependencies by running `pip install -r requirements.txt`.
2. Customize the `config.py` file and set up the required plugins (e.g., WolframAlpha), ChatGPT models, and any additional settings.
3. Obtain your API key by following the instructions provided in the Nagai.ai Discord channel. In the Discord chat, enter the command "I bot /key get" to retrieve your key.
4. Update the `config.py` file with your Nagai.ai API key.
5. Run the `main.py` script to start the PyWebIO server.
6. Open the provided URL in your browser and start interacting with the chatbot.

## Additional Information

- The chatbot is powered by Nagai.ai, which provides an easy-to-use interface for integrating chatbots with different frameworks or platforms.
- PyWebIO is used as the web user interface for the chatbot, allowing for interactive and real-time conversations with the user.
- The integration supports the use of plugins like WolframAlpha, which can extend the chatbot's functionality and allow for advanced computations or queries.
- The file upload feature is included but may have limited functionality currently. Future updates will address this issue and improve file handling capabilities.
- The integration is open to future updates, including the addition of more plugins and support for new ChatGPT models.
- Make sure to refer to the documentation provided by Nagai.ai for more information on integrating plugins and utilizing different models.

## Feedback and Contributions

Feel free to provide any feedback or suggestions for this integration by opening an issue. Contributions are also welcome; simply fork this repository and submit a pull request with your changes.

Let's collaborate and improve the PyWebIO ChatGPT integration with Nagai.ai together!
