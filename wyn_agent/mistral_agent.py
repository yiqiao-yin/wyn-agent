import os
import re
import subprocess
from mistralai import Mistral
from typing import Optional, Any

class ChatBot:
    def __init__(self, api_key: str, agent_id: str):
        """
        Initializes the ChatBot with the given API key.

        Args:
            api_key (str): The API key for accessing Mistral services.
        """
        self.client = Mistral(api_key=api_key)
        self.agent_id = agent_id
        self.history = []

    def generate_response(self, user_message: str) -> str:
        """
        Generates a response from the chatbot based on the user's message.

        Args:
            agent_id (str): The ID of the agent to interact with.
            user_message (str): The message sent by the user.

        Returns:
            str: The response from the chatbot.
        """
        # Add the user's message to the history
        self.history.append({
            "role": "user",
            "content": user_message
        })

        # Send the message to the API and get the response
        chat_response = self.client.agents.complete(
            agent_id=self.agent_id,
            messages=self.history,
        )

        # Extract the AI's response and add it to the history
        ai_response = chat_response.choices[0].message.content
        self.history.append({
            "role": "assistant",
            "content": ai_response
        })

        # Return the AI's response
        return ai_response

    def get_history(self) -> list:
        """
        Returns the conversation history.

        Returns:
            list: The conversation history.
        """
        return self.history

    def isolate_and_save_python_code(self, input_string: str, file_path: str) -> Optional[str]:
        """
        Extracts Python code from a given input string and saves it to a file.

        This function looks for a block of text that is enclosed within triple backticks (```),
        specifically targeting blocks that start with ```python.

        Args:
            input_string (str): The input string containing the Python code block.
            file_path (str): The path where the extracted Python code will be saved.

        Returns:
            Optional[str]: The path to the saved file if the Python code block is found and saved, else None.
        """
        # Define the pattern to match the Python code block
        pattern = r'```python\s*(.*?)\s*```'

        # Search for the pattern in the input string
        match = re.search(pattern, input_string, re.DOTALL)

        if match:
            # Extract the Python code
            python_code = match.group(1)

            # Write the Python code to the specified file
            with open(file_path, 'w') as file:
                file.write(python_code)

            return file_path
        else:
            # Return None if no Python code block is found
            return None

    def execute_python_script(self, script_path: str) -> Any:
        """
        Executes a locally existing Python script.

        This function runs the specified Python script using the subprocess module.

        Args:
            script_path (str): The file path of the Python script to be executed.

        Returns:
            Any: The output of the executed script.
        """
        try:
            # Execute the Python script
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)

            # Return the output of the script
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            print(f"Error executing script: {e}")
            return None

    def run_mistral_agent(self):
        """
        Runs the Mistral agent chatbot interaction.
        """
        prompt = input("🧑 Human: ")

        while 'EXIT' not in prompt:
            response = self.generate_response(
                user_message=prompt
            )

            print("🤖 Bot: ", response)

            if '```python' in response:
                file_name = input("💻 What name do you want to save for this script? ")
                file_name = "_".join(file_name.split())
                self.isolate_and_save_python_code(
                    input_string=response,
                    file_path=f"{file_name}.py"
                )

                execution = input("💻 Do you want to execute this script? Enter 'Y' or 'N'. ")
                if execution == 'Y':
                    output = self.execute_python_script(f"{file_name}.py")
                    if output is not None:
                        print("Script executed successfully.")
                        print("🤖 Bot Output: ")
                        print(output)
                    else:
                        print("Failed to execute the script.")
            prompt = input("🧑 Human: ")

            print("NOTE: Enter 'EXIT' if you want to quit the program.")
