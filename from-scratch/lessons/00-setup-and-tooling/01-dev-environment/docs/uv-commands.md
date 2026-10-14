cd /d "D:\AI Projects\ai-engineering-from-scratch-1"

uv init --bare --name ai-engineering-from-scratch-1 --python 3.12 .

uv python pin 3.12

set "UV_PROJECT_ENVIRONMENT=ai-scratch"

uv add --requirements requirements.txt --link-mode=copy

ai-scratch\Scripts\activate

python phases\00-setup-and-tooling\01-dev-environment\code\verify.py