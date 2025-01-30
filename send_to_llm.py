from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import json

def clean_text_with_mistral(input_file, output_file):
    llm = OllamaLLM(model="mistral")

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split text into individual jobs using the separator "-----"
    job_sections = text.split("\n" + "-" * 50 + "\n")

    # Define the prompt template (per job)
    prompt_template = """
    You are a data cleaning assistant. Process this job listing and extract:
    - Title
    - Advertiser (company name)
    - Work Type (e.g., Full-time)
    - Cleaned Description (remove fluff)
    - Key Responsibilities (bullet points)
    - Required Skills (bullet points)

    Format the output as JSON. Use "N/A" for missing fields.

    Job Listing:
    {job_text}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Process each job individually
    cleaned_jobs = []
    for job_text in job_sections:
        if not job_text.strip():  # Skip empty sections
            continue
            
        # Generate cleaned JSON for this job
        chain = prompt | llm
        cleaned = chain.invoke({"job_text": job_text})
        cleaned_jobs.append(cleaned)
        print(f"Processed job: {len(cleaned_jobs)}")

    # Save all jobs to a JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_jobs, f, indent=2)

    print(f"Cleaned data for {len(cleaned_jobs)} jobs saved to {output_file}")

if __name__ == "__main__":
    input_file = "seek_jobs_2025-01-30.txt"
    output_file = "cleaned_jobs.json"
    clean_text_with_mistral(input_file, output_file)