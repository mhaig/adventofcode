#!/usr/bin/env python3

import logging
import sys

from rich import print
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, track

console = Console()

FORMAT = "%(message)s"
logging.basicConfig(
    level="ERROR", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


def get_rules(page, rules) -> list[str]:
    """Given a page, get all the rules that involve the page."""
    return_rules = []
    for r in rules:
        if page in r:
            return_rules.append(r)

    return return_rules


def test_update(update, rules) -> bool:
    """Given an update, test it against the rules to see if it complies."""

    for i, page in enumerate(update):
        log.debug(f"Checking page: {page}")
        # Get any rules that involve this page.
        page_rules = get_rules(page, rules)
        log.debug(f"Found the following rules: {page_rules}")
        for r in page_rules:
            before, after = r.split("|")
            if before == page:
                # This page must be before.
                log.debug(f"Page {page} must be before {after}")
                if after in update[0:i]:
                    log.debug(f"Found {after} before {page} :(")
                    return False
            else:
                # This page must be after.
                log.debug(f"Page {page} must be after {before}")
                if before in update[i:]:
                    log.debug(f"Found {before} in {update[i:]} :(")
                    return False

        log.debug(f"{page} is good!")
    return True


rules = []
updates = []

for line in sys.stdin.readlines():
    if "|" in line:
        rules.append(line.strip())
    elif "," in line:
        updates.append(line.strip())


def calculate_middle_page_sum(updates):
    middle_page_sum = 0
    for u in updates:
        middle_page_sum += int(u.split(",")[(len(u.split(",")) - 1) // 2])

    return middle_page_sum


good_updates = [x for x in updates if test_update(x.split(","), rules)]
middle_page_sum = calculate_middle_page_sum(good_updates)

print(f"Day 5 Part 1 Solution: {middle_page_sum}")


def make_one_fix(update, rules) -> list[str]:
    # Current version of update doesn't pass, fix and try again.
    for i, page in enumerate(update):
        # Get any rules that involve this page.
        page_rules = get_rules(page, rules)
        log.info(f"Found the following rules: {page_rules}")
        for r in page_rules:
            before, after = r.split("|")
            if before == page:
                # This page must be before.
                log.info(f"Page {page} must be before {after}")
                if after in update[0:i]:
                    log.info(f"Found {after} before {page} :(")
                    update.remove(after)
                    update.insert(i, after)
                    return update
            else:
                # This page must be after.
                log.info(f"Page {page} must be after {before}")
                if before in update[i:]:
                    log.info(f"Found {before} in {update[i:]} :(")
                    update.remove(before)
                    update.insert(i, before)
                    return update

        log.info(f"{page} is good!")
    return update


def fix_update(update, rules) -> str:
    """Given an update, test it against the rules and fix."""

    while True:
        log.info(f"Testing {update}")
        # Test to see if update is alright
        if test_update(update, rules):
            log.info("Passed!")
            return update

        # If not alright, make one fix
        log.info("Failed :( Fixing and trying again!")
        update = make_one_fix(update, rules)
        log.info(f"{update}")


fixed_updates = []
with Progress(console=console) as progress:
    for update in track(updates):
        if test_update(update.split(","), rules):
            continue
        fixed_updates.append(",".join(fix_update(update.split(","), rules)))

middle_page_sum = calculate_middle_page_sum(fixed_updates)

print(f"Day 5 Part 2 Solution: {middle_page_sum}")
