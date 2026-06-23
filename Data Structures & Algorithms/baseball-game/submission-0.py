class Solution:
    def findSum(self,record):
        value = 0
        for i in record:
            value += i
        return value

    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "C":
                #remove previous score from record
                record = record[:-1]
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(i))
        return self.findSum(record)

