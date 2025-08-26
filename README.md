# Buscador de Procedimentos Veterinários

Este script permite buscar procedimentos veterinários relacionados a um termo específico usando a API da OpenAI.

## Como usar

### Uso básico
```bash
python openai-api-demo.py "vacinação"
```

### Mostrar apenas o texto da resposta (recomendado)
```bash
python openai-api-demo.py "vacinação" --text-only
# ou
python openai-api-demo.py "vacinação" -t
```

### Ver ajuda
```bash
python openai-api-demo.py --help
```

## Exemplos de uso

```bash
# Buscar procedimentos relacionados a vacinação (apenas texto)
python openai-api-demo.py "vacinação" --text-only

# Buscar procedimentos relacionados a cirurgia
python openai-api-demo.py "cirurgia" -t

# Buscar procedimentos relacionados a tratamento (apenas texto)
python openai-api-demo.py "tratamento" -t
```

## Exemplo de saída

```
📋 Texto da resposta:
{"search_term":"vacinação","procedures":[{"name":"Vacina V10","description":"Vacina polivalente para cães contra 10 doenças"},{"name":"Vacina V4","description":"Vacina polivalente para gatos contra 4 doenças"}]}
```

## Estrutura do projeto

- `constants.py`: Contém as constantes e configurações do sistema
- `openai-api-demo.py`: Script principal que recebe o termo de busca como argumento
- `scripts.py`: Funções utilitárias para processamento de respostas da API

## Requisitos

- Python 3.7+
- Biblioteca `openai`
- Chave de API da OpenAI configurada no ambiente

## Configuração

Certifique-se de ter a variável de ambiente `OPENAI_API_KEY_BQA` configurada:

```bash
export OPENAI_API_KEY_BQA="sua-chave-api-aqui"
```


