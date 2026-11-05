"""逐项验证附录 C 的故意失败入口和修复版。需要 requests。"""
from pathlib import Path
import json
import os
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
folder=root/"examples/appendixC"
records=json.loads((folder/"cases.json").read_text(encoding="utf-8"))
environment=os.environ.copy()
environment["PYTHONIOENCODING"]="utf-8"
launcher="""from pathlib import Path
import json,sys
source=Path(sys.argv[1]).read_text(encoding="utf-8")
try:
    exec(compile(source,sys.argv[1],"exec"),{"__name__":"__main__"})
except BaseException as error:
    print(json.dumps({"mro":[cls.__name__ for cls in type(error).__mro__]},ensure_ascii=False))
else:
    raise SystemExit(77)
"""
for number,record in enumerate(records,1):
    good=folder/f"case_{number:02d}.py"
    run=subprocess.run([sys.executable,str(good)],env=environment,check=True,
                       capture_output=True,text=True,encoding="utf-8",timeout=12)
    assert run.stdout==record["output"],(number,run.stdout)
    bad=folder/f"case_{number:02d}_bad.py.txt"
    if record["mode"]=="semantic":
        run=subprocess.run([sys.executable,str(bad)],env=environment,check=True,
                           capture_output=True,text=True,encoding="utf-8",timeout=12)
        assert run.stdout==record["bad_output"],(number,run.stdout)
    else:
        run=subprocess.run([sys.executable,"-c",launcher,str(bad)],env=environment,
                           capture_output=True,text=True,encoding="utf-8",timeout=12)
        assert run.returncode==0,(number,run.stdout,run.stderr)
        assert record["exception"] in json.loads(run.stdout)["mro"],number
    print(f"C{number:02d}: error and repair verified.",flush=True)
print("31 records passed.")
