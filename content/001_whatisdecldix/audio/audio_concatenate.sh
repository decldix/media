#!/usr/bin/env bash

# concatenate
for f in *.mp3; do echo "file '$f'" >> audio.txt; done

ffmpeg -f concat -i audio.txt -c copy audio.mp3

# correct metadata of audiofiles
for f in *.mp3 
do 
    ffmpeg -i $f -acodec copy "fixed_$f"
    rm $f
done

rename "s/^fixed_//" *

# get timestamps
for file in *.mp3
do
  duration=$(ffprobe "$file" 2>&1 | grep 'Duration' | cut -d',' -f1 | cut -d' ' -f4)
  echo "$duration $file" >> stats.txt
done 
