from typing import List, Dict, Optional, Union

def process_data(
    items: List[str],
    config: Dict[str, Union[int, str]],
    limit: Optional[int] = None
) -> Dict[str, float]:
    """类型提示提高代码可维护性"""
    # 代码逻辑
    return {"result": 42}

# 静态类型检查工具 (mypy) 可以检测类型错误
process_data(["a", "b", "c"], {"key": "value", "limit": 10})



