from __future__ import unicode_literals
import youtube_dl

video_info =[]
video_link = ["https://www.youtube.com/watch?v=Wv2rLZmbPMA", "https://www.youtube.com/watch?v=GIDoQsQyS0s"]

  

for i in video_link:

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        r = ydl.extract_info(i, False)
        video_info.append(r['title'])

print(video_info)

    
# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # ydl.download(['https://www.youtube.com/watch?v=pFSQh_5QE40&list=RDMMpFSQh_5QE40&start_radio=1'])
# i = input("what song do u ưant to hear?")
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     r = ydl.extract_info('https://www.youtube.com/watch?v=o_lN37OAJ9U', False)
#     print(r['title'])


