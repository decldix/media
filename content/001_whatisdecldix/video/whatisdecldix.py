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
BG_COLOR = (0,0,0)

DURATION = 16
FPS = 30


bg = ColorClip(size=VIDEO_SIZE, color=BG_COLOR)

# Explain decldix
audio_intro = AudioFileClip("./audio/01_intro.mp3")
decldix = TextClip("decldix", font="UbuntuNerdFont-Bold", fontsize = FONT_HUGE, color=TEXT_COLOR, size=VIDEO_SIZE)
decldix = decldix.set_position("center")

duration = audio_intro.duration

intro = decldix.set_audio(audio_intro).set_duration(duration)

intro.write_videofile("./video/intro.mp4",fps=FPS)


# What is decldix
audio_decldix = AudioFileClip("./audio/02_What_is_decldix.mp3")
duration = audio_decldix.duration

bg = ColorClip(size=VIDEO_SIZE, color=BG_COLOR)
bg = bg.set_duration(duration).set_fps(FPS)

decldix = TextClip("decldix", font="UbuntuNerdFont-Bold", fontsize = FONT_SMALL, color=TEXT_COLOR)
decldix = decldix.set_position(("center",0-VIDEO_SIZE[1]/25)).set_duration(duration)

declarative = TextClip("decl arative", font="UbuntuNerdFont-Bold", fontsize = FONT_TINY, color=TEXT_COLOR)
declarative = declarative.set_position(("center",decldix.h-VIDEO_SIZE[1]/25)).set_start(4).set_duration(duration)

debian = TextClip("d ebian", font="UbuntuNerdFont-Bold", fontsize = FONT_TINY, color=TEXT_COLOR)
debian = debian.set_position(("center",decldix.h+declarative.h-VIDEO_SIZE[1]/25)).set_start(4.3).set_duration(duration)

nix = TextClip("n ix", font="UbuntuNerdFont-Bold", fontsize = FONT_TINY, color=TEXT_COLOR)
nix = nix.set_position(("center",decldix.h+declarative.h+debian.h-VIDEO_SIZE[1]/25)).set_start(4.5).set_duration(duration)

whatisdecldix = CompositeVideoClip([bg, decldix, declarative, debian, nix]).set_audio(audio_decldix).set_duration(duration)


whatisdecldix.write_videofile("./video/whatisdecldixdecldix.mp4", fps=FPS)
