<template>
    <header class="header">
        <div class="header-content">
            <img src="/logo.jpg" alt="Logo" class="header-logo" />
            <input type="text" class="header-search" placeholder="Search..." />
            <select class="header-language">
                <option value="en">EN</option>
                <option value="uk">UK</option>
            </select>
            <div class="header-actions">
                <a href="/profile" class="header-link">Profile</a>
                <a href="/basket" class="header-link">Basket</a>
            </div>
        </div>
    </header>
</template>

<script>
    export default {
        name: 'Header'
    };
</script>

<style scoped>
    /* Общие стили для заголовка */
/* Заголовок */
.header {
    background: linear-gradient(90deg, #f0f9ff, #e0f7fa);
    border-radius: 0; /* Убираем закругление, чтобы заголовок выглядел как часть страницы */
    padding: 10px 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    position: fixed; /* Закрепляем заголовок */
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000; /* Чтобы заголовок был поверх других элементов */
}

/* Контент заголовка */
.header-content {
    display: flex;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    justify-content: space-between;
}

/* Остальные стили остаются без изменений */
.header-logo {
    height: 50px;
    width: auto;
    margin-right: 20px;
    border-radius: 8px;
}

.header-title {
    font-family: 'Arial', sans-serif;
    font-size: 24px;
    font-weight: bold;
    color: #00796b;
    margin: 0 20px;
}

.header-search {
    flex-grow: 1;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #b2ebf2;
    margin: 0 20px;
    font-size: 16px;
    color: #e0f2f1;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 15px;
    right: 0;
}

.header-link {
    text-decoration: none;
    color: #00796b;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 8px;
    background: #e0f2f1;
    transition: background-color 0.3s ease;
}

.header-link:hover {
    background-color: #b2dfdb;
}

.header-language {
    padding: 8px;
    border-radius: 8px;
    border: 1px solid #b2ebf2;
    background: #e0f2f1;
    color: #004d40;
    font-size: 16px;
    outline: none;
    cursor: pointer;
}
</style>
