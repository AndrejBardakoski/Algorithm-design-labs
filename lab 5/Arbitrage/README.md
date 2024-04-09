# Arbitrage

Arbitrage is the use of discrepancies in currency exchange rates to transform one unit of a currency into more than one
unit of the same currency. For example, suppose that 1 US Dollar buys 0.5 British pounds, 1 British pound buys 10.0
French francs, and 1 French franc buys 0.21 US dollars. Then, by converting currencies, a clever trader can start with 1
US dollar and buy 0.5 * 10.0 * 0.21 = 1.05 US dollars, making a profit of 5 percent.

Your job is to write a program that takes a list of currency exchange rates as input and then determines whether
arbitrage is possible or not.

### Input

The input file will contain one or more test cases. On the first line of each test case there is an
integer `n` `(1<=n<=30)`, representing the number of different currencies. The next `n` lines each contain the name of
one currency. Within a name no spaces will appear. The next line contains one integer `m`, representing the length of
the table to follow. The last `m` lines each contain the name `c_i` of a source currency, a real number `r_ij` which
represents the exchange rate from `c_i` to `c_j` and a name `c_j` of the destination currency. Note that `c_i` and `c_j`
may be the same currency. Exchanges which do not appear in the table are impossible. Test cases are separated from each
other by a blank line. Input is terminated by a value of zero `0` for `n`.

### Output

For each test case, print one line telling whether arbitrage is possible or not in the format `Case case: Yes`,
respectively `Case case: No`.

### Sample 1

| input                                                                                                                                                                                                                                                                                                                                                                                                         | result                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 3<br>USDollar<br>BritishPound<br>FrenchFranc<br><br>3<br>USDollar 0.5 BritishPound<br>BritishPound 10.0 FrenchFranc<br>FrenchFranc 0.21 USDollar<br><br>3<br>USDollar<br>BritishPound<br>FrenchFranc<br><br>6<br>USDollar 0.5 BritishPound<br>USDollar 4.9 FrenchFranc<br>BritishPound 10.0 FrenchFranc<br>BritishPound 1.99 USDollar<br>FrenchFranc 0.09 BritishPound<br>FrenchFranc 0.19 USDollar<br><br>0  | Case 1: Yes<br>Case 2: No  |
