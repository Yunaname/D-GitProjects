import pandas as pd
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]  # Windows 用 SimHei
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 读取情感分析结果
df = pd.read_excel("comments_with_sentiment.xlsx")

# 1. 基础统计
total = len(df)
positive = len(df[df["情感"] == "正面"])
negative = len(df[df["情感"] == "负面"])
unknown = len(df[df["情感"] == "未知"])

# 2. 打印文本报告
print("=" * 60)
print("🍜 食品评论情感分析报告")
print("=" * 60)
print(f"📌 总评论数：{total} 条")
print(f"✅ 正面评论：{positive} 条，占比 {positive/total*100:.1f}%")
print(f"❌ 负面评论：{negative} 条，占比 {negative/total*100:.1f}%")
print(f"❓ 未知评论：{unknown} 条，占比 {unknown/total*100:.1f}%")
print("=" * 60)

# 3. 高频关键词统计
print("🔍 高频关键词统计：")
keyword_counts = df["关键词"].value_counts()
for kw, cnt in keyword_counts.items():
    if kw != "无":
        print(f"  - {kw}：{cnt} 次")
print("=" * 60)

# 4. 展示典型评论
print("💬 正面评论示例（前3条）：")
positive_samples = df[df["情感"] == "正面"]["评论内容"].head(3)
for i, com in enumerate(positive_samples, 1):
    print(f"  {i}. {com[:60]}..." if len(com) > 60 else f"  {i}. {com}")

print("\n💬 负面评论示例（前3条）：")
negative_samples = df[df["情感"] == "负面"]["评论内容"].head(3)
for i, com in enumerate(negative_samples, 1):
    print(f"  {i}. {com[:60]}..." if len(com) > 60 else f"  {i}. {com}")
print("=" * 60)

# 5. 生成情感分布饼图（可视化）
plt.figure(figsize=(6, 6))
labels = ["正面", "负面", "未知"]
sizes = [positive, negative, unknown]
colors = ["#66b3ff", "#ff9999", "#cccccc"]
explode = (0.05, 0.05, 0)  # 让饼图稍微分开一点

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90
)
plt.title("食品评论情感分布饼图")
plt.savefig("sentiment_pie_chart.png", dpi=300, bbox_inches="tight")
print("📊 情感分布饼图已保存为：sentiment_pie_chart.png")