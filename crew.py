from crewai import Crew, Process
from agents import news_researcher,news_writer
from tasks import research_task,write_task

#Froming the tech-focused crew with some enhanced confuguartions
crew= Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential #Optional : Sequential task execution is default
)

## Starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'Ai in healthcare'})
print(result)