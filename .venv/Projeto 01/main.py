import openai


openai.api_key = "sua key"


numero_de_dias = 7
numero_de_criancas = 1
atividade = "Praia"

# prompt
prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para o Guarujá, para uma família com {numero_de_criancas} criança(s), que gostam de {atividade}."
print(prompt)

try:
    
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt},
        ]
    )

 
    roteiro_viagem = resposta['choices'][0]['message']['content']
    print("\nRoteiro de Viagem Gerado:")
    print(roteiro_viagem)

except Exception as e:
    print(f"Erro ao se comunicar com a API da OpenAI: {e}")
