import yt_dlp
import time

begin = time.time()
def download_video(url, output_path=None):
    
    try:
        print("Baixando vídeo...")

        ydl_opts = {
            'format': 'best',  # Baixa o melhor formato disponível
            'outtmpl': output_path if output_path else '%(title)s.%(ext)s'  # Define o caminho de saída
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)
        
   
if __name__ == "__main__":
    # Exemplo de URL de um vídeo do YouTube
    video_url = 'Escreva a URL do video que quer baixar'
    download_video(video_url)
    
end = time.time()
execution = end - begin
print(execution)

    