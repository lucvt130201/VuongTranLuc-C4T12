from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s'])

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.extract_info(['https://www.youtube.com/watch?v=Wv2rLZmbPMA'])