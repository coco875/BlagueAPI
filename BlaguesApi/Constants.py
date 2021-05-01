from dataclasses import dataclass

JokeTypes = ["global", "dev", "dark", "limit", "beauf", "blondes"]


@dataclass
class Types:
    GLOBAL: str = 'global'
    DEV: str = 'dev'
    DARK: str = "dark"
    LIMIT: str = "limit"
    BEAUF: str = "beauf"
    BLONDES: str = "blondes"


logo = "https://raw.githubusercontent.com/DraftProducts/blagues-api/master/src/public/logo.png"
