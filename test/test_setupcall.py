def test_setupcall():
    """
    Test the call of the setup function
    """
    import os
    import jupyter_gvim_proxy as jx

    os.environ["XPRA_BIN"] = "xpra"

    print("\nRunning test_setupcall...")
    print(jx.setup_gvim())
