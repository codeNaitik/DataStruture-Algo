from Employee import employee;
from full import FullEmp;
from payout import Payout
from hour import Hour

payout =  Payout()
payout.add(FullEmp('john', 'hero', 70000))
payout.add(FullEmp('pohn', 'hero9', 80000))
payout.add(FullEmp('kohn', 'hero00', 90000))
payout.add(Hour('hith', 'kkk', 8,77))

payout.show()