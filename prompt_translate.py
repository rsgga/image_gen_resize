import os
import sys
import openai
import json

def system_prompt():
    # It seems that in order for chatgpt to output json, content that outputs json is required.
    # ref. https://platform.openai.com/docs/guides/text-generation/json-mode
    return "You are a language translation model to output JSON."

def translation_prompt(source_text, source_language, target_language):
    return f"Translate the following text from {source_language} to {target_language}:\n\n{source_text}"

def translate_text(openai_model, source_text, source_language, target_language):
    # As of 12/12/2023, only the following models are available
    # - gpt-4-1106-preview
    # - gpt-3.5-turbo-1106
    # ref. https://platform.openai.com/docs/guides/text-generation/json-mode
    response = openai.chat.completions.create(
        model=openai_model,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt()},
            {"role": "user",   "content": translation_prompt(source_text, source_language, target_language)}
        ]
    )

    loaded_obj = json.loads(response.choices[0].message.content)

    values_list = list(loaded_obj.values())
    translated_text = values_list[0]

    return translated_text

def lambda_handler(event, context):
    body = json.loads(event['body'])

    openai_model = body['openai_model']
    prompt       = body['prompt']
    source_lang  = body['source_lang']
    target_lang  = body['target_lang']

    translated_text = translate_text(openai_model, prompt, source_lang, target_lang)

    print(translated_text)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: python {os.path.basename(__file__)} <openai_model> <prompt> <source_language_in_english> <target_language_in_english>")
        sys.exit(1)

    openai_model = sys.argv[1]
    prompt       = sys.argv[2]
    source_lang  = sys.argv[3]
    target_lang  = sys.argv[4]

    json_body = json.dumps({
        "openai_model": openai_model,
        "prompt":       prompt,
        "source_lang":  source_lang,
        "target_lang":  target_lang
    })

    lambda_handler({ "body": json_body }, {})
