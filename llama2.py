# Imports
import os
import replicate
from getpass import getpass
import json

# Constants and Environment Configuration
REPLICATE_API_TOKEN = getpass()
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN


class ConversationSimulator:
    """
    Class for simulating conversations using the LLM model.
    """

    def __init__(self, model_path: str):
        """
        Initialize the ConversationSimulator with the given model path.

        Parameters:
        - model_path (str): The path to the LLM model.
        """
        self.model_path = model_path

    def generate_response(self, prompt: str, temperature: float = 0.1, top_p: float = 0.9, 
                           max_length: int = 1280, repetition_penalty: float = 1) -> str:
        """
        Generates a response from the LLM model based on the provided prompt and parameters.

        Parameters:
        - prompt (str): The input text to generate a response for.
        - temperature (float, optional): Sampling temperature. Default is 0.1.
        - top_p (float, optional): Top-p sampling. Default is 0.9.
        - max_length (int, optional): Maximum response length. Default is 1280.
        - repetition_penalty (float, optional): Penalty for repetitions. Default is 1.

        Returns:
        - str: The generated response from the model.
        """
        output = replicate.run(self.model_path,
                               input={"prompt": prompt,
                                      "temperature": temperature,
                                      "top_p": top_p,
                                      "max_length": max_length,
                                      "repetition_penalty": repetition_penalty})

        full_response = "".join(output)
        return full_response


if __name__ == '__main__':
    # read patient details from .json
    with open('patients_details.json', 'r') as file:
        all_patient_details = json.load(file)

    # Format the prompt using the loaded patient details
    for patient_details in all_patient_details:
        prompt_text = (
            f"Given the following patient details, simulate a conversation between a doctor and a patient. "
            f"Refer to the doctor as D and patient as P in the output. "
            f"Patient name: {patient_details['name']}. Patient age: {patient_details['age']}. "
            f"Patient condition: {patient_details['condition']}."
        )


    # Create simulator instance and generate response
    model_path = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    simulator = ConversationSimulator(model_path)
    response = simulator.generate_response(prompt_text)

# Save the simulated response to a distinct text file named after the patient
    filename = f"conversation_output_{patient_details['name']}.txt"
    with open(filename, 'w') as file:
        file.write(response)
    print(f"Conversation for {patient_details['name']} saved to {filename}")