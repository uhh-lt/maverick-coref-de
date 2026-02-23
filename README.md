<h1 align="center">
  German Maverick Coref
</h1>
<div align="center">


[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-green.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Pip Package](https://img.shields.io/badge/🐍%20Python%20package-blue)](https://pypi.org/project/maverick-coref-de/)
[![git](https://img.shields.io/badge/Git%20Repo%20-yellow.svg)](https://github.com/uhh-lt/maverick-coref-de)
</div>


# Python Package
The `maverick-coref-de` Python package provides an easy API to use German Maverick models, enabling efficient and accurate coreference resolution with few lines of code.

Install the library from [PyPI](https://pypi.org/project/maverick-coref-de/)

```bash
pip install maverick-coref-de
```
or from source 

```bash
git clone https://github.com/uhh-lt/maverick-coref-de.git
cd maverick-coref-de
pip install -e .
```

## Loading a Pretrained Model
Maverick models can be loaded using huggingface_id or local path:
```bash
from maverick_de import Maverick
model = Maverick(
  hf_name_or_path = "maverick_hf_name" | "maverick_ckpt_path", default = "fynnos/maverick-mes-de10"
  device = "cpu" | "cuda", default = "cuda:0"
)
```
## Inference

### Predict
You can use model.predict() to obtain coreference predictions.
For a sample input, the model will a dictionary containing:
- `tokens`, word tokenized version of the input.
- `clusters_token_offsets`, a list of clusters containing mentions' token offsets.
- `clusters_text_mentions`, a list of clusters containing mentions in plain text.


# Container

Run container, e.g. `docker run --rm --name maverick-de -p 8080:8080 --gpus '"device=0"' uhhlt/maverick-de:latest`

It supports two environment parameters: `MODEL_NAME` (to use another model than the default) and `DEVICE` (defaults to `cuda`, you can set `cpu` to try it without a GPU...)

Support `plain`, `tokenized`, and `tokenized+sentence split` (recommended) text:

```sh
curl -X 'POST' \
  'http://localhost:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tokens": 
      "Alice verkauft ihr altes Fahrrad. Sie braucht es nicht mehr."
}'
```

or

```sh
curl -X 'POST' \
  'http://localhost:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tokens": 
      ["Alice",  "verkauft", "ihr", "altes", "Fahrrad","." ,"Sie", "braucht", "es", "nicht", "mehr", "."]
}'
```

or

```sh
curl -X 'POST' \
  'http://localhost:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tokens": 
      [["Alice",  "verkauft", "ihr", "altes", "Fahrrad","."],[ "Sie", "braucht", "es", "nicht", "mehr", "."]]
}'
```

Result:
```json
{
  "tokens": [
    "Alice",
    "verkauft",
    "ihr",
    "altes",
    "Fahrrad",
    ".",
    "Sie",
    "braucht",
    "es",
    "nicht",
    "mehr",
    "."
  ],
  "clusters_token_offsets": [
    [
      [
        0,
        0
      ],
      [
        2,
        2
      ],
      [
        6,
        6
      ]
    ],
    [
      [
        2,
        4
      ],
      [
        8,
        8
      ]
    ]
  ],
  "clusters_char_offsets": null,
  "clusters_token_text": [
    [
      "Alice",
      "ihr",
      "Sie"
    ],
    [
      "ihr altes Fahrrad",
      "es"
    ]
  ],
  "clusters_char_text": null
}
```



# Training

Create a Python venv and install from source.

```bash
git clone https://github.com/uhh-lt/maverick-coref-de.git
cd maverick-coref-de
pip install -e .
```

* Obtain data in `.conll` format split into train/dev/test
* Run the `minimize.py` script from `data` for the correct dataset
* Adjust `conf/data/<your dataset>.yaml` for your dataset
* Adjust `conf/model/mes/<your encoder model>.yaml` to 
* Adjust `conf/root.yaml` to use the your dataset and your encoder model
* Run `CUDA_VISIBLE_DEVICES=X python maverick_de/train.py`


# Citation
If you use this software, please consider citing our paper published at KONVENS 2025:

```bibtex
@inproceedings{petersenfrey-etal-2025-efficient,
    title = "Efficient and effective coreference resolution for German",
    author = "Petersen-Frey, Fynn and Hatzel, Hans Ole and Biemann, Chris",
    booktitle = "Proceedings of the 21st Conference on Natural Language Processing (KONVENS 2025). Volume 1: Long and Short Papers",
    month = "9",
    year = "2025",
    address = "Hildesheim, Germany",
    publisher = "KONVENS 2025 Organizers"
}
```

The software in this repository is based on the on the work "Maverick: Efficient and Accurate Coreference Resolution Defying Recent Trends" by Giuliano Martinelli, Edoardo Barba, and Roberto Navigli published at [ACL 2024 main conference](https://aclanthology.org/2024.acl-long.722.pdf).
It uses their implementation forked from the [original repository](https://github.com/SapienzaNLP/maverick-coref) with some adaptions to a) make it compatible with German and b) try additional model variants.
For English, refer to the [original python package](https://pypi.org/project/maverick-coref/).


## License
The data and software are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).


