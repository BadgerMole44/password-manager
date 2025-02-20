# this file is intended to be run with pytest from the terminal 
import sqlite3, os, pytest
from pathlib import Path

@pytest.fixture(scope="module")
def setup():
    print("Setting up and initilizing test DB file")
    # init shared variables
    original_dir = Path.cwd()
    test_db_name = "SchemaTest.db"
    tables = ["Applications", "Accounts", "Usernames", "Recovery_info", "Passwords"]

    # alter the CWD
    cur_dir = Path(__file__).parent.resolve()
    os.chdir(cur_dir)

    # create and initialize the test schema file
    con = sqlite3.connect(test_db_name)
    with open("../DB/schema.sql", "r") as f:
        cur = con.cursor()
        schema_script = f.read()
        cur.executescript(schema_script)
        cur.close()
    con.close()

    yield (test_db_name, tables, original_dir)

@pytest.fixture(scope="module", autouse=True)
def cleanup(setup):
    yield
    print("Cleaning up test DB file")
    setup_info = setup
    Path.unlink(setup_info[0])
    os.chdir(setup_info[2])

"""
@pytest.fixture
def query(query:str):
    con = sqlite3.connect(test_db_name)
    cur = con.cursor()
    con.executescript(query)
    res = cur.fetchall()
    cur.close()
    con.close()
    return res
"""
    
# does the DB exist
def test_1(setup):
    setup_info = setup
    assert Path(setup_info[0]).exists() is True

# do all the tabels exist
# do all the tables have the required rows
# is each row correctly constrained
# is the ON DELETE set up correctly
# are the unique constraints being followed correctly





