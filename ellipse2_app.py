
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("動態橢圓繪圖")
#設定滑桿
a = st.slider("a 值", 1, 5, 3)
b = st.slider("b 值", 1, 5, 2)
st.latex(fr"\frac{{x^2}}{{{a**2}}} + \frac{{y^2}}{{{b**2}}} = 1")
theta = np.linspace(0, 2 * np.pi, 300)
x = a * np.cos(theta)
y = b * np.sin(theta)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.grid(True)
ax.set_title(f"ellipse: (x^2)/{a**2} + (y^2)/{b**2} = 1")
st.pyplot(fig)