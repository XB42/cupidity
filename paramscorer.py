from pydantic import BaseModel
from openai import OpenAI

# Define the schema for input parameters
class GenderThesisParams(BaseModel):
    male: str
    female: str
    thesis: str

# Define the schema for the output
class GenderThesisScore(BaseModel):
    score: float

# Instantiate the OpenAI client
client = OpenAI()


# Define the function to calculate the score
def calculate_thesis_score(male: str, female: str, category:str, thesis: str):
    params = GenderThesisParams(male=male, female=female, category = category, thesis=thesis)
    
    # Use the OpenAI client to generate the completion
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": f"Evaluate the compatibility score between 1-100 based on this thesis: {thesis}"},
            {"role": "user", "content": f"The man is Male: {male} and the woman is Female: {female} based on strictly this metric: category: {category}"}
        ],
        response_format=GenderThesisScore,
    )


    # Extract the parsed response
    response = completion.choices[0].message.parsed
    
    return response
