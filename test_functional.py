import main


def test_program_exits_on_abort(monkeypatch, capsys):
    monkeypatch.setattr(main, 'input', lambda: "abort", raising=False)
    main.run()
    captured = capsys.readouterr()
    assert 'Good bye!\n' == captured.out
