# 机器学习标准流程 + 自动保存图片（固定路径版，直接复制）
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import os

# ====================== 固定配置 ======================
# 1. 图片保存路径（绝对路径，直接写死）
save_path = r"D:\python-code\figures"
# 2. 全局中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# ======================================================

# 1. 加载数据
data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. 单模型KNN测试
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ 准确率: {acc:.2f}")

# 3. 绘图 + 自动保存（直接保存到D盘figures文件夹）
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred, cmap='viridis', edgecolor='k')
plt.title("测试集预测结果")
plt.xlabel("花萼长度(cm)")
plt.ylabel("花萼宽度(cm)")

# 核心保存代码（直接复制这段就能用）
plt.savefig(f"{save_path}\\test_iris_pred.png", dpi=300, bbox_inches='tight')
plt.close()
print(f"📸 图片已保存至：{save_path}")