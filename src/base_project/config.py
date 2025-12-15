from dynaconf import Dynaconf

from src.base_project.info import CONFIG_PATH, PYPROJECT


def settings_generator() -> Dynaconf:
    return Dynaconf(
        envvar_prefix=PYPROJECT["project"]["name"],
        environments=True,
        settings_files=["settings.toml", ".secrets.toml"],
        load_dotenv=True,
        root_path=CONFIG_PATH,
    )
