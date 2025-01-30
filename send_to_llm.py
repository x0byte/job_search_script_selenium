from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

def clean_text_with_mistral(input_file, output_file):
    llm = OllamaLLM(model="mistral")

    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Create a prompt for the Mistral model
    prompt = ChatPromptTemplate.from_template("""

    You are a data cleaning assistant. Your task is to process the following job listing and extract structured information:

    - Title
    - Advertiser (company name)
    - Work Type (e.g., Full-time, Part-time)
    - Cleaned Description (remove markdown, URLs, and irrelevant fluff)
    - Key Responsibilities (summarized as bullet points)
    - Required Skills (summarized as bullet points)

    Format the output as JSON. If a field is missing, use "N/A".

    """)

    # Send the text to the Mistral model for cleaning
    cleaned_text = llm(prompt.format(text=text))

    # Write the cleaned text to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

    print(f"Cleaned text saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = "seek_jobs_2025-01-30.txt"
    output_file = "cleaned_text.txt"
    clean_text_with_mistral(input_file, output_file)