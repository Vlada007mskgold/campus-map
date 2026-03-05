// Загружаем MathJax асинхронно
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js';
document.head.appendChild(script);

// Обработчик для завершения загрузки MathJax
script.onload = async () => {
    await renderFormula();
};

async function renderFormula() {
    try {
        // Формула LaTeX
        const latexFormula = "\$\\forall n \\in \\mathbb{N}: n + 1 \\in \\mathbb{N}\$";
        
        // Создаем контейнер для формулы
        const formulaContainer = document.createElement('div');
        formulaContainer.id = 'latex-formula';  // назначаем уникальный id
        formulaContainer.style.marginTop = '20px';  // немного отступ сверху

        // Наполняем контейнер формулой
        formulaContainer.textContent = latexFormula;

        // Вставляем контейнер в конец body
        document.body.appendChild(formulaContainer);

        // Применяем рендеринг MathJax
        await MathJax.typesetPromise([formulaContainer]);
    } catch (err) {
        console.error('Ошибка рендеринга:', err.message);
    }
}