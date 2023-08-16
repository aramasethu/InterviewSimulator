# Conversation Simulator with LLM Model
This project uses llama2 to simulate text files of interviews between patients and doctors based on patient details provided in a .json format.

## Prerequisites
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
The python code uses the [Replicate library] (https://replicate.com/blog/machine-learning-needs-better-tools) which enables
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
