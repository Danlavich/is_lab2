# CI/CD Lab

Учебный проект на Python, который собирает статическую HTML-страницу.
GitHub Actions запускает тесты, собирает сайт и генерирует документацию.

## Локальный запуск

```powershell
python -m unittest -v
python build.py
python generate_docs.py
```

Сайт собирается в `dist/index.html`, документация — в `dist/docs/index.html`.

## CI/CD

На каждый push в `dev` GitHub Actions проверяет проект и сохраняет HTML-документацию
в артефакте `project-docs`. После успешной проверки ветки `release` сайт
и документация публикуются в GitHub Pages. Документация доступна по пути `/docs/`
относительно адреса сайта проекта.
