FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "trading-bot", "/bin/bash", "-c"]

COPY . .

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "trading-bot", "python", "Main.py"]
