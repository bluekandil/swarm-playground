from swarm import Agent
import os

model = os.getenv("MODEL", "llama3.1")

def route_agent():
    return """ transfer to chinese agent or hindi agent """

talk_router_agent = Agent(
    name="Talker Agent",
    instructions=route_agent(),
    model=model, 
)

chinese_agent = Agent(
    name="Chinese Agent",
    instructions="speak only in Chinese.",    
    # functions=[talk],
    model=model, 
)

hindi_agent = Agent(
    name="Hindi Agent",
    instructions="Speak only in Hindi.",
    # functions=[talk],
    model=model, 
)

def transfer_back_to_talker_agent(**kwargs):    
    return talk_router_agent


def transfer_to_chinese_agent(**kwargs):  
    # print('------transfer_to_chinese_agent--------')  
    return chinese_agent

def transfer_to_hindi_agent(**kwargs):
    # print('------transfer_to_hindi_agent--------')  
    return hindi_agent


talk_router_agent.functions = [transfer_to_chinese_agent, transfer_to_hindi_agent]
chinese_agent.functions.append(transfer_back_to_talker_agent)
hindi_agent.functions.append(transfer_back_to_talker_agent)


