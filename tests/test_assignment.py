import os
import pytest
import re

# Generate the list of files once
sql_files = [f for f in os.listdir(".") if re.search(r'\d{1,2}.sql', f)]

@pytest.mark.parametrize("sql_file", sql_files)
def test_sql(sql_file):
    result = os.popen(f'sqlite3 *.db < {sql_file} | md5sum').read().strip()
    expected = os.popen(f'cat tests/{sql_file}.md5').read().strip()
    assert result == expected
