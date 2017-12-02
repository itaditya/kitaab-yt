import requests

OK = 200


def transcribe_video(name):
    url=''
    link = url+name+'.tsv'
    print(link)
    response = requests.get(url)

    return response.status_code, response.content


def search_keywords(name, keyword):

    timestamps = list()

    if not keyword or not youtube_url:
        return timestamps

    status_code, content = transcribe_video(youtube_url)

    if not content:
        print("connect unavailable")
        return timestamps

    if status_code == OK:
        a=[]
        text=list()
        with open('lhack.tsv') as f:
            for l in f:
                n=l.strip().split("\t")
                print(n[1])
                try:
                    if n[1]=='[Music]':
                        continue
                    else:
                        a.append(n[0])
                        text.append(n[1])
                except:
                    pass


        for i in range(len(text)):
            if keyword in text[i]:
                timestamps.append(a[i])
            


    return timestamps
