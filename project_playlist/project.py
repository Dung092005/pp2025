class video:
    def __init__(self,title,url):
        self.title = title
        self.url = url


def input_video():
    title = input("input title of vid : ")
    url = input("input a url of video: ")
    video = video(title,url)
    return video
def input_videos():
    videos = []
    number = int(input("input number of video you want: "))
    for i in range(number):
        vid = input_video()
        videos.append(vid)
    return videos
def print_video(video):   # chỉ in 1 video mà thôi 
    print("Video title is : " + video.title)
    print("Video url is: " + video.url)

def print_videos(videos):
    for i in videos:
        print_video(i)
def write_to_txt(videos):
    with open("data.txt","w") as file:
        total = len(videos)
        for i in range(total):
            file.write(str(total)+ "\n")
            file.write("title of video " + i + " : " + videos[i].title)
            file.write("url of video " + i + " : " + videos[i].url)



def main():
    videos = input_videos()
    write_to_txt(videos)
    print_videos(videos)

main()



