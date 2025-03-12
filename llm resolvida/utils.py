from typing import List, Tuple

def format_prompt(dados_texto: str, user_question: str) -> str:
  
    dados = dados_texto.strip() or "Nenhum dado disponível para exibição."
    return (
        "Você é um assistente que responde perguntas sobre um banco de dados.\n"
        "Aqui estão os últimos registros extraídos:\n\n"
        f"{dados}\n\n"
        "Com base nesses dados, responda à seguinte pergunta de forma clara e objetiva:\n"
        f"\"{user_question.strip()}\""
    )

def format_data_text(rows: List[Tuple]) -> str:
    """
    Converte uma lista de tuplas (linhas do banco de dados) em uma string formatada,
    onde cada linha é separada por uma quebra de linha e os campos são separados por vírgulas.
    
    Args:
        rows (List[Tuple]): Lista de tuplas representando as linhas do banco de dados.
        
    Returns:
        str: Dados formatados como string.
    """
    if not rows:
        return "Nenhum registro encontrado."
    return "\n".join([", ".join(map(str, row)) for row in rows])

def format_data_as_list(rows: List[Tuple]) -> str:
    """
    Converte uma lista de tuplas em uma string onde cada linha é apresentada como item
    de uma lista com marcador (bullet point).
    
    Args:
        rows (List[Tuple]): Lista de tuplas representando as linhas do banco de dados.
        
    Returns:
        str: Dados formatados em forma de lista.
    """
    if not rows:
        return "Nenhum registro encontrado."
    return "\n".join([f"- {', '.join(map(str, row))}" for row in rows])
