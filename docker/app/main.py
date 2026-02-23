from os import environ
from typing import Annotated

from fastapi import Body, FastAPI

from maverick_de import Maverick


model_name = environ.get("MODEL_NAME", "fynnos/maverick-mes-de10")
device = environ.get("DEVICE", "cuda")
print(f"Loading German Maverick Coref with model '{model_name}' on device '{device}'... ", end='')
coref = Maverick(model_name, device)
print("done!")

app = FastAPI()


@app.post("/predict")
def predict(
    tokens: Annotated[list[list[str]] | list[str] | str, Body()],
    singletons: Annotated[bool, Body()] = False,
):
    if isinstance(tokens, str):
        import nltk
        nltk.download('punkt_tab')
    result = coref.predict(tokens, singletons)
    return result
