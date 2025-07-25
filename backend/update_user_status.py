from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.db.models.user import User

DATABASE_URL = "os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/astrobsm_db')"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def update_status(username, new_status):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if not user:
            print(f"User '{username}' not found.")
            return
        user.status = new_status
        session.commit()
        print(f"Status updated for user '{username}' to '{new_status}'.")
    except Exception as e:
        print(f"Error updating status: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    update_status("blakvelvet", "active")
