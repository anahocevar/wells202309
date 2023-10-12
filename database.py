from sqlalchemy import create_engine, text
import os


URL_DB = os.getenv("URL_DB")

def query_db(depth_min, grad_min):
    """Return wells based on criteria."""
    
    engine = create_engine(URL_DB)

    query = text("""
        SELECT latitude, longitude, depth, gradient
        FROM wells
        WHERE depth > :depth_min AND gradient > :grad_min
    """)

    with engine.connect() as conn:
        results = conn.execute(query, depth_min=depth_min, grad_min=grad_min).fetchall()
        
    return results

if __name__ == '__main__':
    import sys

    depth_min = float(sys.argv[1])
    grad_min = float(sys.argv[2])
    print(query_db(depth_min, grad_min))
    