// const container = document.getElementById("card-container");

// knowledgeBase.forEach(item => {
//     const card = document.createElement("div");
//     card.className = "card";
//     card.innerHTML = `
//         <h3>${item.title}</h3>
//         <p>${item.description}</p>
//     `;

//     card.onclick = () => {
//         Swal.fire({
//             title: item.title,
//             html: `
//                 <img src="${item.image}" alt="${item.title}" class="modal-image" />
//                 <p>${item.content}</p>
//             `,
//             confirmButtonText: 'ОК'
//         });
//     };

//     container.appendChild(card);
// });

const container = document.getElementById("card-container");
const searchInput = document.getElementById("searchInput");

// Функция для фильтрации и отображения карточек
function displayCards(filteredItems) {
    container.innerHTML = ''; // Очищаем контейнер перед выводом новых данных

    filteredItems.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <h3>${item.title}</h3>
            <p>${item.description}</p>
        `;
        card.onclick = () => {
            Swal.fire({
                title: item.title,
                html: `
                    <img src="${item.image}" alt="${item.title}" class="modal-image" />
                    <p>${item.content}</p>
                `,
                confirmButtonText: 'ОК'
            });
        };
        container.appendChild(card);
    }

// Фильтрация по запросу в поле поиска
searchInput.addEventListener('input', (event) => {
        const searchTerm = event.target.value.toLowerCase(); // Получаем введенный запрос
        const filteredKnowledgeBase = knowledgeBase.filter(item => {
            return (
                item.title.toLowerCase().includes(searchTerm) ||
                item.description.toLowerCase().includes(searchTerm) ||
                item.content.toLowerCase().includes(searchTerm)
            );
        });

        displayCards(filteredKnowledgeBase); // Показываем отфильтрованные статьи
    });

    // Изначально выводим все карточки
    displayCards(knowledgeBase);
