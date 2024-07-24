# AI Chatbot with integration of OpenAI API key

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Key](#api-key)
5. [Dependencies](#dependencies)
6. [License](#license)

## Project Overview
The DSA Expert Chatbot is an interactive web application that utilizes OpenAI's GPT-3.5-turbo model to provide expert-level answers to questions related to data structures and algorithms. With a simple user interface powered by Gradio, users can engage in real-time conversations with the chatbot.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/rohit-borole/AI-Chatbot-with-integration-of-OpenAI-API-key.git
    cd dsa-expert-chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install openai gradio
    ```

## Usage
1. **Set your OpenAI API Key**: Replace the placeholder in the code with your actual OpenAI API key.
    ```python
    openai.api_key = "your_openai_api_key_here"
    ```

2. **Run the chatbot**:
    ```sh
    python app.py
    ```

3. **Interact with the chatbot**: Once the application is running, a Gradio interface will be launched. You can input your questions related to data structures and algorithms, and receive expert-level responses.

## API Key
You need an OpenAI API key to use this application. Sign up at [OpenAI](https://platform.openai.com/signup) to get your API key and replace the existing one in the script.

## Dependencies
This project requires the following Python packages:
- `openai`: For interacting with the OpenAI API.
- `gradio`: For creating the web interface.

You can install these dependencies using:
```sh
pip install -r requirements.txt
```

**Sample `requirements.txt`:**
```
openai
gradio
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.



Feel free to customize this README file to better fit your project's specifics and any additional details you want to include!
