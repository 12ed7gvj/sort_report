import streamlit as st
import streamlit.components.v1 as components

# 讀取你的 HTML 檔案內容
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 用 Streamlit 將 HTML 渲染出來
components.html(html_content, height=600, scrolling=True)
