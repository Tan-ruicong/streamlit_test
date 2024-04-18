import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import pandas as pd
import numpy as np

# 页面默认设置
st.set_page_config(page_title='最识你心', page_icon='heart.ico', layout="wide", initial_sidebar_state="auto", menu_items=None)

# st.title("⭐⭐⭐《最识你心》实时视频测试⭐⭐⭐",anchor="测试版")

# 使用HTML标签居中标题
st.markdown("<center><h1>⭐⭐⭐《最识你心》实时视频测试⭐⭐⭐</h1></center>", unsafe_allow_html=True)
st.write("一起来聊天吧")

# 视频处理
class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# cap = cv2.VideoCapture(0)
# stop = st.button("Stop")
# frame_placeholder = st.empty()


# 使用列进行布局
col1, col2 = st.columns([3,1])
with col1:
    st.header("🤡实时视频")
    webrtc_streamer(key="example")
    # while cap.isOpened() and not stop:
    #     ret, frame = cap.read()
    #     if not ret:
    #         st.write("Video capture has ended.")
    #         break
    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     frame_placeholder.image(frame, channels="RGB")
    #     if stop:
    #         break
    # cap.release()
    # st.write("这是第一列的内容")
    # 使用展开器创建隐藏内容
    with st.expander("点击展开更多回复建议"):
        st.write("聊个狗吧")

with col2:
    st.header("😃表情状态")

    # EMO = {'anger':{'概率':50},'disgust':{'概率':50},'fear':{'概率':50},'happiness':{'概率':50},'neutral':{'概率':50},'sadness':{'概率':50},'surprise':{'概率':50},'contempt':{'概率':50},'anxiety':{'概率':50},'helplessness':{'概率':50},'disappointment':{'概率':50}}
    # EMO = ["anger","disgust","fear","happiness","neutral","sadness","surprise","contempt","anxiety","helplessness","disappointment"]
    # 假设我们有一些数据
    data = pd.DataFrame(np.arange(10,21).reshape((11,1)),columns=['概率'],
    index=["anger","disgust","fear","happiness","neutral","sadness","surprise","contempt","anxiety","helplessness","disappointment"])
    # st.markdown("<style>.stDataFrame { width: 100%; }</style>", unsafe_allow_html=True)
    # 设置表格样式
    st.markdown(
        """
        <style>
        .stDataFrame {
            width: 100%;
            max-height: 1000px; /* 你可以根据需要设置一个最大高度 */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(data.style.highlight_max(axis=0))
    # st.write(data)
    style = st.selectbox("请选择回复风格", ['正式', '随意', '含蓄', '幽默'])
    st.write(f'已选择回复风格 {style}')
    number = st.slider("请选择回复长度", 1, 100, 50)


if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button("增加")
if increment:
    st.session_state.count += 1

st.write(f"计数器值：{st.session_state.count}")






# 链接
url = "http://47.236.96.234/"
# 在 st.write() 中添加文件下载链接
# st.write(f"点击[此处]({file_url})使用在线版")
# st.markdown(f'©copyright by ["Dontbrother"]({file_url})</h1></center>', unsafe_allow_html=True)
# 使用HTML标签来居中显示版权信息，并包含一个超链接
st.markdown(f'<center><h2>©copyright by <a href="{url}">Dontbrother</a></h2></center>', unsafe_allow_html=True)