import numpy as np
import matplotlib.pyplot as plt

# กำหนดพิกัดหัวใจ
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# วาดหัวใจ
plt.figure(figsize=(6, 6), facecolor="Black")
plt.plot(x, y, 'r', linewidth=3)

# แสดงข้อความ
plt.text(0, -2, "", fontsize=18, color='red',
         fontweight='bold', ha='center', family='serif')

# ตั้งค่าการแสดงผล
plt.axis("off")
plt.show()