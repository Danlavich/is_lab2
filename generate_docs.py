from html import escape
from os import getenv
from pathlib import Path

import build
from inspect import getdoc, getmembers, isfunction, signature

def main():
    output = Path("dist/docs/index.html")
    output.parent.mkdir(parents=True, exist_ok=True)

    title = escape(build.TITLE)
    revision = escape(getenv("GITHUB_SHA", "локальная сборка"))
    sections = []
    markdown = ["# Документация проекта", f"Заголовок сайта — {build.TITLE}"]

    for name, function in getmembers(build, isfunction):
        if name.startswith("_") or function.__module__ != build.__name__:
            continue

        declaration = f"{name}{signature(function)}"
        description = getdoc(function) or "Описание отсутствует."

        sections.append(
            f"<h2><code>{escape(declaration)}</code></h2><p>{escape(description)}</p>"
        )
        markdown.extend([f"## `{declaration}`", description])

    repository_doc = Path("docs/README.md")
    repository_doc.parent.mkdir(parents=True, exist_ok=True)
    repository_doc.write_text("\n\n".join(markdown) + "\n", encoding="utf-8")

    output.write_text(
        f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Документация проекта</title>
</head>
<body>
    <h1>Документация проекта</h1>
    <p>Заголовок сайта — {title}</p>
    <p>Коммит сборки — <code>{revision}</code></p>
    {''.join(sections)}
    <p><a href="../">Открыть сайт проекта</a></p>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Документация сохранена в {output}")


if __name__ == "__main__":
    main()