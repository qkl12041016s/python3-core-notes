<div align="center">

# Python 3 核心编程与实战笔记

基于 PyCharm 与现代工程化实践 · 雪落长安无声

[![XeLaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-3776AB)](https://www.latex-project.org/)
[![书稿许可](https://img.shields.io/badge/书稿-CC_BY--NC_4.0-FFD43B)](LICENSE)
[![示例代码许可](https://img.shields.io/badge/代码-MIT-3776AB)](LICENSE)

[下载最新版 PDF](../../releases/latest) · [查看示例运行方法](RUN_EXAMPLES.md) · [自行编译](#自行编译)

</div>

## 项目简介

这份中文笔记适合正在学 Python，或准备把零散脚本整理成可测试项目的读者。六篇 17 章从解释器、容器、函数与类讲起，逐步进入测试、文件与数据、并发、HTTP、数据库、GUI 和交付。

- **图文与代码同页。** 蓝黄配色、双栏目录、章节导图、编号代码块和「核心直觉」提示框共同组织阅读路径。
- **示例可以动手复现。** 从输入、执行过程与输出对照入手，再用断点、回溯和小样本验证边界。
- **四阶段项目练习。** 通讯录、批量下载、自动报表，以及 PyQt 资料管理器或 FastAPI 本地服务。
- **遇到报错有地方查。** 符号表收录 59 项，排错附录收录 31 条记录，附有错误入口和修复版。

## 自行编译

完整项目从本目录运行 XeLaTeX 两次。图片在 figures/ 中，保持目录结构一起解压。

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

python3-notes.tex 是导言区和全书正文合并后的完整源码，包含内置 TikZ 简图。要复现交付 PDF 的完整矢量插图，请在包含 figures/ 的项目目录编译。

## 项目结构

- main.tex 管篇章顺序。
- preamble.tex 管排版、另页且置顶的篇章标题和提示框。
- frontmatter/ 放封面、路线图、前言、致谢、使用说明和符号表。
- chapters/ 放第 1 至 17 章，projects/ 放项目文字与源码。
- backmatter/appendices.tex 放前三项附录，资料对照表已并入附录 A。
- figures/ 放矢量 PDF 与预览 PNG，tools/create_figures.py 可重新生成。
- examples/appendixA 与 appendixB 放环境诊断、调试例子。
- examples/appendixC 放修复脚本和故意失败的 .py.txt 入口。

## 验证报错记录

安装 requests 后运行以下命令。失败入口单独捕获并核对异常类型，修复版核对输出。

```sh
python tools/verify_error_cases.py
```

章节与四阶段项目的运行方法、依赖与测试范围见 [RUN_EXAMPLES.md](RUN_EXAMPLES.md)。
浏览器、GUI、外部数据库和 Docker 例子按正文准备环境后复核。

## 配图复现

安装 matplotlib 后运行 python tools/create_figures.py。生成器优先使用 Windows 的微软雅黑字体，其他环境可把字体路径改成已安装的中文字体。
这些图为教学示意图。数据核对图使用项目三固定样本，任务条带图描述机制，不表示性能实测。
## 许可与勘误

书稿、LaTeX 文档、原创配图及成书 PDF 采用 CC BY-NC 4.0，示例代码和独立脚本采用 MIT。适用范围和完整协议入口见 [LICENSE](LICENSE)。

提交勘误时，请附版本、页码或章节、运行环境与最小复现。
