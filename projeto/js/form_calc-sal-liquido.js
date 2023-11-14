document.getElementById("salaryCalculatorForm").addEventListener("submit", function (event) {
    event.preventDefault();

    // Obter os valores do formulário
    const salary = parseFloat(document.getElementById("salary").value);
    const dependents = parseInt(document.getElementById("dependents").value) || 0;
    const otherDeductions = parseFloat(document.getElementById("otherDeductions").value) || 0;

    // Constantes de cálculo
    const inssRate = 0.08; // 8%
    const irrfRate = 0.075; // 7.5%
    const dependentDeduction = 189.59; // Valor da dedução por dependente em 2023

    // Cálculo dos descontos
    const inssDeduction = salary * inssRate;
    const irrfBase = salary - inssDeduction - (dependentDeduction * dependents);
    const irrfDeduction = irrfBase * irrfRate;

    // Cálculo do salário líquido
    const netSalary = salary - inssDeduction - irrfDeduction - otherDeductions;

    // Preencher os resultados na tabela
    document.getElementById("grossSalary").textContent = salary.toFixed(2);
    document.getElementById("taxesAndDeductions").textContent = (inssDeduction + irrfDeduction).toFixed(2);
    document.getElementById("netSalary").textContent = netSalary.toFixed(2);
});