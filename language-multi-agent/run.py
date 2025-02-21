from swarm.repl import run_demo_loop
# from sql_agent import sql_router_agent
from talker import talk_router_agent

from swarm import Swarm, Agent
from openai import OpenAI


if __name__ == "__main__":
    
    ollama_client = OpenAI(
        base_url="http://localhost:11434/v1",        
        api_key="ollama"            
    )    
  
    def run_demo_loop(starting_agent, context_variables=None, stream=False, debug=False) -> None:
        client = Swarm(client=ollama_client)       

        messages = []
        agent = starting_agent
       
        while True:
            user_input = input("\033[90mUser\033[0m: ")
            messages.append({"role": "user", "content": user_input})

            response = client.run(
                agent=agent,
                messages=messages,
                context_variables=context_variables or {},
                stream=stream,
                debug=debug,
            )

            if stream:                
                response = print(response.messages[-1]["content"])
            else:                
                print(response.messages[-1]["content"])

            messages.extend(response.messages)
            agent = response.agent

    if __name__ == "__main__":
        run_demo_loop(talk_router_agent)

# user_message = "नमस्ते, आप कैसे हैं?"  # Change this to test different languages
# user_message = "Hello who are you?"  # Change this to test different languages
# user_message = "饺子食谱"  # Change this to test different languages