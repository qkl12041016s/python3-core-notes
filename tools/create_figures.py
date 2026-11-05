"""生成书稿插图。图中示例数据与文字都在此文件中，可重复导出。"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
import sys
ONLY=set(sys.argv[1:])

font_file = Path("C:/Windows/Fonts/msyh.ttc")
if font_file.exists():
    font_manager.fontManager.addfont(str(font_file))
    family = font_manager.FontProperties(fname=str(font_file)).get_name()
else:
    family = "DejaVu Sans"
plt.rcParams.update({"font.family":family,"axes.unicode_minus":False,
                     "pdf.fonttype":42,"savefig.facecolor":"#F6F9FC"})
BLUE="#3776AB"; YELLOW="#FFD43B"; INK="#172B40"; MUTED="#4C6278"
DARK="#122236"; LIGHT="#E8F1F8"; RED="#B43B49"; GREEN="#287E71"
OUT=Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(parents=True,exist_ok=True)

def canvas(title, subtitle, height=4.0):
    fig,ax=plt.subplots(figsize=(10,height))
    fig.patch.set_facecolor("#F6F9FC")
    ax.set(xlim=(0,10),ylim=(0,height))
    ax.axis("off")
    ax.text(.30,height-.28,title,fontsize=17,fontweight="bold",color=INK,va="top")
    ax.text(.32,height-.72,subtitle,fontsize=9,color=MUTED,va="top")
    return fig,ax

def box(ax,x,y,w,h,title,body="",color=BLUE,dark=False):
    fill=DARK if dark else "white"
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.025,rounding_size=.09",
                               facecolor=fill,edgecolor=color,linewidth=1.3))
    ax.add_patch(Rectangle((x+.03,y+h-.10),w-.06,.07,facecolor=color,edgecolor="none"))
    ax.text(x+.16,y+h-.24,title,fontsize=12 if h<1.4 else 14,fontweight="bold",
            color=YELLOW if dark else color,va="top")
    if body:
        ax.text(x+.16,y+h-(.55 if h<1.4 else .65),body,fontsize=11 if h<1.4 else 13,color="white" if dark else INK,
                va="top",linespacing=1.25 if h<1.4 else 1.55)

def arrow(ax,a,b,color=BLUE,dashed=False):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=12,
                                 color=color,linewidth=1.4,
                                 linestyle="--" if dashed else "-"))

def save(fig,name):
    if ONLY and name not in ONLY:
        plt.close(fig)
        return
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    fig.savefig(OUT/(name+".pdf"),bbox_inches="tight",pad_inches=.02)
    fig.savefig(OUT/(name+".png"),dpi=180,bbox_inches="tight",pad_inches=.02)
    plt.close(fig)

fig,ax=canvas("先确认脚下是哪一个 Python","界面示意。终端与项目运行需要指向同一个解释器。")
box(ax,.35,.50,4.0,2.25,"PyCharm / Project Interpreter",
    ".venv / Scripts / python.exe\n项目依赖随这个环境读取",BLUE,True)
box(ax,5.15,.50,4.45,2.25,"Terminal / Run",
    "print(sys.executable)\n.venv / Scripts / python.exe",GREEN,True)
arrow(ax,(4.5,1.65),(5.0,1.65));ax.text(4.68,2.1,"核对",ha="center",color=BLUE,fontsize=10)
save(fig,"interpreter")

fig,ax=canvas("名字指向对象，复制要看哪一层","箭头表示引用。新建外层列表，不会自动复制内层列表。",4.3)
box(ax,.3,2.0,2.2,.95,"original",color=BLUE)
box(ax,.3,.55,2.2,.95,"copied",color=GREEN)
box(ax,3.3,2.0,2.35,.95,"外层列表 A",color=BLUE)
box(ax,3.3,.55,2.35,.95,"外层列表 B",color=GREEN)
box(ax,6.7,1.15,2.95,1.55,"共享的内层列表",'["notes.md"]',YELLOW,True)
arrow(ax,(2.55,2.48),(3.2,2.48));arrow(ax,(2.55,1.02),(3.2,1.02),GREEN)
arrow(ax,(5.72,2.48),(6.62,2.05));arrow(ax,(5.72,1.02),(6.62,1.65),GREEN)
save(fig,"references")

fig,ax=canvas("Type Info 与断点里的值，各看一层","IDE 示意图。菜单与布局以实际安装版本为准。",4.4)
box(ax,.35,.45,5.5,2.65,"variables.py",
    'retries: int = 3\nsummary = f"最多重试 {retries} 次"\nprint(summary)',BLUE,True)
box(ax,6.25,1.95,3.35,1.15,"Type Info","summary → str",BLUE)
box(ax,6.25,.45,3.35,1.15,"Variables","retries → 3\nsummary → 最多重试 3 次",GREEN)
arrow(ax,(5.92,2.3),(6.18,2.45));arrow(ax,(5.92,1.1),(6.18,1.0),GREEN)
save(fig,"type-info")

fig,ax=canvas("从异常末行定位到项目代码","字符串与整数相加触发 TypeError，先看异常类型，再定位函数。",4.4)
box(ax,.35,.50,6.2,2.6,"Run / Traceback",
    'File "main.py", line 2, in add\n    return a + b\nTypeError: unsupported operand type(s)\nfor +: \'str\' and \'int\'',BLUE,True)
box(ax,7.0,1.9,2.6,1.15,"第 1 步","读异常类型",RED)
box(ax,7.0,.50,2.6,1.15,"第 2 步","读文件与行号",BLUE)
arrow(ax,(6.65,1.3),(6.94,2.35),RED);arrow(ax,(6.65,2.55),(6.94,1.08))
save(fig,"traceback")

fig,ax=canvas("列表追加以后，预览仍保留前两项","切片得到新外层列表。本例的元素是不可变字符串。",4.0)
box(ax,.35,.55,4.35,2.05,"files",
    '0  notes.md\n1  todo.md\n2  ideas.md  ← append',BLUE,True)
box(ax,5.3,.55,4.35,2.05,"preview = files[:2]",
    '0  notes.md\n1  todo.md',GREEN,True)
save(fig,"list-preview")

fig,ax=canvas("差集回答还缺什么，交集回答已经有什么","请求名单先去重，再与服务器名单对照。",4.0)
box(ax,.35,.55,2.7,2.05,"wanted",
    "notes.md\ntodo.md",BLUE,True)
box(ax,3.6,.55,2.7,2.05,"remote","notes.md",GREEN,True)
box(ax,6.85,.55,2.7,2.05,"wanted − remote","todo.md",YELLOW,True)
arrow(ax,(3.11,1.55),(3.48,1.55));arrow(ax,(6.36,1.55),(6.73,1.55))
save(fig,"set-difference")

fig,ax=canvas("同一份日志，可以数票，也可以分筐","Counter 留次数，defaultdict(list) 留对应记录。",4.0)
box(ax,.35,.55,2.8,2.05,"events","notes.md / ok\ntodo.md / retry\ndraft.md / retry",BLUE,True)
box(ax,4.0,1.65,5.55,1.0,"Counter","ok → 1       retry → 2",BLUE)
box(ax,4.0,.35,5.55,1.0,"defaultdict(list)","retry → [todo.md, draft.md]",GREEN)
arrow(ax,(3.2,1.9),(3.9,2.10));arrow(ax,(3.2,1.3),(3.9,.85),GREEN)
save(fig,"grouping")

fig,ax=canvas("名字查找沿作用域逐层向外","这里展示普通函数的查找路径。闭包保留外层绑定。",4.2)
for x,w,title,color in [(0.4,9.2,"Builtins / 内置名字",BLUE),
                        (0.8,8.4,"Global / 模块名字",GREEN),
                        (1.2,7.6,"Enclosing / 外层函数",BLUE),
                        (1.6,6.8,"Local / 当前函数",YELLOW)]:
    y=.35+(x-.4)*1.2
    h=3.0-(x-.4)*1.2
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.01",facecolor="white",
                               edgecolor=color,linewidth=1.25))
    ax.text(x+.16,y+.10,title,fontsize=9,color=INK)
ax.text(4.95,2.4,"先从当前函数开始找",ha="center",fontsize=11,color=BLUE,fontweight="bold")
save(fig,"scope")

fig,ax=canvas("装饰时包装，调用时执行","两个时间段分开观察，断点就容易设对位置。",4.3)
box(ax,.35,.5,4.2,2.5,"装饰时",
    "定义原函数 add\n执行 timer(add)\n把 wrapped 绑定回 add",BLUE,True)
box(ax,5.25,.5,4.35,2.5,"调用时",
    "进入 wrapped\n计时 → 调用原函数 → 交回结果\nfinally 记录耗时",YELLOW,True)
arrow(ax,(4.61,1.75),(5.16,1.75))
save(fig,"decorator")

fig,ax=canvas("一次事务，要么提交，要么回滚","虚线为异常路径。连接清理在两条路径之后统一安排。",4.3)
box(ax,.35,1.25,2.3,1.45,"开始事务","执行 SQL",BLUE)
box(ax,3.5,1.25,2.3,1.45,"改动完成","等待确认",BLUE)
box(ax,6.8,2.0,2.65,1.1,"成功","COMMIT",GREEN)
box(ax,6.8,.35,2.65,1.1,"异常","ROLLBACK",RED)
arrow(ax,(2.72,1.98),(3.41,1.98))
arrow(ax,(5.87,2.15),(6.72,2.55),GREEN)
arrow(ax,(5.87,1.6),(6.72,.9),RED,True)
save(fig,"transaction")

fig,ax=canvas("等待时，工作如何交接","机制示意。块的长度不代表本机性能测试。",4.3)
for y,title in [(2.7,"线程"),(1.65,"进程"),(.60,"协程")]:
    ax.text(.35,y+.15,title,color=INK,fontsize=11,fontweight="bold")
    for x,w,label,color in [(1.6,1.7,"开始处理",BLUE),(3.45,2.5,"等待 / 协作",YELLOW),(6.1,2.7,"继续处理",GREEN)]:
        ax.add_patch(FancyBboxPatch((x,y-.1),w,.65,boxstyle="round,pad=.02",
                                   facecolor=color,edgecolor="none"))
        ax.text(x+w/2,y+.22,label,ha="center",va="center",color=INK if color==YELLOW else "white",fontsize=10)
ax.text(1.6,.25,"共享内存、独立内存、事件循环，对应不同的交接约定。",fontsize=9,color=MUTED)
save(fig,"concurrency")

fig,ax=canvas("HTTP 请求和响应，按去回两程读","请求方法、路径与请求头在去程，状态码、响应头与内容在回程。",4.4)
for x,label in [(1.5,"客户端"),(8.45,"服务端")]:
    ax.text(x,3.05,label,ha="center",color=BLUE,fontsize=12,fontweight="bold")
    ax.plot([x,x],[.5,2.8],color="#B6C8D7",linewidth=2)
arrow(ax,(1.55,2.45),(8.38,2.45))
ax.text(4.95,2.62,"GET /notes     请求头",ha="center",fontsize=11,color=INK)
arrow(ax,(8.38,1.5),(1.55,1.5),GREEN)
ax.text(4.95,1.67,"200 OK     JSON 响应体",ha="center",fontsize=11,color=GREEN)
ax.text(4.95,.75,'核对状态 → 解析 {"name": "notes.md"} → 校验字段',ha="center",fontsize=10,color=INK)
save(fig,"http")

fig,ax=canvas("输入从界面进来，规则在业务层执行","界面和 API 可以共用同一层业务与 SQLite 存储。",4.0)
for x,w,title,body,color in [
(.35,2.7,"入口","PyQt 窗口\nFastAPI 接口",BLUE),
(3.65,2.7,"业务","校验输入\n按规则处理",YELLOW),
(6.95,2.7,"存储","参数绑定\nSQLite 事务",GREEN)]:
    box(ax,x,.55,w,2.1,title,body,color,True)
arrow(ax,(3.11,1.55),(3.54,1.55));arrow(ax,(6.41,1.55),(6.84,1.55),GREEN)
save(fig,"architecture")

fig,ax=canvas("NumPy 的形状与切片，一格一格看","数组为 [[1, 2], [3, 4]]。复制选中列后，再修改副本。",4.2)
for r in range(2):
    for c in range(2):
        x=1.0+c*.9;y=1.9-r*.9
        ax.add_patch(Rectangle((x,y),.85,.75,facecolor=YELLOW if c==0 else LIGHT,
                               edgecolor=BLUE,linewidth=1.5))
        ax.text(x+.425,y+.375,str([[1,2],[3,4]][r][c]),ha="center",va="center",fontsize=17,color=INK)
ax.text(1.9,.55,"shape = (2, 2)",ha="center",fontsize=11,color=BLUE)
box(ax,4.2,1.0,2.0,1.65,"切片视图","第一列\n共享底层数据",BLUE)
box(ax,7.1,1.0,2.45,1.65,"copy 后","独立数据\n修改不写回原数组",GREEN)
arrow(ax,(2.9,1.75),(4.08,1.75));arrow(ax,(6.28,1.75),(6.98,1.75),GREEN)
save(fig,"array")

fig,ax=canvas("报表先对数，再出图","本书项目样本。4 行输入，按 event_id 去重后剩 3 个事件。",4.4)
labels=["原始行","事件数","有效耗时"]
values=[4,3,2]
for x,label,value,color in zip([1.4,4.6,7.8],labels,values,[BLUE,YELLOW,GREEN]):
    h=value*.5
    ax.add_patch(Rectangle((x,.6),1.8,h,facecolor=color,edgecolor="none"))
    ax.text(x+.9,h+.75,str(value),ha="center",fontsize=18,fontweight="bold",color=INK)
    ax.text(x+.9,.25,label,ha="center",fontsize=11,color=INK)
save(fig,"quality")

fig,ax=canvas("把源码送到另一个环境，还能跑一遍","源码、构建产物和安装环境，逐步留出核对点。",4.0)
for x,title,body,color in [
(.35,"源码","pyproject.toml\nnotes_demo/",BLUE),
(3.65,"wheel","dist/*.whl\n包名与版本",YELLOW),
(6.95,"新环境","安装包\n离开源码目录运行",GREEN)]:
    box(ax,x,.55,2.7,2.1,title,body,color,True)
arrow(ax,(3.1,1.55),(3.55,1.55));arrow(ax,(6.4,1.55),(6.85,1.55),GREEN)
save(fig,"package")

fig,ax=canvas("按错误现场选择排查层次","先保留输入和回溯，再选最短的排查路径。",4.4)
box(ax,.35,1.15,2.35,1.55,"错误现场","输入 + 回溯\n解释器 + 目录",RED,True)
for y,title,body,color in [(2.2,"代码与数据","类型、索引、字段",BLUE),
                            (1.05,"文件与环境","路径、编码、依赖",GREEN),
                            (-.1,"外部服务","状态、超时、端口",BLUE)]:
    box(ax,4.0,y+.3,5.5,.98,title,body,color)
    arrow(ax,(2.77,1.9),(3.9,y+.82),color)
save(fig,"diagnosis")
print("Created",len(list(OUT.glob("*.pdf"))),"vector figures.")
