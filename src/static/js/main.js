document.getElementById("ping").addEventListener("click", async () => {
    const result = document.getElementById("result");
    try {
        const res = await fetch("/api/health");
        const data = await res.json();
        result.textContent = `API: ${data.status}`;
    } catch (e) {
        result.textContent = "Ошибка запроса";
    }
});