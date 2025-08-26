from openai import OpenAI
import constants
import argparse
import sys
import os
import json
from scripts import extract_text_from_response

MODEL = constants.MODEL
SYSTEM_PROMPT = constants.SYSTEM_PROMPT
TEXT_FORMAT = constants.TEXT_FORMAT

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_BQA")

def main():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser(description='Buscar procedimentos veterinários relacionados a um termo')
    parser.add_argument('search_term', type=str, help='Termo de busca para procedimentos veterinários')
    parser.add_argument('--text-only', '-t', action='store_true', help='Mostrar apenas o texto da resposta')
    
    # Parse dos argumentos
    args = parser.parse_args()
    search_term = args.search_term
    
    print(f"🔍 Buscando procedimentos relacionados a: '{search_term}'")
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.responses.create(
          model=MODEL,
          input=[
            {
              "role": "developer",
              "content": [
                {
                  "type": "input_text",
                  "text": SYSTEM_PROMPT
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "input_text",
                  "text": constants.get_user_prompt(search_term)
                }
              ]
            }
          ],
          text={
            "format": TEXT_FORMAT,
            "verbosity": "medium"
          },
          reasoning={
            "effort": "medium",
            "summary": "auto"
          },
          tools=[
            {
              "type": "file_search",
              "vector_store_ids": [
                "vs_68a8a5f9388c81919e399932e0dc0218"
              ]
            }
          ],
          store=True
        )
        
        print("✅ Resposta recebida com sucesso!")
        
        if args.text_only:
            # Mostrar apenas o texto do output_text
            text_data = extract_text_from_response(response)
            if text_data:
                print("📋 Texto da resposta:")
                print(text_data)
            else:
                print("❌ Não foi possível extrair texto da resposta")
        else:
            # Mostrar apenas o final_output
            print("📋 Resposta da API:", response)
            
    except Exception as e:
        print(f"❌ Erro ao processar a requisição: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()