import sys
from ...translation.translator import translator_client

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def main():

    cli_args = sys.argv
    if len(cli_args) == 1:
        return print("The input text can not be empty", file=sys.stderr)

    from_lang = None
    to_lang = None
    text = cli_args[1]

    for index, item in enumerate(cli_args):
        if item == "--from-lang":
            from_lang = cli_args[index + 1]
        elif item == "--to-lang":
            to_lang = cli_args[index + 1]

    if not from_lang or not to_lang:
        return print(
            'Source language and target language can not be empty. please pass "--from-lang" and "--to--lang" cli args',
            file=sys.stderr,
        )

    print(f"---started translating from {from_lang} to {to_lang}---")
    print(translator_client.translate(text, from_lang, to_lang))


if __name__ == "__main__":
    main()
