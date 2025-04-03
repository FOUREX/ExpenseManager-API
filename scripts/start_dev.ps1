$env:DEV="True"
uvicorn src.main:app --host 127.0.0.1 --port 25565 --reload --timeout-graceful-shutdown 0
