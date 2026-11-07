from html import escape
from pathlib import Path

TITLE = "ПР2: CI/CD - релизная версия"


def render_page(title):
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>{escape(title)}</title>
</head>
<body>
    <h1>{escape(title)}</h1>
    <p>Страница опубликована через GitHub Actions.</p>
</body>
</html>
"""


def main():
    output = Path("dist/index.html")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_page(TITLE), encoding="utf-8")


if __name__ == "__main__":
    main()