"""用于验证 wheel 安装的最小包。"""

def label(name):
    # 安装后用这个函数核对导入路径。
    return f"笔记：{name}"
