# 机器学习标准完整流程（可直接保存为py文件）
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1.加载数据
data = load_iris()
X = data.data   # 特征
y = data.target # 标签

# 2.划分训练集&测试集（固定随机种子，结果永远不变）
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3.模型：实例化 → 训练 → 预测
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)  # 训练模型
y_pred = model.predict(X_test) # 预测

# 4.计算准确率并输出
acc = accuracy_score(y_test, y_pred)
print(f"✅ 测试集准确率: {acc:.2f}")

# 5.简单可视化
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred)
plt.title("测试集预测结果")
plt.show()