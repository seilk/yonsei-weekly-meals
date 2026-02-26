from __future__ import annotations

import json

from src.updater import update


def main() -> None:
    payload = update()
    print(json.dumps({"generated_at": payload["generated_at"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
