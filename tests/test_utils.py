import sqlite3
import tempfile
from pathlib import Path
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.utils import strip_sql_markup, describe_table, list_tables, DB_PATH

@pytest.fixture(scope="module")
def test_db(monkeypatch):
    # Cria um banco de dados temporário
    tmp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    monkeypatch.setenv("HUBIA_DB", tmp_db.name)

    # Inicializa uma tabela de teste
    conn = sqlite3.connect(tmp_db.name)
    conn.execute("""
        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL
        );
    """)
    conn.commit()
    conn.close()

    yield Path(tmp_db.name)

    # Cleanup
    tmp_db.close()
    Path(tmp_db.name).unlink(missing_ok=True)

def test_strip_sql_markup():
    text = "```sql\nSELECT * FROM produtos;\n```"
    assert strip_sql_markup(text) == "SELECT * FROM produtos;"

def test_strip_sql_markup_without_code_block():
    text = "SELECT * FROM produtos;"
    assert strip_sql_markup(text) == "SELECT * FROM produtos;"

def test_list_tables(test_db, monkeypatch):
    # Força o uso do banco temporário
    monkeypatch.setattr("seu_modulo.DB_PATH", test_db)
    tables = list_tables()
    assert "produtos" in tables

def test_describe_table(test_db, monkeypatch):
    monkeypatch.setattr("seu_modulo.DB_PATH", test_db)
    cols = describe_table("produtos")
    assert ("id", "INTEGER") in cols
    assert ("nome", "TEXT") in cols
    assert ("preco", "REAL") in cols
