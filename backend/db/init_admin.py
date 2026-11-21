from backend.db.database import SessionLocal
from backend.models.user import User
from backend.services.security import hash_password


def ensure_admin_exists():
    db = SessionLocal()
    try:
        admin_email = "admin@gyatri.ai"
        admin_user = db.query(User).filter(User.email == admin_email).first()
        if not admin_user:
            admin_user = User(
                name="System Administrator",
                email=admin_email,
                password_hash=hash_password("Admin@123"),
                role="admin"
            )
            db.add(admin_user)
            db.commit()
            print(f"Created default admin user: {admin_email} / Admin@123")
        else:
            if admin_user.role != "admin":
                admin_user.role = "admin"
                db.commit()
                print(f"Updated user {admin_email} to admin role")
            else:
                print(f"Admin user {admin_email} already exists")
    finally:
        db.close()


if __name__ == "__main__":
    ensure_admin_exists()

