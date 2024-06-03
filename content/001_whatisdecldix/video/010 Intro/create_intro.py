from moviepy.editor import *

# Sizes
VIDEO_4K= (3840, 2160)
VIDEO_HD = (1920, 1080)
VIDEO_DRAFT = (640, 360)

VIDEO_SIZE = VIDEO_DRAFT


FONT_HUGE = VIDEO_SIZE[1]/2
FONT_REALBIG = VIDEO_SIZE[1]/3
FONT_BIG = VIDEO_SIZE[1]/4
FONT_MEDIUM = VIDEO_SIZE[1]/5
FONT_SMALL = VIDEO_SIZE[1]/6
FONT_REALSMALL = VIDEO_SIZE[1]/7
FONT_TINY = VIDEO_SIZE[1]/8
FONT_REALTINY = VIDEO_SIZE[1]/9
FONT_MINI = VIDEO_SIZE[1]/10


TEXT_COLOR = "white"
BG_COLOR = "black"

DURATION = 2
FPS = 30


TEXT = "decldix"

clip = TextClip(TEXT, font="UbuntuNerdFont-Bold", fontsize = FONT_HUGE, color=TEXT_COLOR, size=VIDEO_SIZE)
clip = clip.set_position("center").set_duration(DURATION).set_fps(FPS)

clip.write_videofile("decldix.mp4")
