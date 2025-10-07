from collections import defaultdict, namedtuple, deque
from typing import List

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> List[str]:
        Transaction = namedtuple('Transaction', ['name', 'time', 'amount', 'city', 'original_string', 'idx'])
        parsed_transactions = []
        for i, t_str in enumerate(transactions):
            name, time_str, amount_str, city = t_str.split(',')
            parsed_transactions.append(
                Transaction(
                    name=name,
                    time=int(time_str),
                    amount=int(amount_str),
                    city=city,
                    original_string=t_str,
                    idx=i
                )
            )

        invalid_indices = set()
        user_transaction_windows = defaultdict(deque)

        for current_trans in parsed_transactions:
            if current_trans.amount > 1000:
                invalid_indices.add(current_trans.idx)
            q = user_transaction_windows[current_trans.name]
            while q and current_trans.time - q[0].time > 60:
                q.popleft()
            for prev_trans in q:
                if prev_trans.city != current_trans.city:
                    invalid_indices.add(current_trans.idx)
                    invalid_indices.add(prev_trans.idx)

            q.append(current_trans)

        result = []
        for idx in invalid_indices:
            result.append(parsed_transactions[idx].original_string)

        return result