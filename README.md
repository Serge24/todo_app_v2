# 📝 Task Management API

Une API RESTful construite avec Django et Django REST Framework pour gérer des tâches et leurs commentaires.

---

## 🚀 Fonctionnalités

- 🔐 Authentification par token
- 📋 CRUD complet sur les tâches
- 💬 Ajout et consultation de commentaires liés à une tâche
- 🧑 Association des commentaires à un utilisateur (optionnel)

---

## 📦 Installation

1. **Cloner le projet**

```bash
git clone https://github.com/serge24/todo_app.git
cd todo_app

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


**Authentification**
POST /api/auth/login/
{
  "username": "Serges02",
  "password": "pass@02"
}


🔹 Tâches
Méthode	URL	Description
GET	/api/tasks/	Liste des tâches
POST	/api/tasks/	Créer une nouvelle tâche
GET	/api/tasks/{id}/	Détails d’une tâche
PUT	/api/tasks/{id}/	Modifier une tâche
DELETE	/api/tasks/{id}/	Supprimer une tâche