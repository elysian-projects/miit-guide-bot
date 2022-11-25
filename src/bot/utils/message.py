from typing import List

from ..constants.replies import Reply


def assemble_links_line(links: List[str], connector: str = ", "):
    if(len(links) == 0):
        raise ValueError("Couldn't find extra links!")

    return connector.join(links)


def get_more_links_message(links: List[str], connector: str = ", "):
    return f"{Reply.EXTRA_LINKS} {assemble_links_line(links, connector)}"
