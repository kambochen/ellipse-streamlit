import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("橢圓動態模擬圖形")

# 初始化前一個值（用於動畫）
if "a_prev" not in st.session_state:
    st.session_state.a_prev = 3
if "b_prev" not in st.session_state:
    st.session_state.b_prev = 2

# 使用者輸入
a = st.slider("a 值", 1, 5, 3)
b = st.slider("b 值", 1, 5, 2)

# 顯示公式
st.latex(fr"\frac{{x^2}}{{{a**2}}} + \frac{{y^2}}{{{b**2}}} = 1")

# 畫圖函式
def plot_ellipse(a_val, b_val):
    theta = np.linspace(0, 2 * np.pi, 300)
    x = a_val * np.cos(theta)
    y = b_val * np.sin(theta)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.grid(True)
    #ax.set_title(f"ellipse: x²/{a_val**2:.1f} + y²/{b_val**2:.1f} = 1")
    return fig

# 建立圖形動畫容器
plot_placeholder = st.empty()

# 動畫過渡 a, b
steps = 10
for i in range(1, steps + 1):
    a_step = st.session_state.a_prev + (a - st.session_state.a_prev) * i / steps
    b_step = st.session_state.b_prev + (b - st.session_state.b_prev) * i / steps
    fig = plot_ellipse(a_step, b_step)
    plot_placeholder.pyplot(fig)
    time.sleep(0.05)

# 儲存目前值以供下次使用
st.session_state.a_prev = a
st.session_state.b_prev = b
