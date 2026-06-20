from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_mi0_documents_exist() -> None:
    required = [
        "docs/continuation_map.md",
        "docs/thesis_continuity_appendix.md",
        "docs/data_contracts.md",
        "docs/corporate_actions_and_price_policy.md",
        "docs/availability_evidence_policy.md",
        "docs/data_publication_policy.md",
        "docs/mi1_scope.md",
        "configs/universe_mi1.yaml",
        "configs/mi2_research_registry.yaml",
    ]
    for relative_path in required:
        assert (ROOT / relative_path).is_file(), relative_path


def test_mi1_scope_excludes_macro_and_execution() -> None:
    scope = (ROOT / "docs/mi1_scope.md").read_text(encoding="utf-8").lower()
    assert "macro data begins no earlier than mi-3" in scope
    assert "broker integration" in scope
    assert "portfolio construction or simulation" in scope


def test_public_data_directories_are_gitignored() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "/data/raw/*" in gitignore
    assert "/data/normalized/*" in gitignore
    assert "/data/private/*" in gitignore


def test_no_execution_modules_exist() -> None:
    prohibited_modules = ["alpaca.py", "broker.py", "execution.py", "orders.py"]
    package = ROOT / "src" / "market_intelligence_lab"
    for module_name in prohibited_modules:
        assert not (package / module_name).exists(), module_name
