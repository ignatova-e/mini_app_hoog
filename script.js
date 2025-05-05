// Подключение к контейнерам
const cardContainer = document.getElementById("card-container");
const tagFilterContainer = document.getElementById("tag-filter");
const searchInput = document.getElementById("search-input");
const resetBtn = document.getElementById("reset-btn");

let activeTag = null; // текущий выбранный тег

function createCard(item) {
    const card = document.createElement("div");
    card.className = "card";

    const cardInner = document.createElement("div");
    cardInner.className = "card-inner";

    // Передняя сторона
    const cardFront = document.createElement("div");
    cardFront.className = "card-front";
    const title = document.createElement("h2");
    title.textContent = item.title;
    cardFront.appendChild(title);

    // Теги
    if (item.tags && item.tags.length > 0) {
        const tagContainer = document.createElement("div");
        tagContainer.className = "tags";

        item.tags.forEach((tag) => {
            const span = document.createElement("span");
            span.className = "tag";
            span.textContent = tag;
            tagContainer.appendChild(span);
        });

        cardFront.appendChild(tagContainer);
    }

    // Задняя сторона
    const cardBack = document.createElement("div");
    cardBack.className = "card-back";
    const content = document.createElement("p");
    content.textContent = item.description;
    cardBack.appendChild(content);

    // Собираем
    cardInner.appendChild(cardFront);
    cardInner.appendChild(cardBack);
    card.appendChild(cardInner);

    // Клик: поворот и модалка
    card.addEventListener("click", () => {
        card.classList.toggle("flipped");

        Swal.fire({
            title: item.title,
            html: `
                <img src="${item.image}" alt="${item.title}" class="modal-image" onerror="this.style.display='none'" />
                <div style="max-height: 300px; overflow-y: auto; text-align: left;">
                    <p>${item.content.replace(/\n/g, "<br/>")}</p>
                </div>
            `,
            confirmButtonText: "ОК",
        });

        // Если используется Telegram Mini App
        if (window.Telegram && Telegram.WebApp) {
            Telegram.WebApp.sendData(
                JSON.stringify({ selectedCard: item.title }),
            );
        }
    });

    return card;
}

function displayCards(data) {
    cardContainer.innerHTML = "";

    if (data.length === 0) {
        const message = document.createElement("p");
        message.textContent = "Пока нет подходящих карточек 😢";
        cardContainer.appendChild(message);
        return;
    }

    data.forEach((item) => {
        const card = createCard(item);
        cardContainer.appendChild(card);
    });
}

// Поиск + фильтрация по тегу
function filterAndSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    let filtered = knowledgeBase;

    if (activeTag) {
        filtered = filtered.filter((item) =>
            (item.tags || []).includes(activeTag),
        );
    }

    if (searchTerm) {
        filtered = filtered.filter(
            (item) =>
                item.title.toLowerCase().includes(searchTerm) ||
                item.description.toLowerCase().includes(searchTerm) ||
                item.content.toLowerCase().includes(searchTerm),
        );
    }

    displayCards(filtered);
}

// Инициализация тегов
const uniqueTags = [
    ...new Set(knowledgeBase.flatMap((item) => item.tags || [])),
];

uniqueTags.forEach((tag) => {
    const btn = document.createElement("button");
    btn.className = "tag-button";
    btn.textContent = tag;
    btn.addEventListener("click", () => {
        document
            .querySelectorAll(".tag-button")
            .forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeTag = tag;
        filterAndSearch();
    });
    tagFilterContainer.appendChild(btn);
});

// Сброс фильтров
resetBtn.addEventListener("click", () => {
    document
        .querySelectorAll(".tag-button")
        .forEach((b) => b.classList.remove("active"));
    searchInput.value = "";
    activeTag = null;
    displayCards(knowledgeBase);
});

// Поиск при вводе
searchInput.addEventListener("input", filterAndSearch);

// Telegram WebApp
if (window.Telegram && Telegram.WebApp) {
    Telegram.WebApp.ready();
    const startParam = Telegram.WebApp.initDataUnsafe.start_param;
    console.log("Получен start_param:", startParam);

    // Пример действия на основе параметра:
    if (startParam === "1") {
        // Автоматически выбираем нужный тег, фильтруем карточки
        activeTag = "exampleTag"; // замени на тег, который ты хочешь показать
        filterAndSearch();

        // Можно также выделить кнопку тега, если нужно
        const tagBtn = [...document.querySelectorAll(".tag-button")].find(
            (btn) => btn.textContent === activeTag,
        );
        if (tagBtn) tagBtn.classList.add("active");
    }

    Telegram.WebApp.expand();
}

// Загрузка карточек
window.addEventListener("DOMContentLoaded", () => {
    displayCards(knowledgeBase);
});
