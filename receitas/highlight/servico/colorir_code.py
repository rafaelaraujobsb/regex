import re
from servico.arquivo import ler_arquivo, gravar_arquivo


def aplicar_cor(string: str, regex: str, cor: str, flags=None) -> str:
    """
        Aplica a cor informada na string html.

        Params:
            string: texto html.
            regex: pattern.
            flags: filtro para o regex, como: re.IGNORECASE.
            cor: cor para aplicar no texto html.

        Return:
            texto html com as modificações.
    """

    if flags:
        regex = re.compile(regex, eval(flags))
    else:
        regex = re.compile(regex)

    span = r'<span style="color:' + cor + r'"><b>\1</b></span>'

    return regex.sub(span, string)


def code():
    """
        Personaliza uma página html que contenha um código para as cores do python
    """

    regex = re.compile(r"(<code>.*<\/code>)", re.IGNORECASE|re.DOTALL)
    html = ler_arquivo('codigoFonte.html')

    string = regex.search(html).group(0)
    
    # Adicionar style no pre 
    string = regex.sub(r"<pre style='background-color:#1E1E1E'>\1</pre>", string)

    # Modificar cor string
    string = aplicar_cor(string, r'(\".*\")', "#C8703F", "re.IGNORECASE")
    
    # Modificar palavras reservadas 
    string = aplicar_cor(string, r"\b(if|else|import|return)\b", "#864B7E", "re.IGNORECASE")
    string = aplicar_cor(string, r"\b(print)\b", "#D6B85F", "re.IGNORECASE")
    
    # Modificar digitos
    string = aplicar_cor(string, r"\b(\d)\b", "#407A8E", "re.IGNORECASE")

    # Modificar (), >=, =
    string = aplicar_cor(string, r"(\(|\s=\s|\)|\s>=\s|:\s)", "#D4D4D4", "re.IGNORECASE")

    # Modificar comentários
    # (#\s*#.*\s*#|#\s.*|#!.*\n)
    # (#\*|#\s.*|#!.*)
    string = aplicar_cor(string, r"(#\s.*|#\s.*|#!.*)", "#4F9153", "re.IGNORECASE")

    # Modificar var
    # string = aplicar_cor(string, r"()", "#D4D4D4", "re.IGNORECASE")

    regex = re.compile(r"(<pre>.*<\/pre>)", re.IGNORECASE|re.DOTALL)
    string = regex.sub(string, html)

    gravar_arquivo(string, "codigoFinal.html")
