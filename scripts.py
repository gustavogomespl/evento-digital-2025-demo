def extract_text_from_response(response):
    """
    Extrai apenas o texto do output_text da resposta da API
    """
    try:
        if hasattr(response, 'output') and response.output:
            for output_item in response.output:
                if hasattr(output_item, 'content') and output_item.content:
                    for content_item in output_item.content:
                        if hasattr(content_item, 'text') and content_item.text:
                            return content_item.text
        return None
    except Exception as e:
        print(f"Erro ao extrair texto: {e}")
        return None
