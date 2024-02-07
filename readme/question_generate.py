import openai
import os
import json

# Assuming you have set OPENAI_API_KEY in your environment variables

MODEL = "gpt-4-turbo-preview"

def generate_comprehension_question_and_answer(text):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a detailed comprehension question based on the following text: {text}"},
        ],
        temperature=0.5,
    )
    
    # Extract the generated question from the response
    responses = response['choices'][0]['message']['content']
    
    # Extract the answer and citation from the response
    answer_citation = response['choices'][0]['message']['content']
    
    # Splitting the response to separate the answer from the citation
    # This might need refinement based on the actual response format
    split_answer_citation = answer_citation.split('\n', 1)
    answer = split_answer_citation[0]
    citation = split_answer_citation[1] if len(split_answer_citation) > 1 else "No citation provided."
    
    return {
        'text': text,
        'question': question.strip(),
        'answer': answer.strip(),
        'citation': citation.strip()
    }

# Example usage
text = "This is an example text."
question_answer = generate_comprehension_question_and_answer(text)

# Print out the results
print("Generated Question and Answer")
print("============================")
print(f"Text: {question_answer['text']}")
print(f"Question: {question_answer['question']}")
print(f"Answer: {question_answer['answer']}")
print(f"Citation: {question_answer['citation']}")
