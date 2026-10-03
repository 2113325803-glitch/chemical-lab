import pytest
import requests
from storage import load_experiments

# 你的 FastAPI 服务地址（uvicorn 启动后就是它）
API_URL = "http://127.0.0.1:8000/add_experiment"


def test_api_add_and_verify():
    """测试：调用 API 添加化工数据，并断言数据库里确实存在"""
    # 1. 准备测试数据
    payload = {
        "exp_id": "API-CHEM-001",
        "temperature": 150.0,
        "pressure": 2.5,
        "catalyst": "API测试催化剂",
        "yield_rate": 88.8
    }

    # 2. 调用接口（发 POST 请求）
    response = requests.post(API_URL, json=payload)

    # 3. 断言接口返回成功
    assert response.status_code == 200
    assert response.json()["status"] == "success"

    # 4. 去数据库里“查账”（大厂测试开发核心技能）
    db_experiments = load_experiments()
    found = False
    for exp in db_experiments:
        if exp.exp_id == "API-CHEM-001":
            assert exp.temperature == 150.0
            assert exp.yield_rate == 88.8
            found = True
            break
    assert found, "数据库里没找到通过 API 插入的数据！"