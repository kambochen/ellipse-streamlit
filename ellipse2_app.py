import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# 設定整體頁面寬度樣式（讓內容不會過寬）
st.set_page_config(layout="centered")

# 兩欄佈局：標題 + LaTeX 公式
col1, col2 = st.columns([2, 3])
with col1:
    st.subheader("動畫橢圓圖形")
with col2:
    # 先給個預設 a, b 值顯示公式（在 slider 下會再更新）
    st.latex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1")

# 初始化 session state
if "a_prev" not in st.session_state:
    st.session_state.a_prev = 3
if "b_prev" not in st.session_state:
    st.session_state.b_prev = 2

# 水平滑桿佈局（同一行）
col_a, col_b = st.columns(2)
with col_a:
    a = st.slider("a 值", 1, 5, 3)
with col_b:
    b = st.slider("b 值", 1, 5, 2)

# 更新公式（帶入數值）
#st.latex(fr"\frac{{x^2}}{{{a**2}}} + \frac{{y^2}}{{{b**2}}} = 1")

# 畫圖函式（小尺寸）
def plot_ellipse(a_val, b_val):
    theta = np.linspace(0, 2 * np.pi, 300)
    x = a_val * np.cos(theta)
    y = b_val * np.sin(theta)
    fig, ax = plt.subplots(figsize=(1.6, 1.2))  # 更小尺寸
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.grid(True)
    ax.tick_params(axis='both', labelsize=6)
    #ax.set_title(f"x²/{a_val**2:.1f} + y²/{b_val**2:.1f} = 1", fontsize=10)
    return fig

# 建立圖形動畫容器
plot_placeholder = st.empty()

# 動畫效果
steps = 10
for i in range(1, steps + 1):
    a_step = st.session_state.a_prev + (a - st.session_state.a_prev) * i / steps
    b_step = st.session_state.b_prev + (b - st.session_state.b_prev) * i / steps
    fig = plot_ellipse(a_step, b_step)
    plot_placeholder.pyplot(fig)
    time.sleep(0.1)

# 儲存目前值
st.session_state.a_prev = a
st.session_state.b_prev = b
