const sectionsContainer = document.getElementById("sections");
const articlesContainer = document.getElementById("articles");
const searchInput = document.getElementById("search");

// Показать список разделов
function renderSections() {
    sectionsContainer.innerHTML = "";
    knowledgeBase.forEach((section, index) => {
        const btn = document.createElement("button");
        btn.textContent = section.title;
        btn.className = "section-button";
        btn.onclick = () => renderArticles(index);
        sectionsContainer.appendChild(btn);
    });
}

// Показать статьи выбранного раздела
function renderArticles(sectionIndex) {
    const section = knowledgeBase[sectionIndex];
    articlesContainer.innerHTML = `<h2>${section.title}</h2>`;
    section.articles.forEach(article => {
        const div = document.createElement("div");
        div.className = "article";
        div.innerHTML = `<h3>${article.title}</h3><p>${article.content}</p>`;
        articlesContainer.appendChild(div);
    });
}

// Поиск по всем статьям
searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();
    articlesContainer.innerHTML = "<h2>Результаты поиска</h2>";

    knowledgeBase.forEach(section => {
        section.articles.forEach(article => {
            if (
                article.title.toLowerCase().includes(query) ||
                article.content.toLowerCase().includes(query)
            ) {
                const div = document.createElement("div");
                div.className = "article";
                div.innerHTML = `<h3>${article.title}</h3><p>${article.content}</p>`;
                articlesContainer.appendChild(div);
            }
        });
    });

    if (!articlesContainer.innerHTML.includes("article")) {
        articlesContainer.innerHTML += "<p>Ничего не найдено.</p>";
    }
});

// Telegram WebApp API — UI улучшения
if (window.Telegram.WebApp) {
    Telegram.WebApp.expand();
    Telegram.WebApp.setHeaderColor('#ffffff');
}

renderSections();
