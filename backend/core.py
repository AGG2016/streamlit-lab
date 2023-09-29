from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import os
from typing import Any, List, Dict

def run_llm(context: str, chat_history: List[Dict[str, Any]] = []) -> Any:

    template = """
        given the following context {ticket_context} I want you to provide a summary including:
        1. Customer Key issues
        2. Recommendations
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["ticket_context"], template=template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(ticket_context=context)

    return result
