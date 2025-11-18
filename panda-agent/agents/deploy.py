import os
from langchain_aws import ChatBedrock
from langgraph.prebuilt import create_react_agent
from fastapi import APIRouter

deploy_router = APIRouter(prefix="/deploy/v1", dependencies=[])

# 从环境变量获取 Bedrock 配置
model_id = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")
aws_region = os.getenv("AWS_DEFAULT_REGION", "eu-central-1")

# 创建 Bedrock LLM
llm = ChatBedrock(
    model_id=model_id,
    region_name=aws_region,
    model_kwargs={
        "temperature": 0.7,
        "max_tokens": 2048,
    },
)

# 创建 LangGraph agent
deploy_agent = create_react_agent(
    model=llm,
    tools=[],  # 在这里添加你的工具
)
