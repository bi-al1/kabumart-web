"""
ローカル開発用サーバー起動スクリプト

実行方法:
    python webapp/start.py

ブラウザで http://localhost:8000 を開く
"""
import subprocess
import sys
import os

api_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api")

print("=" * 50)
print("  投資管理ダッシュボード ローカルサーバー")
print("=" * 50)
print()
print("  http://localhost:8000  でアクセスできます")
print("  終了するには Ctrl+C を押してください")
print()

subprocess.run(
    [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
    cwd=api_dir
)
