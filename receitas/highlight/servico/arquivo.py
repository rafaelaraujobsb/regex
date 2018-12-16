import sys

DIR = sys.path[0]
ORG = DIR+"/templates/originais"
ALT = DIR+"/templates/alterados"

def ler_arquivo(name_file: str) -> str:
    """
        Ler arquivo que está na pasta original

        Params:
            name_file: nome do arquivo que vai ser lido.

        Return:
            string: str
    """

    with open(f"{ORG}/{name_file}", "r") as f:
        string = f.read()

    return string


def gravar_arquivo(string: str, name_file: str) -> None:
    """
        Gravar string em aquivo.

        Params:
            string: texto que será gravado.
            name_file: nome do arquivo.

        Return:
            None
    """
    with open(f"{ALT}/{name_file}", "w") as f:
        f.write(string)
