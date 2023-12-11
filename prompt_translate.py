import sys
import openai
import json


def translate_text(source_text, source_language, target_language):
    """
    Translates the given text from the source language to the target language using OpenAI's translation model.

    Parameters:
    source_text (str): The text to be translated.
    source_language (str): The language of the source text.
    target_language (str): The language to translate the text into.

    Returns:
    str: The translated text.
    """

    translation_prompt = f"Translate the following text from {source_language} to {target_language}:\n\n{source_text}"

    # FIXME: I want to get model from the argument
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a language translation model to output JSON."},
            {"role": "user", "content": translation_prompt}
        ]
    )


    #print(response.choices[0].message.content)
    loaded_obj = json.loads(response.choices[0].message.content)

    values_list = list(loaded_obj.values())
    translated_text = values_list[0]

    return translated_text

def lambda_handler(event, context):
    body = json.loads(event['body'])

    prompt      = body['prompt']
    source_lang = body['source_lang']
    target_lang = body['target_lang']

    translated_text = translate_text(prompt, source_lang, target_lang)

    print(translated_text)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python prompt_translate_japanese_to_english.py <prompt> <source_language_in_english> <target_language_in_english>")
        sys.exit(1)

    prompt      = sys.argv[1]
    source_lang = sys.argv[2]
    target_lang = sys.argv[3]

    # Fixed value
    quality = "standard"

    json_body = json.dumps({
        "prompt":  prompt,
        "source_lang": source_lang,
        "target_lang": target_lang
    })

    lambda_handler({ "body": json_body }, {})

