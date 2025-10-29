
def test_imports():
    import bioomicshub
    from bioomicshub.core import preprocessing, visualization, ml_utils
    assert hasattr(bioomicshub, "__version__")
