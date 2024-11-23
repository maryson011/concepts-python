from langchain_community.tools import DuckDuckGoSearchRun # type: ignore

ddg_search = DuckDuckGoSearchRun()

search_result = ddg_search.run('Quem foi Alan Turing?')
print(search_result)

print('='*50)

from langchain_community.tools import WikipediaQueryRun # type: ignore
from langchain_community.utilities import WikipediaAPIWrapper # type: ignore

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        lang='pt'
    )
)

wikipedia_results = wikipedia.run('Quem foi Alan Turing?')
print(wikipedia_results)