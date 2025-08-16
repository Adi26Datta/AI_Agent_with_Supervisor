from functions.config import llm, search_engine
from langgraph.prebuilt.chat_agent_executor import create_react_agent
from functions.tools import SearchEngine,get_vector_response,add_data_to_kg
from functions.prompts import Agent_prompt, search_agent_prompt, kg_agent_prompt,supervisor_agent_prompt
from langgraph_supervisor import create_supervisor

def Search_Agent():
    tools_list = [SearchEngine]
    Agent_search_engine = create_react_agent(
        llm,tools=tools_list,name="search_engine",prompt=search_agent_prompt)
    return Agent_search_engine

def KG_Agent():
    tools_list = [get_vector_response, add_data_to_kg]
    knowledge_graph_agent = create_react_agent(
        llm,tools=tools_list,name="knowledge_graph_agent",prompt= kg_agent_prompt)
    return knowledge_graph_agent

def Supervisor_Agent(search_agent, knowledgeGraph_agent,
                     **compile_kwargs) -> "CompiledWorkflow":
    supervisor = create_supervisor(
        agents=[search_agent, knowledgeGraph_agent],model=llm,
        prompt=supervisor_agent_prompt,output_mode="full_history",
        **compile_kwargs)
    return supervisor
