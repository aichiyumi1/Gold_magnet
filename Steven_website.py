from PIL import Image
import streamlit as st
import random
#首页
balloon_snow_open = True
st.header("欢迎来到飞·网！")
st.subheader("在这里，你可以尽情浏览内容，或听听音乐，或下载一些使用小工具，或与其他人聊天，或尽情畅玩，一起嗨皮吧！")
st.text("""
工作室名字：飞·网
根据地用户：所有人
根据地用途：综合
现有模块：兴趣推荐、图片处理、词典、聊天室
原创模块：常用网站、游戏分站、音乐分站、代码分站、世界地图
原创模块一句话介绍：
    常用网站：新闻网呀、天气网呀、B站啊、某音啊...
    游戏分站：上传和下载一些游戏的文件，免费玩到一些付费游戏，不能商业化使用哦
    音乐分站：上传自己喜欢的音乐，也可以在线收听，不能商业化使用哦
    代码分站：上传自己喜欢的作品，下载一些通用的小工具，python制作的哦
    世界地图：找找你的家乡在哪
""")
if st.toggle('气球/雪花特效 开/关'):
    balloon_snow_open = True
else:
    balloon_snow_open = False
choice = st.slider('控制气球/雪花特效数量',1,50,1)
web = st.sidebar.radio('首页',['兴趣推荐','图片处理','词典','聊天室','常用网站','音乐分站','游戏分站','代码分站','世界地图'])
if balloon_snow_open:
    for i in range(int(choice)):
        if random.randint(1,2) == 1:
            st.snow()
        st.balloons()
def bgm():
    with open ('music/BGM.mp3','rb') as f:
        mymusic = f.read()
    st.audio(mymusic,format='audio/mp3',start_time=0)
    with open ('music/BGM2.wav','rb') as g:
        mymusic2 = g.read()
    st.audio(mymusic2,format='audio/wav',start_time=0)
    with open ('music/BGM3.mp3','rb') as h:
        mymusic3 = h.read()
    st.audio(mymusic3,format='audio/mp3',start_time=0)
bgm()
#侧边栏
def image_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def page1():
    st.write(":blue[我的游戏推荐]")
    game_tab1,game_tab2 = st.tabs(["Plants V.S. Zombies","raft"])
    with game_tab1:
        st.write("1.Plants V.S. Zombies（植物大战僵尸）")
        st.write("游戏内部界面：")
        st.image("game_share_image/主界面.png")
        st.image("game_share_image/菜单.png")
        st.image("game_share_image/1-1.png")
        st.image("game_share_image/白天.png")
        st.image("game_share_image/黑夜.png")
        st.image("game_share_image/泳池.png")
        st.image("game_share_image/迷雾.png")
        st.image("game_share_image/屋顶.png")
        st.image("game_share_image/僵王.png")
        st.write("不用过多介绍了，宝开横向塔防神作，玩法，元素都很经典，我就是玩着它长大的")
    with game_tab2:
        st.write("2.raft（木筏求生）")
        st.write("游戏内部界面：")
        st.image("game_share_image/界面.png")
        st.image("game_share_image/海.png")
        st.image("game_share_image/木筏.png")
        st.image("game_share_image/第三人称.png")
        st.image("game_share_image/背包.png")
        st.image("game_share_image/岛上.png")
        st.write("题材很新颖，3D场面也很不错，里面的元素也很丰富，可玩性很高，还有主线剧情，最重要的是可以联机，最近也是很火")
        st.success("好了，就安利到这里，游戏不在于多而在于精，大家可以去试玩一下哦")
