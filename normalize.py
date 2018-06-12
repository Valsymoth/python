import sys
from user_agents import parse

file = open("agents.txt","r")
for line in file:
    user_agent = parse(line)
    print user_agent
