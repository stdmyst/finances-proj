from sqlalchemy.dialects.postgresql import insert
import tinkoff
from connect_db import session, TinkoffTransaction


transactions = {
    'tinkoff': (tinkoff.get_transactions("_filepath_"), TinkoffTransaction)
}

for (source_transactions, TransactionClass) in transactions.values():
    for transaction in source_transactions:
        
        # transaction["user"] = 1

        session.execute(insert(TransactionClass).values(transaction).on_conflict_do_nothing())
        session.commit()

session.close()
