function calcularImposto() {
    const renda = parseFloat(document.getElementById('income').value);
    const deducoes = parseFloat(document.getElementById('deductions').value);

    if (isNaN(renda) || isNaN(deducoes)) {
      alert('Por favor, insira valores válidos.');
      return;
    }

    const imposto = calcularImpostoRenda(renda, deducoes);
    document.getElementById('resultado').textContent = `Imposto de Renda devido: R$ ${imposto.toFixed(2)}`;
  }

  function calcularImpostoRenda(renda, deducoes) {
    // Lógica de cálculo do imposto de renda aqui (exemplo simplificado)
    // Esta lógica é apenas um exemplo e pode não representar a realidade fiscal.
    const baseCalculo = renda - deducoes;
    const taxa = 0.15; // Taxa fictícia de 15%
    const impostoDevido = baseCalculo * taxa;
    return impostoDevido;
  }