def page2():
    st.write(":icecream:一个有一点简单的图片处理小程序:icecream:")
    uploaded_file = st.file_uploader("在这里上传图片",type=["png","jpeg","jpg","gif","bmp","webp"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img=Image.open(uploaded_file)
        img_tab1,img_tab2,img_tab3,img_tab4 = st.tabs(["原图","颜色失真1","颜色失真2","颜色失真3"])
        with img_tab1:
            st.image(img)
            st.success("图片加载成功！")
        with img_tab2:
            try:
                st.image(image_change(img,0,2,1))
                st.success("图片转换成功！")
            except:
                st.exception()
        with img_tab3:
            try:
                st.image(image_change(img,2,1,0))
                st.success("图片转换成功！")
            except:
                st.exception()
        with img_tab4:
            try:
                st.image(image_change(img,1,0,2))
                st.success("图片转换成功！")
            except:
                st.exception()
def page3():
    st.write(':blue[智能词典]')
    with open("data/words_space.txt",'r',encoding="utf-8") as f:
        word_list = f.read().split('\n')
        for i in range(len(word_list)):
            word_list[i]=word_list[i].split("#")
        words_dict = {}
        for i in word_list:
            words_dict[i[1]]=[int(i[0]),i[2]]#单词：[编号，意思]

        with open("data/check_out_times.txt","r",encoding='utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])#编号：次数
    word=st.text_input("在这里键入你要搜索的单词：")
    while word:
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            if times_dict[n] >= 50:
                st.write("该单词已经被查询了：",times_dict[n],"次，是个高频词汇呦！")
            else:
                st.write("该单词已经被查询了：",times_dict[n],"次")
            with open("data/check_out_times.txt","w",encoding="utf-8") as f:
                msg = ''
                for k, v in times_dict.items():
                    msg += str(k) + "#" + str(v) + '\n'
                msg = msg[:-1]
                f.write(msg)
            if word == 'python':
                st.code('''
                       #彩蛋！这个网站就是用python这门语言编写的呦！下面是源代码：
                       ''')
            if word == 'balloon' or word == 'birthday':
                st.balloons()
            if word == 'snow' or word == 'winter':
                st.snow()
            if word == 'win' or word == 'success':
                st.success("恭喜你又触发了一个彩蛋！")
            if word == 'Steven' or word == 'steven':
                st.success("召唤本作者！")
            break
        else:
            st.text("""检索错误。
                    可能是你输入的单词不合规范，也可能是你要查找的单词不在词典中。
                    如果是后者，请联系我们，我们会尽快加入缺失的内容""")
            break
def page4():
    st.write("聊天室")
    with open("data/leave_messages.txt",'r',encoding='utf-8') as f:
        msg_list = f.read().split('\n')
    for i in range(len(msg_list)):
        msg_list[i] = msg_list[i].split("#")
    for i in msg_list:
        if i[1] == '阿短':
            with st.chat_message('🌽'):
                st.write(i[1],"：",i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌈'):
                st.write(i[1],"：",i[2])
        elif i[1] == '制作组':
            with st.chat_message('🧑‍🔬'):
                st.header(i[1],"：",i[2])
        elif i[1] == '匿名用户1':
            with st.chat_message('🧨'):
                st.write(i[1],"：",i[2])
        elif i[1] == '匿名用户2':
            with st.chat_message('🧧'):
                st.write(i[1],"：",i[2])
        elif i[1] == '匿名用户3':
            with st.chat_message('🪄'):
                st.write(i[1],"：",i[2])
        name = st.selectbox("你的名字是：",['阿短','编程猫','制作组','匿名用户1','匿名用户2','匿名用户3'])
    new_msg = st.text_input("冒个泡吧：")
    if st.button('发送'):
        msg_list.append([str(int(msg_list[-1][0])+1),name,new_msg])
        with open("data/leave_messages.txt",'w',encoding='utf-8') as f:
            msg=''
            for i in msg_list:
                msg += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            msg = msg[:-1]
            f.write(msg)
def page5():
    st.write(":blue[常用网站]")
    st.write("你可以在这里找到平时常用的各大网站，如果在本站逛累了就可以来这里哦")
    col1,col2,col3,col4,col5,col6,col7 = st.columns(1,1,1,1,1,1,1)
    with col1:
        st.link_button('百度','https://www.baidu.com/')
        st.link_button('bilibili','https://www.bilibili.com/')
        st.link_button('中国天气网','https://www.xiaohongshu.com/')
        st.link_button('酷狗音乐','https://www.kugou.com/')
        st.link_button('python','https://www.python.org/')
    with col3:
        st.link_button('Bing','https://www.bing.com/')
        st.link_button('抖音','https://www.douyin.com/')
        st.link_button('中国科技网','http://www.stdaily.com/')
        st.link_button('网易云音乐','https://music.163.com/')
        st.link_button('Github','https://github.com/')
    with col5:  
        st.link_button('360','https://hao.360.com/')
        st.link_button('快手','https://www.kuaishou.com/')
        st.link_button('中国教育考试网','https://www.neea.edu.cn/')
        st.link_button('QQ音乐','https://y.qq.com/')
    with col7:
        st.link_button('Google','https://www.google.com/')
        st.link_button('小红书','https://www.xiaohongshu.com/')
        st.link_button('中国新闻网','https://www.chinanews.com.cn/')
        st.link_button('酷我音乐','http://www.kuwo.cn/')
def page6():
    pass
def page7():
    pass
def page8():
    pass
def page9():
    st.write(":sunglasses:超详细的世界地图~快来看看你的家乡在哪？:sunglasses:")
    st.map()
if web == '兴趣推荐':
    page1()
elif web == '图片处理':
    page2()
elif web == '词典':
    page3()
elif web == '聊天室':
    page4()
elif web == '常用网站':
    page5()
elif web == '音乐分站':
    page6()
elif web == '游戏分站':
    page7()
elif web == '代码分站':
    page8()
elif web == "世界地图":
    page9()
 