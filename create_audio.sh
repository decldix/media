#!/bin/bash
conda activate tortoise
python ~/Projects/tortoise-tts/tortoise/read.py --output_path . --preset fast --voice matthiasjonen --textfile audioscript.txt

python ~/Projects/tortoise-tts/tortoise/read.py --output_path . --preset fast --voice daniel --textfile audioscript.txt

python ~/Projects/tortoise-tts/tortoise/do_tts.py --preset fast --voice daniel --text "decldix is the central package for the decldix idea aimed at people who like the values of debian and know the advantages of declarative system configuration."
