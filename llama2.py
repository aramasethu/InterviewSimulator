import replicate


class ConversationSimulator:
    """
    Class for simulating conversations using the LLM model.
    """

    def __init__(self, model_path):
        """
        Initialize the ConversationSimulator with the given model path.

        Parameters:
        - model_path (str): The path to the LLM model.
        """
        self.model_path = model_path

    def generate_response(self, prompt, temperature=0.1, top_p=0.9, max_length=1280, repetition_penalty=1):
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
    # Prompts
    prompt_text = ("Given the following patient details, simulate a conversation between a doctor and a patient. Refer to the doctor as D and patient as P in the output. "
                   "Patient name: Bob. Patient age: 55. Patient condition: Bob has been experiencing acute hair loss since the last 6 weeks.")

    simulator = ConversationSimulator('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5')
    response = simulator.generate_response(prompt_text)
    print(response)