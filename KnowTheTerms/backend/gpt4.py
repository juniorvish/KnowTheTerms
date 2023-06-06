import openai

def summarize_terms_of_service(terms_of_service_url):
    openai.api_key = "your_openai_api_key"

    user_message = f"Summarize the terms of service and provide a safety remark for the following URL: {terms_of_service_url}"
    prompt = f"User: {user_message}\nAI Developer:"

    message = []
    message.append({"role": "system", "content": "You are a friendly AI Developer"})
    message.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content

    summary, safety_remark = gpt_message.split("\n")[:2]

    return {
        "summary": summary.strip(),
        "safety_remark": safety_remark.strip()
    }