<template>
    <header class="header">
      <div class="logo-section">
        <img src="/Tomorrowland.webp" alt="Logo" class="logo" />
        <span class="site-name">Festival Shop</span>
      </div>
      <div class="search-section">
        <input type="text" placeholder="Search..." class="search-input" />
      </div>
      <div class="actions-section">
        <select class="language-select">
          <option value="en">EN</option>
          <option value="ua">UA</option>
        </select>
        <button class="profile-button">Profile</button>
        <button class="basket-button">Basket</button>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header'
  };
  </script>
  
  <style scoped>
  .header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #f5f5f5;
    border-bottom: 1px solid #ddd;
    z-index: 1000;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .logo-section {
    display: flex;
    align-items: center;
  }
  
  .logo {
    height: 40px;
    margin-right: 10px;
  }
  
  .site-name {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
  }
  
  .search-section {
    flex-grow: 1;
    text-align: center;
  }
  
  .search-input {
    width: 60%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .actions-section {
    display: flex;
    align-items: center;
  }
  
  .language-select {
    margin-right: 15px;
    padding: 5px;
  }
  
  .profile-button,
  .basket-button {
    background-color: transparent;
    border: none;
    font-size: 1rem;
    margin-right: 10px;
    cursor: pointer;
  }
  
  .profile-button:hover,
  .basket-button:hover {
    color: #007bff;
  }
  
  /* Додамо відступ зверху, щоб уникнути перекривання контенту хедером */
  #app {
    padding-top: 70px; /* Відступ, рівний висоті хедера */
  }
  </style>
