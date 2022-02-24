import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
from pathlib import Path
import re

curr_time = datetime.datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":

    headers = {
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'Cookie': 'nts_mail_user=yangding19thu@163.com:-1:1; mail_psc_fingerprint=a42671a74cda263857522b79cb43a250; _ntes_nuid=0b885646ad31db3ef8d8d5699bdbb06f; WM_TID=DL0pQ9vv+QFFRBUAVAZ/JMeLM8bS5GcL; ntes_kaola_ad=1; NMTID=00OHDYCN_2XPLmSfUqEnoYX19TvOfQAAAF0wNSuYw; WEVNSM=1.0.0; WNMCID=irmzpg.1622624403803.01.0; _ntes_nnid=0b885646ad31db3ef8d8d5699bdbb06f,1632309861429; UM_distinctid=17ce9d9ed37c4-0bcd671e8231a5-561a135a-144000-17ce9d9ed38542; __remember_me=true; vinfo_n_f_l_n3=a7927fa1ed14ecbd.1.1.1638777908887.1638777965180.1639062363576; __csrf=c9896375010f1d086ac48b15c8190d68; MUSIC_U=1a23dbe468f087b3858a5fadac66de7877d2eada99190702c4a5e70bad197918993166e004087dd3d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; _ntes_newsapp_install=false; NTES_P_UTID=u4Mwo5uzCIPuAMMukWOV2f78YUkmGC34|1644471972; NTES_SESS=Mxf0KUdN1FWaaDtEAFJh99rMgscTTLac12.YD.UZRnq6xaw1xYbLveZHlViHLTFNpt3g8WOzzjc0Rjsv3j0yrJB1ndxN7Ota0jhfjtOyufJXRkrbZ1wRG_pqcaiqIlscYkOCqp49yIg6fI_Z7STQn_ZEGYrvpKHwQccriZ7zwTI7hTVRq_H2nhK6tk6dQYTW.FEnrZWEmJf7sPJA1XA926tYlAHzlppvn; NTES_PASSPORT=.VpBkcrC_355wjybuu4.aAqlOSCfCEN9DF_on2dDzatgYtclYUOmhkLyv_aymw3XWa3pxjaOujqX..QJdr.6bwUTkJW8ESRZd2HXzAM97SN0Cjl3QqETaMXlbyOasgzIUshcddjXlx7qtls3dKYNmlq1KH8J.0dN6iltNv7hiCkPYMLUnd8JV4qQ4mfjkByT7; S_INFO=1644471972|0|3&80##|yangding19thu#yangding160115; P_INFO=yangding19thu@163.com|1644471972|1|mail163|00&99|jis&1644220938&mailmaster_ios#jis&320600#10#0#0|183698&0|youdaodict_client&mail163&mailmaster_ios|yangding19thu@163.com; MUSIC_EMAIL_U=c31d93881662a489ed67d0d8aed07aba5ad7bfae54577152194671dccbe0aa2320f04ec5aa727caed7697cc2f3cb641c22fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; playliststatus=visible; WM_NI=i/LCr0k3OQCM/isZOmBlhuQ9uuP0O1m+l0EmV3wbvVXc8332ZhZUmkPiG3Q8ZOgqv8Gg3Teh75yTX1ZTPgfKxhDWa2mm96dFaD0CmOWnS/aDsZ4nRZxkgWAwOJ2NAC3yQUM=; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7d2259b89f7d0e96594ef8ab6d44e839e8f85ae21a2ed819bd34e979ea898d92af0fea7c3b92aabf184a4f13ca9ed81b2c247edb7bdbbce6782b4a896d433b7aba0d1ce3baff5a4d1c86796edb983f55e9cbdf8d4b23a9ab896b6f06194b789d4d4349a91a992f53485b9fdb5e864f5ebb7b5db3b9a8ca088e541bcb88cb8e43aafb3f7d7e74ea39c00a4f04595b29dd0e450b186fc8fd152bcb5a9b8c47d8d96feafc449f1a79fb6d037e2a3; _iuqxldmzr_=32; JSESSIONID-WYYY=e+Y2FfgnmOclmnUg8/SbfV7faoa9Vr8bR8MAnrG13Ia\qBIsF3NWFp6Z5P6xjWiMvemGrIewuAHHfzYIWRGFr9AAtiHHn8ZIvgwtyruIaizD0foPS93v/5RVhFFFhBBZ8jD6T\YVq6hlp+1P/nq5Dx+Dr2Kc/0RO0DsBTe+S/yGPQ/FX:1644650734182',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50',
        'Accept': '*/*'
    }

    url = input("输入网页版歌单的链接\n")
    url = url.replace('/#/', '/')
    url = url.replace('/my/m/music/', '/')

    response = requests.get(url=url, headers=headers)
    html = response.content.decode(encoding="utf-8")

    soup = BeautifulSoup(html, 'lxml')
    results = soup.find('ul', {'class': 'f-hide'})
    results = results.find_all('a')

    print("将要下载的歌单为：{}\n".format(soup.find('title').text))

    print("包含如下歌曲：")
    cnt = 0
    for music in results:
        cnt += 1
        print("{}. {}".format(cnt, music.text))

    ch = input("\n是否开始下载?(y/n)")

    if ch == 'y' or ch == 'Y':
        path = './auto_download/'+ curr_time
        Path(path).mkdir(parents=True, exist_ok=True)

        cnt = 0
        for music in results:
            cnt += 1
            music_id = music['href'].split("=")[1]
            music_name = music.text

            music_name = re.sub('/|\*|"', ' ', music_name)
            music_name = music_name.replace(':', '：')
            music_name = music_name.replace('?', '？')
            music_name = music_name.replace('<', '《')
            music_name = music_name.replace('>', '》')
            music_name = music_name.replace('|', ' ')
            music_name = music_name.replace('\\', ' ')


            # music_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_id)

            music_url = "https://link.hhtjim.com/163/{}.mp3".format(music_id)

            print("进度{}/{}, 正在下载 <{}>".format(cnt, len(results), music_name))

            try:
                urllib.request.urlretrieve(music_url, path + '/' + music_name + '.mp3')
            except urllib.error.HTTPError:
                print("资源已失效，跳过下载")


        print("下载完成")