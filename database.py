import os
from sqlalchemy import create_engine, text

db_connection = os.getenv("DB_STRING")

engine = create_engine(
  db_connection,
  connect_args={
    "ssl": {
       "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
