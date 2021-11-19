import youtube_dl # Kütüphaneyi yüklemek için terminale pip install youtube_dl yazınız.

video_linki = input("Youtube linkini yapıştırınız: ")
video_ismi = youtube_dl.YoutubeDL().extract_info(url = video_linki, download = False)

dosya_ismi = f"{video_ismi['title']}.mp3"

ayarlar = {
    'format':'bestaudio/best', 'keepvideo':False, 'outtmpl':dosya_ismi,
}

with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_ismi['webpage_url']])

    print(f"İndirme işlemi başarılı. {dosya_ismi}")