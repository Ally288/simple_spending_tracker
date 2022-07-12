import pdb
from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag
import datetime

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

merchant_repository.delete_all()
transaction_repository.delete_all()
tag_repository.delete_all()

merchant_repository.select_all()
transaction_repository.select_all()
tag_repository.select_all()

tag1 = Tag("Charity")
tag_repository.save(tag1)

tag2 = Tag("Eating Out")
tag_repository.save(tag2)

tag3 = Tag("Entertainment")
tag_repository.save(tag3)

tag4 = Tag("Gifts")
tag_repository.save(tag4)

tag5 = Tag("Grocery")
tag_repository.save(tag5)

tag6 = Tag("Holidays")
tag_repository.save(tag6)

tag7 = Tag("Internal Transfer")
tag_repository.save(tag7)

tag8 = Tag("Online Shopping")
tag_repository.save(tag8)

tag9 = Tag("Transport")
tag_repository.save(tag9)

tag10 = Tag("Utility Bills")
tag_repository.save(tag10)


merchant1 = Merchant("Tesco", tag5)
merchant_repository.save(merchant1)

merchant2 = Merchant("Amazon", tag8)
merchant_repository.save(merchant2)

merchant3 = Merchant("Savings", tag7)
merchant_repository.save(merchant3)

merchant4 = Merchant("First Bus", tag9)
merchant_repository.save(merchant4)

merchant5 = Merchant("Save the Children", tag1)
merchant_repository.save(merchant5)

merchant6 = Merchant("Netflix", tag3)
merchant_repository.save(merchant6)

transaction1 = Transaction(datetime.date(2022, 5, 27), merchant1, tag5, 50.02)
transaction_repository.save(transaction1)

transaction2 = Transaction(datetime.date(2022, 5, 26), merchant2, tag8, 25.99)
transaction_repository.save(transaction2)

transaction3 = Transaction(datetime.date(2022, 5, 25), merchant3, tag7, 100.00)
transaction_repository.save(transaction3)

transaction4 = Transaction(datetime.date(2022, 5, 30), merchant6, tag7, 49.99)
transaction_repository.save(transaction4)

transaction5 = Transaction(datetime.date(2022, 6, 1), merchant4, tag9, 20.54)
transaction_repository.save(transaction5)


pdb.set_trace()
