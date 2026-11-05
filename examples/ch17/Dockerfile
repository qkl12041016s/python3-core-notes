# 在本章样例目录构建，先生成 dist 里的 wheel。
FROM python:3.12-slim
WORKDIR /app
COPY dist/ /wheels/
RUN python -m pip install --no-cache-dir /wheels/*.whl
CMD ["python", "-m", "notes_demo"]
