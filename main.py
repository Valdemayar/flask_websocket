from app.main import app  # Импортируем экземпляр FastAPI приложения из app/__init__.py

# Добавляем маршруты к приложению
# app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn

    # Запуск FastAPI приложения с помощью Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
