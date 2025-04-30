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
            const tags = item.tags || [];  // если теги не указаны, создаем пустой массив
            const tagsHTML = tags.map(tag => `<span class="tag">${tag}</span>`).join(' ');

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

    // Первичная отрисовка
    displayCards(knowledgeBase);
});
