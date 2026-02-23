FROM pytorch/pytorch:2.8.0-cuda12.6-cudnn9-runtime

WORKDIR /code

RUN apt update \
    && apt-get install -y wget build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl \
    && pip install --break-system-packages --no-cache-dir ./flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl fastapi[standard] maverick-coref-de

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]