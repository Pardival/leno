from pathlib import Path

PROMPTS_DIR = Path(__file__).parent

def load_prompt(name: str) -> str:
    prompt_path = PROMPTS_DIR / f"{name}.md"
    return prompt_path.read_text(encoding="utf-8")

def build_classification_prompt(categories_existantes: list[str]) -> str:
    template = load_prompt("classificator")
    categories_str = ", ".join(categories_existantes) if categories_existantes else "Aucune pour l'instant"
    prompt = template.replace("{CATEGORIES_EXISTANTES}", categories_str)
    return prompt