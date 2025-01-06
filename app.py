from fastapi import FastAPI
import requests
from deep_translator import GoogleTranslator
from json import JSONResponse

app = FastAPI()


@app.get("/kanye-west")
def frases_kanye():
    url = ('https://api.kanye.rest/')


    
    try:
        # Faz a requisição à API do kanye
        response = requests.get(url)
        
        # Exceção para códigos de erro HTTP
        response.raise_for_status()

        dados = response.json()

        # Extrai a citação do JSON retornado
        aspas = dados['quote']

        # Traduz a citação para português
        traduzido = GoogleTranslator(source='en', target='pt').translate(aspas)

        return JSONResponse(content={'Original': aspas, 'Tradução': traduzido},
                        headers={'Access-Control-Allow-Origin': '*'})
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro na requisição: {str(e)}"}

    except Exception as e:
        print(f'Algo deu errado com a requisição. Código: {response.status_code} - Erro: {e}')
