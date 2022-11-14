from typing import List


def assemble_links_line(links: List[str], connector: str = ", "):
    if(len(links) == 0):
        return ""

    return connector.join(links)
