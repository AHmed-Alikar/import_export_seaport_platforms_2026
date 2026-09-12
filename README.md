# Seaport Import/Export Platform

A full-stack app for managing seaport import/export operations — a Flask + MySQL backend (users, roles, RBAC, shipments) and a React dashboard for logging in and viewing them.

**Status: early-stage / actively developed.** Auth and role models exist; most of the dashboard is still scaffolding.

## Security note

An earlier commit accidentally included a real `.env` file and a hardcoded database credential in `backend/app/config.py`. Both are fixed as of this commit: the app now reads `SECRET_KEY` and `DATABASE_URI` from the environment and fails fast if either is missing, `.env` is gitignored, and a `.env.example` documents what's needed. **If the committed values were ever real, rotate them** — removing a file from the latest commit doesn't remove it from git history.

## Tech stack

| Layer | Choice |
|---|---|
| Backend | Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Cors |
| Database | MySQL (via `PyMySQL`) |
| Auth | Password hashing (`werkzeug.security`) + JWT (`PyJWT`) |
| Frontend | React (Create React App), React Router |

## Project structure

```
backend/
├── app/
│   ├── config.py       # env-based config (SECRET_KEY, DATABASE_URI)
│   ├── models/          # User, Role, Shipment
│   └── routes/          # auth (register/login/roles), dashboard
├── migrations/          # Flask-Migrate/Alembic migrations
└── run.py

seaport-frontend/
└── src/
    ├── components/       # LoginPage, Dashboard, Sidebar
    └── App.js
```

## Getting started

**Backend:**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in SECRET_KEY and DATABASE_URI
flask db upgrade        # apply migrations
python run.py
```

**Frontend:**
```bash
cd seaport-frontend
npm install
npm start
```

## API

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Create a user (username, password, role_id) |
| POST | `/login` | Authenticate, returns a JWT |
| POST | `/roles` | Create a role |

## Known limitations

- No automated tests.
- `/register` and `/login` do minimal input validation.
- Debug `print()` statements are still present in `routes/auth.py`.
- The JWT is signed with `SECRET_KEY` directly via `PyJWT` rather than through `Flask-JWT-Extended`, even though that package is installed and initialized — it's currently unused.
- No CI.

## License

Not yet licensed — treat as source-available for now.
