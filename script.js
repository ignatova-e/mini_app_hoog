const container = document.getElementById("card-container");

knowledgeBase.forEach(item => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `<h3>${item.title}</h3><p>${item.description}</p>`;
    card.onclick = () => {
        Swal.fire({
            title: item.title,
            html: `<p>${item.content}</p>`,
            confirmButtonText: 'ОК'
        });
    };
    container.appendChild(card);
});