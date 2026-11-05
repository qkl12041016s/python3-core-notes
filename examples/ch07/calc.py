def add(left, right):
    # 复用逻辑位于模块顶层，启动动作位于入口守卫。
    return left + right


if __name__ == "__main__":
    print("从 calc.py 入口运行", add(2, 3))
