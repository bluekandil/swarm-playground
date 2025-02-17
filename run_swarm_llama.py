from swarm import Swarm, Agent
from openai import OpenAI

ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",        
    api_key="ollama"            
)

try:    
    print('running swarm...')

    client = Swarm(client=ollama_client)
    
    agent_a = Agent(
        name="Agent A",
        instructions="You are a helpful agent.", 
        model="llama3.1",       
    )

    response = client.run(
        agent=agent_a,
        messages=[{"role": "user", "content": "Tell me something about a black hole?"}],
    )

    print(response.messages[-1]["content"])
        
except Exception as e:
    print(f"An error occurred while running the swarm: {e}")
