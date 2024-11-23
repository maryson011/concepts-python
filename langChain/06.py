import os
from decouple import config # type: ignore

from langchain import hub # type: ignore
from langchain.agents import create_react_agent, AgentExecutor # type: ignore
from langchain.prompts import PromptTemplate # type: ignore
from langchain_community.utilities.sql_database import SQLDatabase # type: ignore
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit # type: ignore
from langchain_openai import ChatOpenAI # type: ignore


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-4o'
)

db = SQLDatabase.from_uri('sqlite:///ipca.db')

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True
)

prompt = '''
Use as ferramentas necessárias para responder perguntas relacionadas de IPCA ao usuario.
Responde tudo em português brasileiro.
Perguntas: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)

question = input('O que deseja saber sobre IPCA?')

output = agent_executor.invoke({
    'input': prompt_template.format(q=question)
})

print(output.get('output'))