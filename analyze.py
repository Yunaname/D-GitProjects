import pandas as pd
import requests
import time

# ========== 替换成你的智谱清言 API Key ==========
API_KEY = "8e6357bd42aa45edb91acd28f963bf3a.2QpPbsSW7T1hK836"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
# =================================================

def analyze_sentiment(comment_text):
    """调用智谱清言 API 判断评论情感：正面/负面/未知"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "glm-4-flash",  # 免费模型，速度快
        "messages": [
            {"role": "system", "content": "你是食品评论情感分析专家，只返回「正面」「负面」「未知」三个结果之一，不要其他内容"},
            {"role": "user", "content": f"判断这条食品评论的情感：{comment_text}"}
        ],
        "temperature": 0
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code != 200:
            print(f"API 请求失败，状态码：{response.status_code}，响应：{response.text}")
            return "未知"
        
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            sentiment = result["choices"][0]["message"]["content"].strip()
        elif "error" in result:
            print(f"API 返回错误：{result['error']}")
            return "未知"
        else:
            print(f"未知返回结构：{result}")
            return "未知"
            
        if "正面" in sentiment:
            return "正面"
        elif "负面" in sentiment:
            return "负面"
        else:
            return "未知"
    except Exception as e:
        print(f"分析出错：{e}")
        return "未知"

def extract_keyword(comment):
    keywords = ["好吃", "难吃", "新鲜", "变质", "包装", "物流"]
    for kw in keywords:
        if kw in comment:
            return kw
    return "无"

# 读取评论
df = pd.read_excel("comments.xlsx")

# 分析情感
print("开始分析...")
df["情感"] = df["评论内容"].apply(analyze_sentiment)
time.sleep(1)  # 避免触发频率限制

# 提取关键词
df["关键词"] = df["评论内容"].apply(extract_keyword)

# 保存结果
df.to_excel("comments_with_sentiment.xlsx", index=False)
print("✅ 分析完成！结果保存在 comments_with_sentiment.xlsx")