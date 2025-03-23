### **3. Aggiunta di Test End-to-End**

I **test end-to-end** verificano il corretto funzionamento dell'intero sistema, simulando l'interazione dell'utente con l'interfaccia.

### **3.1. Strumenti per Test End-to-End**

- **Cypress**: Strumento per test end-to-end su applicazioni web.
- **Selenium**: Alternativa per test end-to-end su browser.

### **3.2. Configurazione di Cypress**

1. Installa Cypress:
    
    ```bash
    npm install cypress --save-dev
    
    ```
    
2. Crea un file di configurazione `cypress.json`:
    
    ```json
    {
      "baseUrl": "<http://localhost:3000>",
      "viewportWidth": 1280,
      "viewportHeight": 720
    }
    
    ```
    
3. Scrivi test end-to-end:

```jsx
// cypress/integration/simulations.spec.js
describe('Simulations Page', () => {
    it('Avvia una simulazione', () => {
        cy.visit('/simulations');
        cy.get('input[type="text"]').type('1');
        cy.get('button[type="submit"]').click();
        cy.contains('Simulazione completata').should('be.visible');
    });
});

```

---

### **4. Integrazione con Continuous Integration (CI)**

Configura un sistema di **Continuous Integration** per eseguire automaticamente i test ogni volta che viene effettuato un push o una pull request.

### **4.1. Configurazione di GitHub Actions**

1. Crea un file di configurazione `.github/workflows/ci.yml`:
    
    ```yaml
    name: CI
    
    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main
    
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'
          - name: Install dependencies
            run: |
              pip install -r requirements.txt
              pip install pytest pytest-cov
          - name: Run tests
            run: |
              pytest --cov=app tests/
    
    ```
    

### **4.2. Configurazione di Cypress in CI**

Aggiungi un job separato per i test end-to-end:

```yaml
jobs:
  test:
    # Job per test unitari e di integrazione
    ...

  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - name: Install dependencies
        run: |
          npm install
      - name: Run Cypress tests
        run: |
          npm run cypress:run

```

---

### **5. Copertura dei Test**

Utilizza strumenti come `pytest-cov` per misurare la copertura dei test e identificare aree del codice non testate.

### **5.1. Configurazione di pytest-cov**

1. Installa `pytest-cov`:
    
    ```bash
    pip install pytest-cov
    
    ```
    
2. Esegui i test con la copertura:
    
    ```bash
    pytest --cov=app tests/
    
    ```
    
3. Genera un report HTML:
    
    ```bash
    pytest --cov=app --cov-report=html tests/
    
    ```
    

---

### **6. Automazione dei Test**

### **6.1. Script per Esecuzione dei Test**

Crea uno script per eseguire tutti i test in modo automatizzato:

```bash
# run_tests.sh
#!/bin/bash

# Esegui test unitari e di integrazione
pytest --cov=app tests/

# Esegui test end-to-end
npm run cypress:run

```

### **6.2. Integrazione con Pre-commit Hooks**

Configura pre-commit hooks per eseguire i test automaticamente prima di ogni commit:

1. Installa `pre-commit`:
    
    ```bash
    pip install pre-commit
    
    ```
    
2. Crea un file `.pre-commit-config.yaml`:
    
    ```yaml
    repos:
      - repo: local
        hooks:
          - id: run-tests
            name: Run Tests
            entry: ./run_tests.sh
            language: system
            stages: [commit]
    
    ```
    
3. Installa i pre-commit hooks:
    
    ```bash
    pre-commit install
    
    ```
    

---

### **Conclusione**

Con queste migliorie, il sistema di **test automatici** di **RIQA_Software** diventerà più robusto, affidabile e adatto a un uso in produzione. L'aggiunta di test unitari, di integrazione, end-to-end e l'integrazione con strumenti di CI garantiranno la qualità del codice e la stabilità del software.