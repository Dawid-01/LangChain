from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import os
from dotenv import load_dotenv

load_dotenv()



llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key="sua_api_key")

modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse} "
)

modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira os melhores restaurantes da região {cidade}"
)

modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

cadeia_cidade = LLMChain(Prompt=modelo_cidade, llm=llm)
cadeia_restaurantes = LLMChain(Prompt=modelo_restaurantes, llm=llm)
cadeia_cultural = LLMChain(Prompt=modelo_cultural, llm=llm)

cadeia = SimpleSequentialChain(chains=[cadeia_cidade, cadeia_restaurantes, cadeia_cultural] verbose=True)



resultado = cadeia.invoke("Praias")
print(resultado)

