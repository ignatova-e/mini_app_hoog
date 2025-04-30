console.log(knowledgeBase);  // Проверим, загружены ли данные

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById("card-container");
    const searchInput = document.getElementById("searchInput");

    function displayCards(filteredItems) {
        container.innerHTML = '';

        if (filteredItems.length === 0) {
            container.innerHTML = '<p>Нет результатов для вашего запроса.</p>';
            return;
        }

        filteredItems.forEach(item => {
            const card = document.createElement("div");
            card.className = "card";
            const tags = item.tags || [];
            const tagsHTML = tags.map(tag => `<span class="tag tag-${tag}">${tag}</span>`).join(' ');

            card.innerHTML = `
                <h3>${item.title}</h3>
                <p>${item.description}</p>
                <div class="tags">${tagsHTML}</div>
            `;

            card.addEventListener('click', () => {
                console.log(`Открытие карточки: ${item.title}`);
                Swal.fire({
                    title: item.title,
                    html: `
                        <img src="${item.image}" alt="${item.title}" class="modal-image" />
                        <p>${item.content}</p>
                    `,
                    confirmButtonText: 'ОК'
                });
            });

            container.appendChild(card);
        });
    }

    // Поиск
    searchInput.addEventListener('input', (event) => {
        const searchTerm = event.target.value.toLowerCase();
        const filteredKnowledgeBase = knowledgeBase.filter(item => {
            return (
                item.title.toLowerCase().includes(searchTerm) ||
                item.description.toLowerCase().includes(searchTerm) ||
                item.content.toLowerCase().includes(searchTerm)
            );
        });

        displayCards(filteredKnowledgeBase);
    });

    // === ФИЛЬТР ПО ТЕГАМ ===
    const tagFilterContainer = document.getElementById("tagFilter");

    const uniqueTags = [...new Set(knowledgeBase.flatMap(item => item.tags || []))];

    uniqueTags.forEach(tag => {
        const btn = document.createElement("button");
        btn.className = "tag-button";
        btn.textContent = tag;
        btn.addEventListener("click", () => {
            document.querySelectorAll(".tag-button").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            const filtered = knowledgeBase.filter(item => (item.tags || []).includes(tag));
            displayCards(filtered);
        });
        tagFilterContainer.appendChild(btn);
    });

    const resetBtn = document.createElement("button");
    resetBtn.className = "tag-button";
    resetBtn.textContent = "Показать все";
    resetBtn.addEventListener("click", () => {
        document.querySelectorAll(".tag-button").forEach(b => b.classList.remove("active"));
        displayCards(knowledgeBase);
    });
    tagFilterContainer.prepend(resetBtn);

    // Первичная отрисовка
    displayCards(knowledgeBase);
});
