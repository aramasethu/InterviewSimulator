# Conversation Simulator with LLM Model
This project uses llama2 to simulate text files of interviews between patients and doctors based on patient details provided in a .json format.

## Prerequisites

### Cloning the Repository
To get a copy of this project, you'll need to clone it to your local machine. Follow these steps:

Open your terminal or command prompt.
Navigate to the directory where you want to store the project.
Clone the repository by entering:
```
git clone [GitHub Repository URL]
```

Replace [GitHub Repository URL] with the actual URL of this repository.

### Libraries Installation
Before you begin, ensure you have the necessary Python libraries installed. They are specified in the requirements.txt file.

Install them by running:

```
pip install -r requirements.txt
```

### Data Setup
The repository contains .json file called patient_detail.json. It has patient details for two patients as an example. 
Make sure you have a .json file named patient_details.json containing patient details in the following format:

### API Token
The python code uses the (Replicate library) [https://replicate.com/blog/machine-learning-needs-better-tools] which enables
llama2 to be run on cloud without having to download the model in the local machine.  
You will need an API to run the python script. Sign up on Replicate to get the API token. When you run the script, you'll be prompted to enter the REPLICATE_API_TOKEN. Make sure you have it handy.

## Usage
Navigate to the project directory.
Run the main script:
```
python ConvSimulator.py
```
Enter the REPLICATE_API_TOKEN when prompted.
The script will read patient details from patient_details.json, simulate conversations, and save them to individual text files in a folder named Data.

## Methodology

### Environment Setup:

The script imports necessary libraries such as os, replicate, getpass, and json.
The user is prompted to provide the REPLICATE_API_TOKEN for authentication. This token is then set as an environment variable. 

### Definition of the ConversationSimulator Class:
This class serves as an interface to interact with llama2 through the Replicate.
The class is initialized with a model path.
There's a method named generate_response that takes a prompt with other parameters like temperature, top_p, etc. This method interacts with the Replicate platform to obtain a response from the LLM based on the provided prompt.

### Script Execution:
When the script is executed, it performs the following steps:
a. Initializes the ConversationSimulator with a specific model path.
b. Reads patient details from a patient_details.json file.
c. For each patient detail in the JSON file, it formats a prompt to simulate a conversation between a doctor and the patient using the provided details.
d. Using the ConversationSimulator, it generates a simulated conversation response.
e. Saves this generated response in a text file within the Data folder, naming the file based on the patient's name.
