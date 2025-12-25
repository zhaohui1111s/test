from openai import OpenAI

# 初始化客户端（会自动从环境变量 OPENAI_API_KEY 里读取密钥）
client = OpenAI()

def call_llm(prompt: str) -> str:
    """
    调用 OpenAI 大模型，返回模型输出内容（只取第一条 message）。
    """
    response = client.chat.completions.create(
        model="gpt-5.1-mini",  # 模型名可换成 gpt-5.1, o3-mini 等
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,       # 控制随机性
        max_tokens=512,        # 限制输出长度
    )

    # 只取第一条完成结果
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = "简单介绍一下大语言模型是干什么的，用三句话。"
    answer = call_llm(user_input)
    print("模型输出：")
    print(answer)
