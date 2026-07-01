# 🐍 Python CI/CD con GitHub Actions

Pipeline CI/CD completo para proyectos Python. Cubre lint, tests con coverage y deploy automático.

---

## 📁 Estructura

```
python-cicd-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # Pipeline principal
├── src/
│   ├── __init__.py
│   └── app.py                # Tu aplicación
├── tests/
│   └── test_app.py           # Tests unitarios
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline (3 etapas)

```
push / PR
    │
    ▼
┌─────────────┐
│ 1. BUILD    │  Instala deps + flake8 lint
│   & LINT    │
└──────┬──────┘
       │ ✅
       ▼
┌─────────────┐
│  2. TEST    │  pytest en Python 3.11 y 3.12
│  (matrix)   │  Coverage mínimo: 80%
└──────┬──────┘
       │ ✅ (solo main)
       ▼
┌─────────────┐
│  3. DEPLOY  │  Solo en push a main
│             │  Personaliza el paso de deploy
└─────────────┘
```

---

## 🚀 Inicio rápido

```bash
# Clonar y entrar al proyecto
git clone https://github.com/TU_USER/python-cicd-project.git
cd python-cicd-project

# Crear entorno virtual
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Correr tests localmente
pytest tests/ -v --cov=src --cov-report=term-missing
```

---

## 🔐 Configurar el Secret de Deploy

En tu repo GitHub: **Settings → Secrets and variables → Actions → New repository secret**

| Nombre          | Valor                          |
|-----------------|-------------------------------|
| `DEPLOY_TOKEN`  | Token de tu plataforma de deploy |

---

## 🎯 Personalizar el Deploy

Edita el paso `Simular deploy` en `.github/workflows/ci-cd.yml` con tu comando real:

```yaml
# Ejemplo AWS Elastic Beanstalk
- name: Deploy a AWS EB
  run: |
    pip install awsebcli
    eb deploy mi-entorno

# Ejemplo: SSH + rsync a servidor propio
- name: Deploy por SSH
  run: |
    rsync -avz ./src/ user@servidor:/app/src/
    ssh user@servidor "systemctl restart mi-app"
```

---

## ✅ Reglas del pipeline

| Condición                   | Resultado                    |
|-----------------------------|------------------------------|
| Coverage < 80%              | ❌ Pipeline falla             |
| Error de sintaxis (flake8)  | ❌ Pipeline falla             |
| PR a main                   | Corre build + test (no deploy)|
| Push a main                 | Corre build + test + deploy   |
| Push a develop              | Corre build + test (no deploy)|
