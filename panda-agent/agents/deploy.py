import os
import sys
from pathlib import Path

# Add the agents directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from langchain_aws import ChatBedrock
from langchain.agents import create_agent
from fastapi import APIRouter
from tools import check_permission, create_environment

deploy_router = APIRouter(prefix="/deploy/v1", dependencies=[])

model_id = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")
aws_region = os.getenv("AWS_DEFAULT_REGION", "eu-central-1")
system_prompt = 'You are an assistant responsible for setting up and deploying environments based on the requester’s permissions.'

llm = ChatBedrock(
    model_id=model_id,
    region_name=aws_region,
    model_kwargs={
        "temperature": 0.7,
        "max_tokens": 2048,
    },
)

deploy_agent = create_agent(
    model=llm,
    tools=[create_environment, check_permission],
    system_prompt=system_prompt,
)

