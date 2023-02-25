import os
from sqlalchemy import create_engine, text

print(os.getenv("dburl"))

db_connection = "[REDACTED]]"


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
    for row in result:
      jobs.append(row)
    return jobs