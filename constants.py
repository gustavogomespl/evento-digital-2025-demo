SYSTEM_PROMPT = """
Você é um assistente especialista em busca por termos de procedimentos médicos veterinários. 
Com base na lista de procedimentos sinônimos que você tem anexo nas tools, 
encontre os procedimentos que mais se relacionem com o termo procurado e retorne sua resposta no json schema especificado.
"""

def get_user_prompt(search_term: str) -> str:
    """
    Gera o prompt do usuário com o termo de busca específico.
    
    Args:
        search_term: O termo de busca para encontrar procedimentos relacionados
        
    Returns:
        O prompt formatado com o termo de busca
    """
    return f"""
            Quais são os procedimentos relacionados com o {search_term}?
            """

MODEL = "gpt-5-mini"

TEXT_FORMAT = {
      "type": "json_schema",
      "name": "search_term_with_procedures",
      "strict": True,
      "schema": {
        "type": "object",
        "properties": {
          "search_term": {
            "type": "string",
            "description": "The original term input by the user."
          },
          "procedures": {
            "type": "array",
            "description": "A list of possible procedures related to the search term.",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Name of the procedure."
                },
                "description": {
                  "type": "string",
                  "description": "Brief description of the procedure."
                }
              },
              "required": [
                "name",
                "description"
              ],
              "additionalProperties": False
            }
          }
        },
        "required": [
          "search_term",
          "procedures"
        ],
        "additionalProperties": False
      }
    }