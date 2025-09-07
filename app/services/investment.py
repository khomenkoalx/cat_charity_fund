from datetime import datetime
from typing import Iterable, List, Tuple


def invest_money(target, sources: Iterable) -> Tuple[object, List[object]]:

    for source in sources:
        if getattr(target, 'fully_invested', False):
            break
        if getattr(source, 'fully_invested', False):
            continue

        target_needed = target.full_amount - target.invested_amount
        source_available = source.full_amount - source.invested_amount
        transfer_amount = min(target_needed, source_available)
        if transfer_amount <= 0:
            continue

        for obj in (target, source):
            if obj is target:
                obj.invested_amount += transfer_amount
            else:
                obj.invested_amount += transfer_amount

            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.utcnow()

    return target, list(sources)
