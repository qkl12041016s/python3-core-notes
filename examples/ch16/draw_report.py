from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # 自动生成报表时使用无界面后端。
import matplotlib.pyplot as plt

days = [1, 2, 3]
counts = [2, 4, 3]
figure, axes = plt.subplots(
    1, 2, figsize=(7, 3), layout="constrained"
)
axes[0].plot(days, counts, marker="o", label="synced")
axes[0].set(xlabel="Day", ylabel="Files")
axes[0].legend()
axes[1].bar(["A", "B"], [5, 4])
axes[1].set(xlabel="Team", ylabel="Files")
figure.savefig("report.pdf")
plt.close(figure)  # 批量生成时及时释放画布。
print(Path("report.pdf").is_file())
