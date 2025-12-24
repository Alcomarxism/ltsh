from openai import OpenAI,AsyncOpenAI
from agents import Agent, Runner,OpenAIChatCompletionsModel, function_tool

model=OpenAIChatCompletionsModel(
    model='gpt-oss:120b-cloud',
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1/",api_key='ollama'),
    
)
q=""
@function_tool
def save_question(question):
    global q
    q=question
    return "Sucsess"

@function_tool
def read_question(question):
    return q

agent_l = Agent(
    name="Agent_lenin",
    instructions="Сформулируй вопрос от имент Владимира Ленина, сохрани его при помощи save_question(question) и передай Николаю 2",
    tools=[read_question,save_question],
    model=model,
)

agent_n =Agent(
    name="Agent_Nikolay",
    instructions="Прочитай вопрос при помощи read_question и ответь от имени Николая 2",
    tools=[read_question,save_question],
    model=model
)

agent_l.handoffs=[agent_n]
agent_n.handoffs=[agent_l]


result = Runner.run_sync(agent_l, input="")
print(result.final_output)
print(result.last_agent.name)

print(q)