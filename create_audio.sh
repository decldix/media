#!/bin/bash
conda activate tortoise

#presets 
# ultra_fast for test
# high_quality for end result
python ~/Projects/tortoise-tts/tortoise/do_tts.py --preset ultra_fast --voice daniel --text "decldix is the central package for the decldix idea aimed at people who like the values of debian and know the advantages of declarative system configuration."
