from swarm import Swarm, Agent
from openai import OpenAI
import os


try:    
    # make sure to add OPENAI_API_KEY to your environment variables 
    # set OPENAI_API_KEY=sk-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx

    if 'OPENAI_API_KEY' not in os.environ:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")
    
    print('running swarm...')

    client = Swarm() 
    
    agent_a = Agent(
        name="Agent A",
        instructions="You are a helpful agent.",        
    )

    response = client.run(
        agent=agent_a,
        messages=[{"role": "user", "content": "Tell me something about a black hole?"}],
    )

    print(response.messages[-1]["content"])
        
except Exception as e:
    print(f"An error occurred while running the swarm: {e}")
