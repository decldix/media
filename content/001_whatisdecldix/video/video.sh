# png with mp3 --> mp4
ffmpeg -loop 1 -i *.png -i *.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest out.mp4

ffmpeg  \
-vsync 0 \
-i 1.mp4 \
-i 2.mp4 \
-filter_complex "[0]settb=AVTB[0:v]; \
[1]settb=AVTB[1:v]; \
[0]aresample=async=1:first_pts=0,apad,atrim=0:99[0:a]; \
[1]aresample=async=1:first_pts=0,apad,atrim=0:98[1:a]; \
[0:v][1:v]xfade=transition=fade:duration=1:offset=98,format=yuv420p[video]; \
[0:a][1:a]acrossfade=d=1:c1=tri:c2=tri[audio]" \
-map "[audio]" \
-ar 48000 \
-b:a 96k \
-map "[video]" \
-rc vbr \
-cq 30 \
-qmin 30 \
-qmax 30 \
out.mp4
