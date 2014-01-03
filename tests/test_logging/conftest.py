#!/usr/bin/env python2.6
import tempfile
import pytest


@pytest.fixture
def log_file(request):
    f = tempfile.NamedTemporaryFile()
    request.addfinalizer(lambda: f.close())
    return f
