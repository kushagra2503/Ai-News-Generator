from crewai import Agent,LLM
from tools import tool
import os
from litellm import completion

from dotenv import load_dotenv
load_dotenv()

#Call the gemini model

llm=LLM(
    model='gemini/gemini-2.0-flash',
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GEMINI_API_KEY")
    
)

##Creatinga senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation eager to explore and share knowlegde that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## Creating a Writer agent with custom tools responsible in writing news blog
news_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)