# app/Dockerfile

FROM python:3.11-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/AGG2016/streamlit-lab.git .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENV OPENAI_API_KEY=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

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
